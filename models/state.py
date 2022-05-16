#!/usr/bin/python3
""" State Module for HBNB project """    
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    if env.get('HBNB_ENV') == 'db':
        cities = relationship('City',
                              backref='state',
                              cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.__dict__.update(kwargs)

    @property
    def cities(self):
        """
        getter cities
        """
        from models import storage

        objs = []
        for key, value in storage.all('City').items():
            if (value.state_id == self.id):
                objs.append(value)

        return objs
