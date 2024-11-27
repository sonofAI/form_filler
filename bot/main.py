import asyncio
from aiogram import Bot, Dispatcher
from handlers import register_handlers

from dotenv import load_dotenv
import os
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    register_handlers(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
