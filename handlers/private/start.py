from aiogram.dispatcher.webhook import SendMessage
from aiogram.types import Message


async def start(m: Message):
    """
    Responds to /start with basic greeting
    """
    print('is handler Start', m)

    # return SendMessage(m.chat.id, m.text)
    # print('is send message:', SendMessage(m.chat.id, m.text))
    await m.answer(f"Hello there, {m.from_user.first_name}!")
    # return result

    # await m.answer(f"Hello there, {m.from_user.first_name}!")