from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.trip_states import TripStates

from services.photos import save_photo
from services.collection import collect_card
from services.users import get_user_by_telegram_id


router = Router()


@router.message(
    TripStates.waiting_for_photo
)
async def receive_photo(
    message: Message,
    state: FSMContext
):

    if not message.photo:
        await message.answer(
            "Please send a photo 📸"
        )
        return


    photo = message.photo[-1]

    file_id = photo.file_id


    data = await state.get_data()

    card_id = data["current_card_id"]


    user_id = get_user_by_telegram_id(
        message.from_user.id
    )


    save_photo(
        user_id,
        card_id,
        file_id
    )


    collect_card(
        user_id,
        card_id
    )


    await message.answer(
        "💌 Memory saved!\n\n"
        "Your frame has been collected ✨"
    )


    await state.clear()