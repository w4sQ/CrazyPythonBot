from aiogram import executor

import config_logging  # type: ignore
from bot import dp
from handlers import message, callback
from helper import is_private, is_group
import logging
from database import Database
logger = logging.getLogger(__name__)


def main():
    message.register(dp)
    callback.register(dp)
    dp.filters_factory.bind(is_private)
    dp.filters_factory.bind(is_group)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
    finally:
        Database().close()
