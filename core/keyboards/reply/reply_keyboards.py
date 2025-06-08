from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_menu_reply():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='💰 Пополнить'),
                KeyboardButton(text='🍪 Купить гемы'),
                KeyboardButton(text='🍪 Купить Brawl Pass')
            ],
            [
                KeyboardButton(text='🧑‍💻 Поддержка'),
                KeyboardButton(text='👤 Профиль')
            ],
            [
                KeyboardButton(text='📰 Новостник'),
                KeyboardButton(text='😀 Отзывы')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def back_menu_reply():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🏠 Главное меню')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard