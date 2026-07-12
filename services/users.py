from services.database import get_connection



def get_or_create_user(
        telegram_id,
        username
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM users
        WHERE telegram_id = ?
        """,
        (
            telegram_id,
        )
    )

    user = cursor.fetchone()

    if user:
        conn.close()
        return user[0]
    

    cursor.execute("""
    INSERT INTO users
    (
        telegram_id,
        username
    )

    VALUES (?, ?)

    """,
    (
        telegram_id,
        username
    ))

    
    new_user_id = cursor.lastrowid

    conn.commit()
    conn.close()
    
    return new_user_id


def get_user_by_telegram_id(telegram_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id
    FROM users
    WHERE telegram_id = ?
    """,
    (
        telegram_id,
    ))

    user = cursor.fetchone()

    conn.close()

    if user:
        return user[0]

    return None