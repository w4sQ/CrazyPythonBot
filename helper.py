import asyncio
import logging

import mcstatus.pinger
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from mcstatus import JavaServer

logger = logging.getLogger(__name__)


class is_private(BoundFilter):
    async def check(self, message: Message):
        chat_type = message.chat.type
        if chat_type == "private":
            return True
        msg = await message.answer("Это команда достпуна только в личных сообщениях!", disable_notification=True)
        await asyncio.sleep(1.5)
        await msg.delete()


class is_group(BoundFilter):
    async def check(self, message: Message):
        chat_type = message.chat.type
        if chat_type != "private":
            return True
        msg = await message.answer("Это команда достпуна только в групповых чатах!", disable_notification=True)
        await asyncio.sleep(1.5)
        await msg.delete()


class Server:

    def __init__(self, address: str):
        self.address = address

    def check(self) -> str:
        players = self.players_online()
        if players:
            msg = f'Онлайн: {len(players)}\n' \
                  f'Игроки: {", ".join(players)}'
            return msg
        return 'Сервер выключен! -_-'

    def players_online(self) -> list | None:
        player_list = [player['name'] for player in self.__connection_to_server().raw['players']['sample']]
        return player_list

    # 'players'
    def __connection_to_server(self) -> mcstatus.pinger.PingResponse | None:
        try:
            server = JavaServer.lookup(address=self.address, timeout=10)
            logger.info(f'Connected to {self.address}')
            resp = server.status()
            return resp
        except TimeoutError:
            logger.warning(f'{self.address} is offline')
