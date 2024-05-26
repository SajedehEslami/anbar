from anbar.controller.exceptions.exceptoins import StorageNotFoundError
from anbar.model.da.da import DataAccess
from anbar.model.entity.storage import Storage

storage_da = DataAccess(Storage)


class StorageBl:
    @staticmethod
    def save(storage):
        return storage_da.save(storage)

    @staticmethod
    def edit(storage):
        if storage_da.find_by_id(storage.id):
            return storage_da.edit(storage)
        else:
            raise StorageNotFoundError()

    @staticmethod
    def remove(id):
        storage = storage_da.find_by_id(id)
        if storage:
            return storage_da.remove(storage)
        else:
            raise StorageNotFoundError()

    @staticmethod
    def find_all():
        storage_list = storage_da.find_all()
        if storage_list:
            return storage_list
        else:
            raise StorageNotFoundError()

    @staticmethod
    def find_by_id(id):
        storage = storage_da.find_by_id(id)
        if storage:
            return storage
        else:
            raise StorageNotFoundError()

    @staticmethod
    def find_count_by_product_id(product_id):
        storage_list = storage_da.find_by(Storage.product_id == product_id)
        if storage_list:
            return storage_list
        else:
            raise StorageNotFoundError()
