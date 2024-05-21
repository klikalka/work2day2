from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from datetime import datetime

TOKEN_API = '6657224400:AAHKm9R4uijLFIegHJh3tePq2LgUXTm0JnU'
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

keyboard1 = InlineKeyboardMarkup(row_width=1)
button1 = InlineKeyboardButton('переключиться на 2 клавиатуру', callback_data= 'go_to_2')
button3 = InlineKeyboardButton('отправь случайное число', callback_data= 'send_random')
keyboard1.add(button1, button3)

keyboard2 = InlineKeyboardMarkup(row_width=1)
button2 = InlineKeyboardButton('переключиться на 1 клавиатуру', callback_data= 'go_to_1')
button4 = InlineKeyboardButton('время', callback_data= 'time')
keyboard2.add(button2, button4)



@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('нажми на кнопку', reply_markup=keyboard1)

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('нажми на кнопку, чтобы вернуться на предыдущую клавиатуру', reply_markup=keyboard2)

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('нажми на кнопку, чтобы вернуться на предыдущую клавиатуру', reply_markup=keyboard1)


@dp.callback_query_handler(lambda c: c.data == 'send_random')
async def random_number(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'Случайное число: {random_number}')
random_number = random.randint(1, 100)

@dp.callback_query_handler(lambda c: c.data == 'time')
async def time(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'Сейчас: {time}')
time = datetime.now().strftime("%H:%M:%S")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
