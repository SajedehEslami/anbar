from anbar.model.entity import *

class Product(Base):
    __tablename__ = "product_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20))
    brand = Column(String(20))
    serial= Column(String(20))
    status = Column(Boolean, default=True)

    # def __init__(self, id, name, family, status=True):
    #     self.id = id
    #     self.name = name
    #     self.family = family
    #     self.status = status


    # todo : getter / setter (validation)