from aiogram import executor

import config_logging  # type: ignore
from bot import dp
from handlers import message, callback
from helper import is_private, is_group


def main():
    message.register(dp)
    callback.register(dp)
    dp.filters_factory.bind(is_private)
    dp.filters_factory.bind(is_group)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
