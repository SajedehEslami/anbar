from anbar.controller.exceptions.exceptoins import ProductNotFoundError
from anbar.model.da.da import DataAccess
from anbar.model.entity.product import Product

product_da = DataAccess(Product)


class ProductBl:
    @staticmethod
    def save(product):
        return product_da.save(product)

    @staticmethod
    def edit(product):
        if product_da.find_by_id(product.id):
            return product_da.edit(product)
        else:
            raise ProductNotFoundError()

    @staticmethod
    def remove(id):
        product = product_da.find_by_id(id)
        if product:
            return product_da.remove(product)
        else:
            raise ProductNotFoundError()

    @staticmethod
    def find_all():
        product_list = product_da.find_all()
        if product_list:
            return product_list
        else:
            raise ProductNotFoundError()

    @staticmethod
    def find_by_id(id):
        product = product_da.find_by_id(id)
        if product:
            return product
        else:
            raise ProductNotFoundError()

    @staticmethod
    def find_count_by_id(id):
        product_list = product_da.find_by(Product.id == id)
        if product_list:
            return product_list
        else:
            raise ProductNotFoundError()
