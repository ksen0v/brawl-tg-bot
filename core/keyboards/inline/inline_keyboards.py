from aiogram.utils.keyboard import InlineKeyboardBuilder
from config_loader import MESSAGES, GEMS

def top_up_by_card_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='💰 Банковской картой', callback_data='top_up_by_card')
    keyboard.adjust(1)

    return keyboard.as_markup()

def popup_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='💳 Пополнить', callback_data='top_up_by_card_two')
    keyboard.adjust(1)

    return keyboard.as_markup()

def contact_support_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='✉️ Связаться', callback_data='contact_support')
    keyboard.adjust(1)

    return keyboard.as_markup()

def main_menu_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='🏠 Главное меню', callback_data='main_menu')
    keyboard.adjust(1)

    return keyboard.as_markup()

def news_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='📰 Перейти в новостник', url=str(MESSAGES['link_to_news_for_keyboard']))
    keyboard.adjust(1)

    return keyboard.as_markup()

def reviews_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='😄 Отзывы', url=str(MESSAGES['link_to_reviews_for_keyboard']))
    keyboard.adjust(1)

    return keyboard.as_markup()

def buy_gems_inline():
    keyboard = InlineKeyboardBuilder()
    for i in range(10):
        lot = str(GEMS[f"{i + 1}"]).split(':', 1)
        keyboard.button(text=f'Brawl Stars {lot[0]} Гемов | {lot[1]} ₽', callback_data='no_money')
    keyboard.adjust(1)

    return keyboard.as_markup()

def buy_pass_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=f'Brawl Pass Plus | 1049 руб', callback_data='no_money')
    keyboard.button(text=f'Brawl Pass | 749 руб', callback_data='no_money')
    keyboard.adjust(1)

    return keyboard.as_markup()