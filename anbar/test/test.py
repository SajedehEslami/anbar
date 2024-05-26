from datetime import datetime

from anbar.controller.person_controller import PersonController
from anbar.model.bl.storage import StorageBl
from anbar.model.da.da import DataAccess
from anbar.model.entity import *


# person = Person()
# person.name = "ali"
# person.family = "alipour"
# p_da = DataAccess(Person)
# p_da.save(person)
#
# person = p_da.find_by_id(1)
# print(person)
#
#
# product = Product()
# product.name = "mobile"
# product.brand = "iPhone"
# pr_da = DataAccess(Product)
# pr_da.save(product)
#
# product = pr_da.find_by_id(1)
# print(product)
#
#
#
# storage = Storage()
# storage.product = product
# storage.person = person
# storage.date_time = datetime.now()
# storage.count = 5
# storage.transaction_type = "income"
# st_da = DataAccess(Storage)
# st_da.save(storage)
#
# storage = st_da.find_by_id(1)
#
# print(storage)

# print(StorageBl.find_count_by_product_id(1))

print(PersonController.save("test", "test", False))
