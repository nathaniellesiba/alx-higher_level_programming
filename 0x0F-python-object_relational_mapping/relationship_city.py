#!/usr/bin/python3
"""improve city file"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
            nullable=False, autoincrement=True)
    
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        self.name = name
