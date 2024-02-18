#!/usr/bin/python3
"""A new engine with DB concept"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity


classes = {"State": State, "City": City,
           "User": User, "Place": Place,
           "Review": Review, "Amenity": Amenity}


class DBStorage:
    """New engine DBStorage for mysql"""
    __engine = None
    __session = None

    def __init__(self):
        """new dbstorage instance"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB
                                       ), pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)"""
        dictionary = {}
        if cls is None:
            for i in classes.values():
                objs = self.__session.query(i).all()
                for obj in objs:
                    k = obj.__class__.__name__ + '.' + obj.id
                    dictionary[k] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                k = obj.__class__.__name__ + '.' + obj.id
                dictionary[k] = obj
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as excep:
                self.__session.rollback()
                raise excep

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """calls remove session"""
        self.__session.remove()
