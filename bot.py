from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio

from handlers.cards import cards_router
from handlers.start import router as start_router
from handlers.trips import router as trip_router
from handlers.destinations import router as destinations_router
from services.database import init_db

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(trip_router)
dp.include_router(destinations_router)
dp.include_router(cards_router)

async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())