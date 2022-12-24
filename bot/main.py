from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests


API_TOKEN = "5634871729:AAHQJqg_clCweceY8mwkfZPHZyBlTj7NmFc"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! Я Ro1mus Bot, напиши /help, чтобы увидеть больше команд!")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(text="/help - помощь по командам\n/start - запустить работу бота\n/cat - отправить картинку с котом\n/buttons - отправить кнопки\n/random_cat - картинка с рандомным котом!")

@dp.message_handler(commands=['cat'])
async def send_gif(message: types.Message):
    await bot.send_animation(message.from_user.id,\
    "https://tenor.com/ru/view/animals-with-captions-dink-my-oiter-cat-drinking-water-animal-drinking-water-cat-eating-gif-25121865")

button = InlineKeyboardMarkup()
first_pic = InlineKeyboardButton(text="кот1", url="https://tenor.com/ru/view/funny-cats-gif-18764288")
second_pic = InlineKeyboardButton(text="кот2", url="https://tenor.com/ru/view/cat-cat-standing-cat-stare-stare-bruhcat-gif-22348277")
third_pic = InlineKeyboardButton(text="кот3", url="https://tenor.com/ru/view/cat-vaccum-cat-automatic-cat-in-car-cute-cat-cattitude-gif-17562882")
button.add(first_pic, second_pic, third_pic)

@dp.message_handler(commands=['buttons'])
async def send_buttons(message: types.Message):
	await bot.send_message(message.from_user.id, "Держи немного кнопок", reply_markup=button)
	
@dp.message_handler(commands=['random_cat'])
async def send_random_gif(message: types.Message):
	await bot.send_message(message.from_user.id, "Рандомный кот!")
	response = requests.get("https://aws.random.cat/meow")
	link = response.json()['file']
	await bot.send_photo(message.from_user.id, link)


@dp.message_handler()
async def handle_other_messages(message: types.Message):
	await bot.send_message(message.from_user.id, "Что-то не так с синтаксисом команд, напиши /help")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
