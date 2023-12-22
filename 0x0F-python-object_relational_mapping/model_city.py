#!/usr/bin/python3
"""
Class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class:
    - Inherits from Base.
    - Links to the MySQL table cities.
    - Has id, name, and state_id attributes.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
