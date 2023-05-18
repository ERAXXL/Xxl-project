import time
import logging
from aiogram import Bot, Dispatcher, executor, types

r=7

Token="5665743452:AAGf9hGRu1dDQoZo-tFxUTcuJi7qJwAEhgc"
bot = Bot(token=Token)
dp= Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	user_id = message.from_user.id 
	user_name= message.from_user.full_name
	user_full_name= message.from_user.from_name
	logging.info(f'{user_id} {user_full_name=} {time.asctime()}')
	await message.reply(f"Привет, {user_full_name}")

for i in range(7):
	time.sleep(2):
	await bot.send_message(user_id, r.format(user_full_name))

if __name__ == '__main__':
	executor.start_polling(dp)