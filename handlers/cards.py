from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states.trip_states import TripStates
from keyboards.card_keyboard import upload_photo_keyboard
from services.trip import get_next_card


router = Router()


@router.callback_query(
    lambda c: c.data == "open_frame"
)
async def open_frame(
    callback: CallbackQuery,
    state: FSMContext
):

    await callback.answer()


    data = await state.get_data()


    trip_id = data["trip_id"]
    destination_id = data["destination_id"]


    card = get_next_card(
        callback.from_user.id,
        trip_id,
        destination_id
    )


    if not card:
        await callback.message.answer(
            "✨ You opened all frames from this destination!"
        )
        return


    await state.set_state(
        TripStates.waiting_for_photo
    )

    await state.update_data(
        current_card_id=card["id"]
    )


    await callback.message.answer(
        f"🎴 {card['title']}\n\n"
        f"{card['description']}",
        reply_markup=upload_photo_keyboard(card["id"])
    )