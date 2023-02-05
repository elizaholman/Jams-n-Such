from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.vendor_repository as vendor_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all() 
    return render_template("products/index.html", all_products = products)

@products_blueprint.route("/vendors")
def vendors():
    vendors = vendor_repository.select_all()
    return render_template("vendors/index.html", all_vendors = vendors)

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
