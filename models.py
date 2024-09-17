from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer)
    venue_id = Column(Integer)
