#!/usr/bin/python3
"""Class definition of State"""

from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class definition of a State and inherits  Base

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id
    name(sqlalchemy.String): The state's name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
