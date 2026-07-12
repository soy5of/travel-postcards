from aiogram import Router
from aiogram.types import Message

from states.trip_states import TripStates
from services.trip import get_trip_by_code


router = Router()

@router.message(TripStates.waiting_for_trip_code)
async def process_trip_code(message: Message):

    code = message.text.strip()

    trip = get_trip_by_code(code)

    if not trip:
        await message.answer(
            "❌ I couldn't find this trip code."
        )
        return


    await message.answer(
        f"✨ Trip found!\n\n"
        f"{trip['title']}"
    )