class Product:

    def __init__(self, name, description, buying_price, selling_price, stock_quantity, vendor, low_stock, out_of_stock, id = None):
        self.name = name
        self.description = description
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.stock_quantity = stock_quantity
        self.vendor = vendor
        self.low_stock = low_stock
        self.out_of_stock = out_of_stock
        self.id = id
