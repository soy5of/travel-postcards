from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext


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


    await callback.message.answer(
        f"🎴 {card['title']}\n\n"
        f"{card['description']}"
    )