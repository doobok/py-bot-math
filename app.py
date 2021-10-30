from aiogram import types
from aiogram.dispatcher import Dispatcher


async def app(dp: Dispatcher, bot):
    @dp.message_handler(commands=['start'])
    async def echo(message: types.Message):

        print('is start command')

        await bot.send_message(message.chat.id, message.text)

    @dp.message_handler(commands=['help'])
    async def echo(message: types.Message):
        # Regular request
        # await bot.send_message(message.chat.id, message.text)
        print('is help command')

        await bot.send_message(message.chat.id, message.text)

    @dp.message_handler()
    async def echo(message: types.Message):
        # Regular request
        # await bot.send_message(message.chat.id, message.text)
        print('is another command')

        await bot.send_message(message.chat.id, message.text)

