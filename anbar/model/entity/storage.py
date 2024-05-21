from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from anbar.model.entity.base import Base
from anbar.model.entity.person import Person
from anbar.model.entity.product import Product


class Storage(Base):
    __tablename__ = "storage_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer)
    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    product = relationship(Product)


    def __init__(self, product, count):
        self.id = None
        self.product = product
        self.count = count
