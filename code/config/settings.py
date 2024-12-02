import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS").split(",")  
STOP_WORDS = os.getenv("STOP_WORDS").split(",")