import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from extract.extractor import get_data
from models import Base, ContactModel

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")


def load_contacts():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    contacts = get_data()

    try:
        for contact in contacts:
            contact_row = ContactModel(**contact.__dict__)
            session.merge(contact_row)

        session.commit()
    finally:
        session.close()

