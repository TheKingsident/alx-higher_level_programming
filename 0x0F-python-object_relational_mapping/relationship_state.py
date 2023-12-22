#!/usr/bin/python3
"""
Class definition of a State and an instance Base.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class:
    - Inherits from Base.
    - Links to the MySQL table states.
    - Has id and name attributes.
    - Has a relationship with the City class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
