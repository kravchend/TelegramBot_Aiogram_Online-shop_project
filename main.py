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

async def info(message: types.Message):
    await message.answer(
        "Это бот, который будет отвечать на ваши запросы",
    )

async def main():
    bot = Bot(token=TOKEN_KEY)
    dp = Dispatcher()

    # Регистрируем хендлер с помощью метода message
    dp.message.register(start, Command('start'))
    dp.message.register(info, Command("info"))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())