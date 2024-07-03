#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.config import storage_t


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    # Check the global storage type 
    # to decide on the class attributes
    if storage_t == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='cities')
    else:
        # For file system storage, placeholders are 
        # defined instead of actual columns
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        # Call the parent class initializer
        super().__init__(*args, **kwargs)
