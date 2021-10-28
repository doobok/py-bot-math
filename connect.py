import os
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)