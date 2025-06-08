from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery, ContentType
import random

from core.keyboards.reply.reply_keyboards import start_menu_reply, back_menu_reply
from core.keyboards.inline.inline_keyboards import reviews_inline, news_inline, top_up_by_card_inline, buy_gems_inline, contact_support_inline, popup_inline, buy_pass_inline
from config_loader import MESSAGES, MIN_PAYUP_RUB, ADMIN_ID
from core.states.main_states import BillStates, Abstract


async def get_start(message: Message, state: FSMContext):
    await state.clear()
    photo = FSInputFile('start_photo.jpg')  # Replace with your photo filename in root folder
    await message.answer_photo(photo, caption=MESSAGES['startup_user'], reply_markup=start_menu_reply())

async def top_up(message: Message, state: FSMContext):
    photo = FSInputFile('top_up_photo.jpg')
    await message.answer_photo(photo, caption=MESSAGES['top_up'], reply_markup=back_menu_reply())
    await state.set_state(BillStates.amount)

async def top_up_query(callback_query: CallbackQuery, state: FSMContext):
    photo = FSInputFile('top_up_photo.jpg')
    await callback_query.message.answer_photo(photo, caption=MESSAGES['top_up'], reply_markup=back_menu_reply())
    await callback_query.answer()
    await state.set_state(BillStates.amount)

async def process_top_up_amount(message: Message, state: FSMContext):
    amount_text = message.text.strip()
    if amount_text.isdigit():
        if int(amount_text) >= MIN_PAYUP_RUB:
            await message.answer(MESSAGES['top_up_proceed'], reply_markup=top_up_by_card_inline())
            await state.update_data(current_top_up_amount = amount_text)
        else:
            await message.answer(str(MESSAGES['min_payup']).format(amount = MIN_PAYUP_RUB))
    else:
        await message.answer("Пожалуйста, вводите только цифры. Попробуйте еще раз.")

async def top_up_by_card(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    amount = int(data.get('current_top_up_amount'))
    message = str(MESSAGES['top_up_by_card']).format(rub_amount=str(amount))
    await callback_query.message.answer(message)
    await state.set_state(BillStates.photo)
    await callback_query.answer()

async def bill_proceed(message: Message, bot: Bot, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        await message.answer(MESSAGES['bill_photo_success'])
        await bot.forward_message(chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id)
        await state.clear()
    else:
        await message.answer(MESSAGES['bill_photo_need'])

async def no_money(callback_query: CallbackQuery, bot: Bot):
    await bot.send_message(callback_query.from_user.id , MESSAGES['no_money'], reply_markup=popup_inline())
    await callback_query.answer()

async def buy_gems(message: Message):
    await message.answer(MESSAGES['buy_gems'], reply_markup=buy_gems_inline())

async def buy_pass(message: Message):
    await message.answer(MESSAGES['buy_pass'], reply_markup=buy_pass_inline())

async def pay_out(message: Message):
    await message.answer(MESSAGES['no_payout'], reply_markup=back_menu_reply())

async def support(message: Message):
    await message.answer(MESSAGES['support'], reply_markup=contact_support_inline())

async def support_send_message(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(MESSAGES['support_message'])
    await callback_query.answer()
    await state.set_state(Abstract.temp)

async def support_message_send_success(message: Message, state: FSMContext):
    await message.answer(MESSAGES['support_message_success'])
    await state.clear()

async def profile(message: Message):
    await message.answer(str(MESSAGES['profile']).format(tag=message.from_user.username, uid=message.from_user.id, id=random.randint(1000, 10000)))

async def rate(message: Message):
    await message.answer(str(MESSAGES['rate']).format(rub=round(float(1/float(RATE)), 2)))

async def news(message: Message):
    await message.answer(MESSAGES['news'], reply_markup=news_inline())

async def reviews(message: Message):
    await message.answer(MESSAGES['reviews'], reply_markup=reviews_inline())

async def calc(message: Message):
    await message.answer(MESSAGES['calc'], reply_markup=calc_reply())

async def calc_rbx_to_rub(message: Message, state: FSMContext):
    await message.answer(MESSAGES['calc1'])
    await state.set_state(Calc.calc1)

async def calc_rub_to_rbx(message: Message, state: FSMContext):
    await message.answer(MESSAGES['calc2'])
    await state.set_state(Calc.calc2)

async def calc_rbx_to_rub_answer(message: Message, state: FSMContext):
    amount_text = message.text.strip()
    if amount_text.isdigit():
        await message.answer(f"🍪 {amount_text} RBX = {round(int(amount_text)*1/RATE, 2)} RUB")
        await state.clear()
    else:
        await message.answer(MESSAGES['calc_no_symbole'])

async def calc_rub_to_rbx_answer(message: Message, state: FSMContext):
    amount_text = message.text.strip()
    if amount_text.isdigit():
        await message.answer(f"🍪 {amount_text} RUB = {int(int(amount_text)*RATE)} RBX")
        await state.clear()
    else:
        await message.answer(MESSAGES['calc_no_symbole'])

