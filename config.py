from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
#OWNER_ID = int(getenv("7037832227"))
OWNER_ID = int(getenv("OWNER_ID", "6730120198"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
MUST_JOIN = getenv("MUST_JOIN", None)
