from db.run_sql import run_sql

from models.product import Product
from models.vendor import Vendor
import repositories.vendor_repository as vendor_repository

def save(product):
    sql = "INSERT INTO products (name, description, buying_price, selling_price, stock_quantity, low_stock, out_of_stock, vendor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.buying_price, product.selling_price, product.stock_quantity, product.low_stock, product.out_of_stock, product.vendor_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        vendor = vendor_repository.select(row['vendor_id'])
        product = Product(row['name'], row['description'], row['buying_price'], row['selling_price'], row['stock_quantity'], row['low_stock'], row['out_of_stock'], vendor, row['id'] )
        products.append(product)
    return products


def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        vendor = vendor_repository.select(result['vendor_id'])
        product = Product(result['name'], result['description'], result['buying_price'], result['selling_price'], result['stock_quantity'], result['low_stock'], result['out_of_stock'], vendor, result['id'] )
    return product


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update (product):
    sql = "UPDATE products SET (name, description, buying_price, selling_price, stock_quantity, low_stock, out_of_stock, vendor_id) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values =  [product.name, product.description, product.buying_price, product.selling_price, product.stock_quantity, product.low_stock, product.out_of_stock, product.vendor_id]
    run_sql(sql, values)
