import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Tom bot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Tom_01157")
ALIVE_NAME = getenv("ALIVE_NAME", "Tom")
BOT_USERNAME = getenv("BOT_USERNAME", "Tom01212bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ahmed1157")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "music_Desha")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Tom01255")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4d8336527d0fb27ca8e8e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Tom01212/almheb-help.git")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/4d8336527d0fb27ca8e8e.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/4d8336527d0fb27ca8e8e.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/4d8336527d0fb27ca8e8e.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/4d8336527d0fb27ca8e8e.jpg")
