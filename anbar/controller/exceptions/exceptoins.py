class PersonNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Person not found")


class ProductNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Product not found")

class StorageNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Storage not found")