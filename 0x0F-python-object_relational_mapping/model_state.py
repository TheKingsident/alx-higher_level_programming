#!/usr/bin/python3
"""
This module defines the State class with SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class:
    - Inherits from Base.
    - Links to MySQL table states.
    - Has id and name attributes.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
