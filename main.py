import logging

from extract import get_data
from load import load_contacts, clear_contacts
from transform import filter_ground_contacts, filter_emergency_contacts

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("Clearing existing contacts from the database...")
    clear_contacts()
    logger.info("Fetching new contacts from OpenSky Network...")
    contacts = get_data()
    logger.info(f"Loading ${len(contacts)} new contacts into the database...")
    load_contacts(contacts)
    logger.info("Data loading complete.")
    airborne_contacts = filter_ground_contacts(contacts)
    logger.info(f"Number of airborne contacts (above 500ft): {len(airborne_contacts)}")
    emergency_contacts = filter_emergency_contacts(contacts)
    logger.info(f"Number of emergency contacts (squawk codes 7500, 7600, 7700): {len(emergency_contacts)}")

if __name__ == "__main__":
    main()