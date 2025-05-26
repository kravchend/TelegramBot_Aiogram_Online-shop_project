from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import json
import asyncio
from config import TOKEN_KEY


async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🚀 Открыть веб страницу",
                    web_app=WebAppInfo(url="https://kravchend.github.io/TelegramBot_Aiogram_Online-shop_project/")
                )
            ]
        ],
        resize_keyboard=True  # чтобы кнопка подходила под размер экрана
    )
    await message.answer(f"Привет, {message.from_user.full_name}!",
                         reply_markup=markup)


async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f"Name: {res['name']}. Email: {res['email']}. Phone: {res['phone']}.")


async def main():
    bot = Bot(token=TOKEN_KEY)
    dp = Dispatcher()
    # Регистрируем функцию /start
    dp.message.register(start, Command('start'))
    # Регистрируем функцию web_app
    dp.message.register(web_app, lambda m: m.web_app_data is not None)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
