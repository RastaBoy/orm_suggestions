from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class House(DeclarativeBase):
    __tablename__ = 'houses'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    address = Column(String, nullable=False)

    jitels = relationship('Jitel')
    

class Jitel(DeclarativeBase):
    __tablename__ = 'jitels'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id'))
    
    house = relationship(House, back_populates='jitels')
    