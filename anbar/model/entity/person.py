from anbar.model.entity import *


class Person(Base):
    __tablename__ = "person_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)

    # def __init__(self, id, name, family, status=True):
    #     self.id = id
    #     self.name = name
    #     self.family = family
    #     self.status = status

    # todo : getter / setter (validation)