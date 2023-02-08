import pdb
from models.product import Product
from models.vendor import Vendor

import repositories.product_repository as product_repository
import repositories.vendor_repository as vendor_repository

product_repository.delete_all()
vendor_repository.delete_all()

vendor1 = Vendor("Toby", "Toad", "Toad", "Jam")
vendor_repository.save(vendor1)
vendor2 = Vendor("Earl", "Grey", "Cat", "Trinkets")
vendor_repository.save(vendor2)
vendor3 = Vendor("Rupert", "Rupertson", "Frog", "Foraging")
vendor_repository.save(vendor3)
vendor4 = Vendor("Winnie", "BoBinnie", "Frog", "A Good Time")
vendor_repository.save(vendor4)

vendor_repository.select_all()

product1 = Product("Strawberry Jam", "Delicious", 1, 2, 10, vendor1)
product_repository.save(product1)
product2 = Product("Blueberry Jam", "Delicious", 1, 3, 10, vendor1)
product_repository.save(product2)
product3 = Product("Apricot Jam", "Delicious", 1, 4, 1, vendor1)
product_repository.save(product3)
product4 = Product("Mysterious Trinket", "Spoopy", 3, 5, 1, vendor2)
product_repository.save(product4)
product5 = Product("Mushroom", "Stinky", 1, 2, 5, vendor3)


pdb.set_trace()