# test_models.py

from models import Band, Venue, Concert, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

@pytest.fixture
def session():
    engine = create_engine('sqlite:///test_database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def test_create_band(session):
    band = Band(name="Sauti soul", hometown="Nairobi")
    session.add(band)
    session.commit()
    assert band in session.query(Band).all()

def test_create_venue(session):
    venue = Venue(title="Carnivore", city="Nairobi")
    session.add(venue)
    session.commit()
    assert venue in session.query(Venue).all()

def test_create_concert(session):
    band = Band(name="Sauti soul", hometown="Nairobi")
    venue = Venue(title="Carnivore", city="Nairobi")
    session.add_all([band, venue])
    session.commit()
    concert = Concert(date="2024-10-10", band=band, venue=venue)
    session.add_all([band, venue, concert])
    session.commit()
    assert concert in session.query(Concert).all()
    
