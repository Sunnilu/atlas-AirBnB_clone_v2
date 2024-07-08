#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    __tablename__ = 'states'

    # Attributes for both types of storage
    name = Column(String(128), nullable=False)

    # Define relationship differently based on storage type
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """
            Getter method for cities linked to the current State
            """
            from models import storage  # Ensure this import is correctly set for your project
            city_objs = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return string representation of State"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
