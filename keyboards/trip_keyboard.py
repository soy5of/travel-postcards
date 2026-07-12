from aiogram.utils.keyboard import InlineKeyboardBuilder


def destinations_keyboard(destinations):

    builder = InlineKeyboardBuilder()

    for destination in destinations:
        builder.button(
            text=destination["name"],
            callback_data=f"destination_{destination['id']}"
        )

    builder.adjust(2)

    return builder.as_markup()