from aiogram import Router
from aiogram.filters  import CommandStart
from aiogram.types import Message
from services.database import add_user

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    add_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username
    )

    await message.answer(
        "✈️Welcome to Travel Postcards!\n\n"
        "Ready to collect memories?"
    )