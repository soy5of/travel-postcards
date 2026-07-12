from services.database import get_connection


def collect_card(user_id, card_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO card_collection
    (
        user_id,
        card_id
    )

    VALUES (?, ?)
    """,
    (
        user_id,
        card_id
    ))

    conn.commit()
    conn.close()