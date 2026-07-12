from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from services.trip import set_current_destination
from keyboards.card_keyboard import open_frame_keyboard
from services.users import get_user_by_telegram_id


router = Router()


@router.callback_query(
    lambda c: c.data.startswith("destination:")
)
async def choose_destination(
    callback: CallbackQuery,
    state: FSMContext
):

    destination_id = int(
    callback.data.split(":")[1]
    )


    await state.update_data(
    destination_id=destination_id
    )


    data = await state.get_data()

    trip_id = data["trip_id"]

    user_id = get_user_by_telegram_id(
    callback.from_user.id
    )
    
    set_current_destination(
        user_id=user_id,
        trip_id=trip_id,
        destination_id=destination_id
    )


    await callback.message.answer(
    "✨ Destination selected!\n\n"
    "Ready for your next memory?",
    reply_markup=open_frame_keyboard()
    )