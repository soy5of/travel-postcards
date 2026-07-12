from aiogram.utils.keyboard import InlineKeyboardBuilder


def open_frame_keyboard():

    builder = InlineKeyboardBuilder()

    builder.button(
        text="🎴 Open next frame",
        callback_data="open_frame"
    )

    return builder.as_markup()


def upload_photo_keyboard(card_id):

    builder = InlineKeyboardBuilder()

    builder.button(
        text="📸 Add memory",
        callback_data=f"upload:{card_id}"
    )

    return builder.as_markup()