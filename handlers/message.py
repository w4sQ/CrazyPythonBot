import logging

from aiogram import Dispatcher
from aiogram.types import Message

from config import servers
from helper import is_private, is_group, Server  # type: ignore
from keyboards import main_menu

logger = logging.getLogger(__name__)


async def start(message: Message):
    await message.reply("Hello, my friend!", reply_markup=main_menu())


async def check(message: Message):
    server_name = message.get_args()
    text = 'Такого сервера нет в списке, доступные сервера:\n' \
           f'{", ".join(servers.keys())}'
    if not server_name:
        text = 'Укажите сервер:\n' \
               '/check \<название\>'
    if server_name in servers:
        server = Server(servers[server_name])
        text = server.check()
    await message.reply(text)


def register(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(check, commands='check')
    logger.debug('handlers.message registered')
