import os

from dotenv import load_dotenv


load_dotenv()

STEPIC_USERNAME = os.getenv("STEPIC_USERNAME")
STEPIC_PASSWORD = os.getenv("STEPIC_PASSWORD")
