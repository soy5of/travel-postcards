from aiogram.utils.keyboard import InlineKeyboardBuilder


def open_frame_keyboard():

    builder = InlineKeyboardBuilder()

    builder.button(
        text="🎴 Open next frame",
        callback_data="open_frame"
    )

    return builder.as_markup()