from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
from models.vendor import Vendor
import repositories.product_repository as product_repository
import repositories.vendor_repository as vendor_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all() 
    return render_template("products/index.html", all_products = products)

@products_blueprint.route("/products/<id>", methods=["GET"])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product = product)

@products_blueprint.route("/products/new", methods=["GET"])
def new_product():
    vendors = vendor_repository.select_all()
    return render_template("products/new.html", all_vendors = vendors)

@products_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    stock_quantity = request.form["stock_quantity"]
    vendor_id = request.form["vendor_id"]
    vendor = vendor_repository.select(vendor_id)
    product = Product(name, description, buying_price, selling_price, stock_quantity, vendor, False, False)
    product_repository.save(product)
    return redirect("/products")

@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    vendor = vendor_repository.select_all()
    return render_template('products/edit.html', product = product, all_vendors = vendor)

@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    description = request.form["description"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    stock_quantity = request.form["stock_quantity"]
    vendor_id = request.form["vendor_id"]
    vendor = vendor_repository.select(vendor_id)
    product = Product(name, description, buying_price, selling_price, stock_quantity, vendor, False, False, id)
    product_repository.update(product)
    return redirect("/products")

@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")






@products_blueprint.route("/vendors")
def vendors():
    vendors = vendor_repository.select_all()
    return render_template("vendors/index.html", all_vendors = vendors)

@products_blueprint.route("/vendors/<id>", methods=["GET"])
def show_vendor(id):
    vendor = vendor_repository.select(id)
    return render_template('vendors/show.html', vendor = vendor)

@products_blueprint.route("/vendors/new", methods=["GET"])
def new_vendor():
    return render_template("vendors/new.html", all_vendors = vendors)

@products_blueprint.route("/vendors", methods=["POST"])
def create_vendor():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    vendor = Vendor(first_name, last_name)
    vendor_repository.save(vendor)
    return redirect("/vendors")

@products_blueprint.route("/vendors/<id>/edit", methods=['GET'])
def edit_vendor(id):
    vendor = vendor_repository.select(id)
    return render_template('vendors/edit.html', vendor = vendor)

@products_blueprint.route("/vendors/<id>", methods=["POST"])
def update_vendor(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    vendor = Vendor(first_name, last_name, id)
    vendor_repository.update(vendor)
    return redirect("/vendors")

@products_blueprint.route("/vendors/<id>/delete", methods=["POST"])
def delete_vendor(id):
    vendor_repository.delete(id)
    return redirect("/vendors")