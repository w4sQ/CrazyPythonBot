from aiogram import types


def main_menu() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
    start_button = types.InlineKeyboardButton(text='Start', callback_data='test')
    keyboard.add(start_button)
    return keyboard
