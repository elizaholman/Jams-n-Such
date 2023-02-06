import pdb
from models.product import Product
from models.vendor import Vendor

import repositories.product_repository as product_repository
import repositories.vendor_repository as vendor_repository

product_repository.delete_all()
vendor_repository.delete_all()

vendor1 = Vendor("Toby", "Toad")
vendor_repository.save(vendor1)
vendor2 = Vendor("Earl", "Grey")
vendor_repository.save(vendor2)
vendor3 = Vendor("Rupert", "")
vendor_repository.save(vendor3)
vendor4 = Vendor("Winnie", "")
vendor_repository.save(vendor4)

vendor_repository.select_all()

product1 = Product("Strawberry Jam", "Delicious", 1, 3, 10, vendor1)
product_repository.save(product1)
product2 = Product("Blueberry Jam", "Delicious", 1, 3, 10, vendor1)
product_repository.save(product2)
product3 = Product("Apricot Jam", "Delicious", 1, 3, 10, vendor1)
product_repository.save(product3)
product4 = Product("Apple Jam", "Delicious", 1, 3, 10, vendor1)
product_repository.save(product4)


pdb.set_trace()