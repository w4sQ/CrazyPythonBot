import asyncio
import logging
import random

from aiogram import Dispatcher
from aiogram.types import Message

from helper import is_private, is_group
from keyboards import main_menu

logger = logging.getLogger(__name__)


async def start(message: Message):
    await message.reply("Hello, my friend!", reply_markup=main_menu())


async def spam(message: Message):
    if message.reply_to_message is not None:
        spam_user = message.reply_to_message.from_user.username
        await message.reply(spam_user)
    else:
        pass


async def test(message: Message):
    await message.reply('test')


async def cum(message: Message):
    text = "Размер вашей cum-пушки: {size} см."
    msg = await message.reply(text.format(size=random.randint(3, 44)), protect_content=True)
    sticker = await message.reply_sticker('CAACAgIAAxkBAAEHYVljzGF0ux80GskQWlNb6UsLzex-QAACxw8AAj-VwUqoJZJZftReKS0E')
    await asyncio.sleep(2)
    await msg.edit_text(text.format(size=random.randint(1, 4)))
    await sticker.delete()


def register(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(test, is_private(), commands='test')
    dp.register_message_handler(spam, is_group(), commands='spam')
    dp.register_message_handler(cum, commands='cum')

    logger.debug('handlers.message registered')
