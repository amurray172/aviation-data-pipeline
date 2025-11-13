
from dotenv import load_dotenv
from extract.extractor import get_data
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv() 

def main():
    contacts = get_data()
    for contact in contacts:
        logger.info(contact)


if __name__ == "__main__":
    main()