from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from services.users import get_or_create_user
from states.trip_states import TripStates


router = Router()


@router.message(CommandStart())
async def start(
        message: Message,
        state: FSMContext
):

    get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username
    )


    await state.set_state(
        TripStates.waiting_for_trip_code
    )


    await message.answer(
        "✈️ Welcome to 22 Frames!\n\n"
        "Enter your trip code:"
    )