def collect_card(
        user_id,
        card_id
):

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


    collected = cursor.rowcount > 0


    conn.commit()
    conn.close()


    return collected