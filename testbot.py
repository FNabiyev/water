import json
import logging

import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2144079245:AAEFUL8t2z8en68qNPZOzbQ1JIsuFkn8QpA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Assalomu Alaykum {message.from_user.full_name}\nChat id : {message.from_user.id}\nUsername : {message.from_user.username}")


@dp.message_handler(commands=['register'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Ro'yxatdan o'tish uchun @FNabiyev ga murojaat qiling. Kanalimizga obuna bo'ling.")


@dp.message_handler(commands=['category'])
async def send_category(message: types.Message):
    r = requests.get('http://127.0.0.1:8000/api/category/')
    json_data = json.loads(r.text)
    text = ''
    for c in json_data:
        text +='category id ' + str(c['id']) + '\tcategory name ' + c['name'] + "\n"
    await message.reply(f"Bizda mavjud categoriyalar:\n{text}")


@dp.message_handler(commands=['brand'])
async def send_brand(message: types.Message):
    r = requests.get('http://127.0.0.1:8000/api/brand/')

    await message.reply(f"Bizda mavjud brandlar:\n{r.text}")


@dp.message_handler(commands=['products'])
async def send_products(message: types.Message):
    r = requests.get('http://127.0.0.1:8000/api/products/')
    json_data = json.loads(r.text)
    text = ''
    for c in json_data:
        text += '\nname :' + str(c['name']) + '\nprice' + str(c['price']) + '\ndokonda bor :' +str(c['count']) + "\n\n"
    await message.reply(f"Bizda mavjud productlar:\n{text}")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)