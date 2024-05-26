from anbar.model.entity import *



class Storage(Base):
    __tablename__ = "storage_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer)
    transaction_type = Column(String(6))
    date_time = Column(DateTime)

    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    product = relationship("Product")

    person_id = Column(Integer, ForeignKey("person_tbl.id"))
    person = relationship("Person")
    # def __init__(self, product, count):
    #     self.id = None
    #     self.product = product
    #     self.count = count
    # todo : getter / setter (validation)