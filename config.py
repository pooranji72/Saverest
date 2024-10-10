# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23940130"))
API_HASH = getenv("API_HASH", "4d717a6f888e37b7ebde0ace80cd22c6")
BOT_TOKEN = getenv("BOT_TOKEN", "7443034654:AAH83ai22x0R_um_D4zHToFIiCAv8M1q4Co")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5315677437").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://amit:amitrajera@now.xhnas.mongodb.net/?retryWrites=true&w=majority&appName=now")
LOG_GROUP = getenv("LOG_GROUP", "yuy1326")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002314107303"))
