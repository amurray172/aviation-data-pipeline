
from dotenv import load_dotenv
import logging

from load.load_contacts import load_contacts

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv() 

def main():
    load_contacts()

if __name__ == "__main__":
    main()