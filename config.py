from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29174394"))
API_HASH = getenv("API_HASH", "2c83df6681819061fb6951c8d482b661")

BOT_TOKEN = getenv("BOT_TOKEN", "7254375706:AAF_ZivIzvn8Kzn2JshsktiRIU-1c5-ay90")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://vasudurairam:vasudurai123@cluster01.3l3sszt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01")

OWNER_ID = int(getenv("OWNER_ID", 6916055129))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FallenAssociation")
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/6b8905e7e063a96bc6030.jpg")
