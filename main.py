from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton
import asyncio
from config import TOKEN_KEY


async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Открыть веб страницу", web_app=WebAppInfo(url="https://kravchend.github.io/TelegramBot_Aiogram_Online-shop_project/"))]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Привет, {message.from_user.full_name}!",
                         reply_markup=markup)


async def main():
    bot = Bot(token=TOKEN_KEY)
    dp = Dispatcher()

    # Регистрируем функцию /start
    dp.message.register(start, Command('start'))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())