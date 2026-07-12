from aiogram import Router
from aiogram.types import CallbackQuery

from services.trip import set_current_destination


router = Router()


@router.callback_query(
    lambda c: c.data.startswith("destination:")
)
async def choose_destination(
    callback: CallbackQuery
):

    destination_id = int(
        callback.data.split(":")[1]
    )


    await callback.answer()


    await callback.message.answer(
        f"✨ Destination selected!\n\n"
        f"ID: {destination_id}"
    )