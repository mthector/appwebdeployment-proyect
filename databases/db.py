from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Category(db.Model):
    """Categories of Instruments"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return {u'<{self.__class__.__name__}: {self.id}>'.format(self=self)}

class Supplier(db.Model):
    """Suppliers of Instruments"""
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Instrument(db.Model):
    """Instruments"""
    __tablename__ = 'instruments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image = Column(String(200), nullable=True)
    image_2 = Column(String(200), nullable=True)
    
    supplier_id = Column(Integer,ForeignKey('suppliers.id'), nullable=False)
    supplier = relationship('Supplier', backref='instruments')

    category_id = Column(Integer,ForeignKey('categories.id'), nullable=False)
    category = relationship('Category', backref='instruments')

class User(db.Model, UserMixin):
    """Users"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=True)
