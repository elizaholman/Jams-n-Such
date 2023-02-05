from db.run_sql import run_sql

from models.vendor import Vendor
from models.product import Product


def save(vendor):
    sql = "INSERT INTO vendors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [vendor.first_name, vendor.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vendor.id = id
    return vendor


def select_all():
    vendors = []

    sql = "SELECT * FROM vendors"
    results = run_sql(sql)

    for row in results:
        vendor = Vendor(row['first_name'], row['last_name'], row['id'] )
        vendors.append(vendor)
    return vendors


def select(id):
    vendor = None
    sql = "SELECT * FROM vendors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        vendor = Vendor(result['first_name'], result['last_name'], result['id'] )
    return vendor


def delete_all():
    sql = "DELETE FROM vendors"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM vendors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vendor):
    sql = "UPDATE vendors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [vendor.first_name, vendor.last_name, vendor.id]
    run_sql(sql, values)


def products(vendor):
    products = []

    sql = "SELECT * FROM products WHERE user_id = %s"
    values = [vendor.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['description'], row['buying_price'], row['selling_price'], row['stock_quantity'], vendor,  row['low_stock'], row['out_of_stock'], row['id'])
        products.append(product)
    return products
