from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_start = KeyboardButton('/start_game 😀')
btn_help = KeyboardButton('/help 🚑')
btn_location = KeyboardButton('/loc 🌎', request_location=True)

kb_main_menu.add(btn_help, btn_start)
kb_main_menu.add(btn_location)



