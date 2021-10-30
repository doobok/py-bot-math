from aiogram import Dispatcher, types
from aiogram.dispatcher.webhook import SendMessage

from .private.start import start


async def setup(dp: Dispatcher):
    # async def setup(m:  types.Message):
    """
    Setup handlers
    """

    return 'five'

    print('is init handler dp = ', dp)

    dp.message_handler(start, commands=["start"])

    # SendMessage(dp.chat.id, 'KABOOM').reply(message)

    # aiogram.dispatcher.webhook(start, commands=["start"])
