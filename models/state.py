#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """A state class"""
    __tablename__ = 'states'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )

    else:
        @property
        def cities(self):
            '''returns FileStorage relationship between State and City'''
            from models import storage
            cityr = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    cityr.append(city)
            return cityr
