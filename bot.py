from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
from handlers.start import router

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())