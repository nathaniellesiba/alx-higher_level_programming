#!/usr/bin/python3
"""Write a python file that contains
the class definition of a State and
an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Ensure to import all classes that inherit from Base before calling Base.metadata.create_all(engine)
# Example:
# from your_module import State

# Create an engine to connect to the MySQL server running on localhost at port 3306
engine = create_engine('mysql://username:password@localhost:3306/database_name')

# Create the tables
Base.metadata.create_all(engine)
