#!/usr/bin/python3
"""
Module to provide a database storage interface using SQLAlchemy
"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys


class DBStorage():
    """
    Database storage class using SQLAlchemy
    for interaction with a MySQL database.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the DBStorage instance and create the database engine.
        """
        env = getenv('HBNB_ENV')
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                user, password, host, database), pool_pre_ping=True)

        if env == 'test':
            pass

    def all(self, cls=None):
        """
        Query and return all objects from the database.

        Args:
            cls (str): The name of the class to query.
                        If None, query all objects from all tables.

        Returns:
            dict: A dictionary of objects, format {'classname.id': object}.
        """
        classes = {'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review, 'User': User}
        if cls in classes.keys():
            cls = classes[cls]

        if cls is None:
            # If cls is not specified, query all objects from all tables
            objects = []
            objects += self.__session.query(State).all()
            objects += self.__session.query(City).all()
        else:
            # Query all objects of the specified class
            objects = self.__session.query(cls).all()

        return {f'{obj.__class__.__name__}.{obj.id}': obj for obj in objects}

    def new(self, obj):
        """
        Add a new object to the current database session.

        Args:
            obj: The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit changes to the database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the database session.

        Args:
            obj: The object to delete from the session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and set up a new session.
        """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close the current database session.
        """
        self.__session.close()
