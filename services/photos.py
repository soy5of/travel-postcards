from services.database import get_connection


def save_photo(
    user_id,
    card_id,
    file_id,
    caption=None
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO photos
    (
        user_id,
        card_id,
        file_id,
        caption
    )

    VALUES (?, ?, ?, ?)
    """,
    (
        user_id,
        card_id,
        file_id,
        caption
    ))

    conn.commit()
    conn.close()