from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from collections import namedtuple
from db.connection import Base, engine


ParamDefault = namedtuple("ParamDefault", ["id", "name"])


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), default=None)
    email = Column(String(255), unique=True, index=True)
    is_active = Column(Boolean, default=False)

    items = relationship("Item", back_populates="owner")
    def __repr__(self):
        return ParamDefault(self.id, self.name)


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), default=None)
    title = Column(String(255), default=None)
    description = Column(String(255), index=True) 
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='items')  

    def __repr__(self):
        return ParamDefault(self.id, self.name)

    
