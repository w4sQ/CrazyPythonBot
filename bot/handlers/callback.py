import logging

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

logger = logging.getLogger(__name__)


async def test(call: CallbackQuery):
    await call.message.reply("123")


def register(dp: Dispatcher):
    dp.register_callback_query_handler(test, text='test')

    logger.debug('handlers.callback registered')
