# Интернет-магазин с онлайн-оплатой

## Описание проекта

Телеграм-бот на Python с использованием современного фреймворка [aiogram](https://docs.aiogram.dev/) 3.20.0. Проект построен с поддержкой роутеров, middleware, асинхронной работы с базой данных PostgreSQL через SQLAlchemy и разделением логики для пользователей и администраторов. Подходит для личного и группового применения.

---


### Возможности:

- Обработка личных и групповых чатов
- Разделение пользовательской и админ логики
- Поддержка middleware, FSM
- Асинхронная работа с БД через SQLAlchemy
- Настройка через .env
- Гибкая архитектура для масштабирования
- Просмотр каталога товаров с фотографиями и описаниями
- Поиск и фильтрация товаров по категориям
- Добавление товаров в корзину, изменение количества
- Оформление заказа с вводом контактных данных
- Поддержка онлайн-оплаты (банковские карты, электронные кошельки и др.)
- Админ-панель для управления товарами и заказами

## Технологии

- Backend: Python 3.13+
- [aiogram 3.x](https://docs.aiogram.dev)
- База данных: PostgreSQL (через SQLAlchemy – асинхронный режим)
- [asyncpg](https://github.com/MagicStack/asyncpg) (адаптер PostgreSQL)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- asyncio

## Как запустить проект

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kravchend/TelegramBot_Aiogram_Online-shop_project
   ```

2. Перейдите в директорию проекта и создайте виртуальное окружение:
   ```bash
   cd TelegramBot_Aiogram_Online-shop_project
   python -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4.Откройте браузер и перейдите по адресу https://kravchend.github.io/TelegramBot_Aiogram_Online-shop_project/

## Контакты

По вопросам пишите на почту: <kravchend@gmail.com>
