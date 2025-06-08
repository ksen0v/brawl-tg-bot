from aiogram import Bot, Dispatcher, F
import asyncio

<<<<<<< HEAD
from core.handlers.main_handlers import buy_pass, no_money, reviews, news, get_start, top_up, process_top_up_amount, top_up_by_card, bill_proceed, buy_gems, top_up_query, pay_out, support, support_send_message, support_message_send_success, profile
=======
from core.handlers.main_handlers import buy_pass, no_money reviews, news, rate, get_start, top_up, process_top_up_amount, top_up_by_card, bill_proceed, buy_gems, top_up_query, pay_out, support, support_send_message, support_message_send_success, profile
>>>>>>> 7cea6f9c10272733e9cba0dffefe11b02e6087d1
from config_loader import TOKEN, ADMIN_ID, MESSAGES
from core.states.main_states import BillStates, Abstract

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def startup_bot(bot: Bot):
    try:
        await bot.send_message(ADMIN_ID, MESSAGES['startup_admin'])
        logger.info(f'Сообщение о запуске успешно отправлено админу - {ADMIN_ID}')
    except Exception as e:
        logger.error(f'Не удалось отправить сообщение о запуске админу - {ADMIN_ID}. Ошибка: {e}')


async def main():
    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(startup_bot)

    dp.message.register(get_start, F.text == '/start')
    dp.message.register(get_start, F.text == '🏠 Главное меню')
    dp.message.register(top_up, F.text == '💰 Пополнить')
    dp.message.register(process_top_up_amount, BillStates.amount)
    dp.callback_query.register(top_up_by_card, F.data == 'top_up_by_card')
    dp.message.register(bill_proceed, BillStates.photo)
    dp.message.register(buy_gems, F.text == '🍪 Купить гемы')
    dp.message.register(buy_pass, F.text == '🍪 Купить Brawl Pass')
    dp.callback_query.register(no_money, F.data == 'no_money')
    dp.callback_query.register(top_up_query, F.data == 'top_up_by_card_two')
    dp.message.register(pay_out, F.text == '🍪 Вывод')
    dp.message.register(support, F.text == '🧑‍💻 Поддержка')
    dp.callback_query.register(support_send_message, F.data == 'contact_support')
    dp.message.register(support_message_send_success, Abstract.temp)
    dp.message.register(profile, F.text == '👤 Профиль')
    dp.callback_query.register(get_start, F.data == 'main_menu')
    dp.message.register(news, F.text == '📰 Новостник')
    dp.message.register(reviews, F.text == '😀 Отзывы')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
