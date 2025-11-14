from sqlalchemy import ARRAY, Boolean, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ContactModel(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    icao24 = Column(String, nullable=False)
    callsign = Column(String, nullable=True)
    origin_country = Column(String, nullable=False)
    time_position = Column(Integer, nullable=True)
    last_contact = Column(Integer, nullable=False)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    baro_altitude = Column(Float, nullable=True)
    on_ground = Column(Boolean, nullable=False)
    velocity = Column(Float, nullable=True)
    true_track = Column(Float, nullable=True)
    vertical_rate = Column(Float, nullable=True)
    sensors = Column(ARRAY(Integer), nullable=True)
    geo_altitude = Column(Float, nullable=True)
    squawk = Column(String, nullable=True)
    spi = Column(Boolean, nullable=False)
    position_source = Column(Integer, nullable=False)
    position_source_name = Column(String, nullable=True)
    category = Column(Integer, nullable=True)
    category_name = Column(String, nullable=True)
    