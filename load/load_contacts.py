import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from extract import get_data
from models import Base, ContactModel, Contact

load_dotenv() 

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")


def get_engine():
    return create_engine(DATABASE_URL)

def clear_contacts():
    engine = get_engine()
    Base.metadata.drop_all(engine)

def load_contacts(contacts: list[Contact]):
    engine = get_engine()
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for contact in contacts:
            contact_row = ContactModel(**contact.__dict__)
            session.merge(contact_row)

        session.commit()
    finally:
        session.close()

