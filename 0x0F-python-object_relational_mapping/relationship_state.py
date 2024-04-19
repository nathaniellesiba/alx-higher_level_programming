#!/usr/bin/python3
"""improve state file"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from relationship_city import Base, City

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
            autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
            cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name
