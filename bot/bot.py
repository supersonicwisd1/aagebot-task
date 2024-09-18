import telebot
import uuid
from dotenv import load_dotenv
import os

# Load the bot token and server link (url) from environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
SERVER_LINK = os.getenv('SERVER_LINK')

from bot.db import Database

class TelegramBot:
    def __init__(self, db: Database):
        self.db = db
        self.bot = telebot.TeleBot(API_KEY)
        self.bot.message_handler(commands=['create'])(self.create_uuid)

    def create_uuid(self, message):
        user_id = message.from_user.id
        new_uuid = str(uuid.uuid4())
        self.db.insert_user_link(user_id, new_uuid)
        self.bot.reply_to(message, f"Your link is: {SERVER_LINK}/link/{new_uuid}")

    def start(self):
        self.bot.polling()
