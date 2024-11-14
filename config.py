# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "239130"))
API_HASH = getenv("API_HASH", "4d717a67ebde0ace80cd22c6")
BOT_TOKEN = getenv("BOT_TOKEN", "74430R_um_D4zHToFIiCAv8M1q4Co")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5315677437").split()))
MONGO_DB = getenv("MONGO_DB", "mfjhfjfhfhhfjhjnow")
LOG_GROUP = getenv("LOG_GROUP", "yuy1326")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002314107303"))
