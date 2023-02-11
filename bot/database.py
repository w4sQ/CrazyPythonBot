import asyncio
import logging
from typing import LiteralString, Iterable, Any

import aiosqlite

import config

logger = logging.getLogger(__name__)


class Database:

    def __init__(self):
        self.__connection = await aiosqlite.connect(config.SQLITE_DB_FILE)

    async def _get_cursor(self, sql: LiteralString, params: Iterable[Any] | None) -> aiosqlite.Cursor:
        args: tuple[LiteralString, Iterable[Any] | None] = (sql, params)
        cursor = await self.__connection.execute(*args)
        self.__connection.row_factory = aiosqlite.Row
        return cursor

    def close(self) -> None:
        asyncio.run(self.__async_close())

    async def __async_close(self) -> None:
        await (await self.__connection).close()

    async def fetch_all(self, sql: LiteralString, params: Iterable[Any] | None = None) -> list:
        cursor = await self._get_cursor(sql, params)
        rows = await cursor.fetchall()
        result = [row for row in rows]
        return result

    async def execute(self, sql: LiteralString, params: Iterable[Any] | None = None, *,
                      autocommit: bool = True) -> None:
        args: tuple[LiteralString, Iterable[Any] | None] = (sql, params)
        await self.__connection.execute(*args)
        if autocommit:
            await self.__connection.commit()
