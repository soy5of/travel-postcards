from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.trip_states import TripStates

from services.trip import get_trip_by_code
from services.trip import get_destinations
from keyboards.trip_keyboard import destinations_keyboard


router = Router()


@router.message(TripStates.waiting_for_trip_code)
async def process_trip_code(
    message: Message,
    state: FSMContext
):

    code = message.text.strip().upper()

    trip = get_trip_by_code(code)

    if not trip:
        await message.answer(
            "❌ I couldn't find this trip code."
        )
        return


    destinations = get_destinations(trip["id"])


    text = (
        f"✨ Trip found!\n\n"
        f"🌏 {trip['title']}\n\n"
        "Your destinations:\n"
    )


    for destination in destinations:
        text += f"\n📍 {destination['name']}"


    await state.update_data(
        trip_id=trip["id"]
    )    


    await state.set_state(
        TripStates.choosing_destination
    )


    await message.answer(
        text,
        reply_markup=destinations_keyboard(destinations)
    )