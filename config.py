from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "6293739020"))
API_HASH = getenv("API_HASH", "ee6df88753c36eeab95391940ba3844f")

BOT_TOKEN = getenv("BOT_TOKEN", "6293739020:AAEWNsNNG5pzU5K1RQ2by7xPdT9ua0nA5YY")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://karjr002:INCyT5eXfqjoiYQ4@cluster0.6swcped.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6088155585))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")
