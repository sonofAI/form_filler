
import asyncio
from aiogram import Bot, Dispatcher
from handlers import register_handlers

# Укажите токен вашего бота
API_TOKEN = "8067065920:AAHGS3AZtUTVIpxQDuYk2hkFR9hF4dUS3mU"

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Регистрация хэндлеров
    register_handlers(dp)

    # Запуск диспетчера
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
