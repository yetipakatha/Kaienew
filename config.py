from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22175021"))
API_HASH = getenv("API_HASH", "9dd328229c3bb96dc1a112c3eac79a1a")

BOT_TOKEN = getenv("BOT_TOKEN", "7476307432:AAFKIp4JpWnaWYNlLWcvqIfLbODDvVt8eVw")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://vasudurairam:vasudurai123@cluster01.3l3sszt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01")

OWNER_ID = int(getenv("OWNER_ID", 655594746))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/we_are_universee")
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/7f02fa86d8b5f924be21b.jpg")
