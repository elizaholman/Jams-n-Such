import pdb
from models.product import Product
from models.vendor import Vendor

import repositories.product_repository as product_repository
import repositories.vendor_repository as vendor_repository

product_repository.delete_all()
vendor_repository.delete_all()

vendor1 = Vendor("Toby", "Toad")
vendor_repository.save(vendor1)
# Vendor2 = Vendor("Victor", "McDade")
# vendor_repository.save(Vendor2)

vendor_repository.select_all()

product1 = Product("strawberry jam", "delicious", 1, 3, 10, vendor1)
product_repository.save(product1)

# product2 = Product("Go for a run", vendor1, 30, True)
# product_repository.save(product2)


pdb.set_trace()