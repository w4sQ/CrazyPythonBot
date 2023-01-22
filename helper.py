import asyncio

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


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
