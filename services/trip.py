from services.database import get_connection


def get_trip_by_code(code):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT id, title
    FROM trips
    WHERE code = ?
    """,
    (
        code,
    ))


    trip = cursor.fetchone()

    conn.close()


    if trip:
        return {
            "id": trip[0],
            "title": trip[1]
        }

    return None


def get_destinations(trip_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, name
    FROM destinations
    WHERE trip_id = ?
    ORDER BY id               
    """,
    (
        trip_id,
    ))
    
    destinations = cursor.fetchall()

    conn.close()

    if destinations:
        return [
        {
            "id": destination[0],
            "name": destination[1]
        }
        for destination in destinations
        ]

    
def set_current_destination(user_id, trip_id, destination_id):
        
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR 
    REPLACE INTO user_trip_state
    (
        user_id, 
        trip_id, 
        current_destination_id
    ) 
                   
    VALUES (?, ?, ?)
    """,
    (
        user_id, 
        trip_id, 
        destination_id
    ))

    conn.commit()
    conn.close()


def get_cards(trip_id, destination_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        id,
        category,
        title,
        description,
        image
    FROM cards
    WHERE trip_id = ?
    AND (
        destination_id = ?
        OR destination_id IS NULL
    )
    ORDER BY position
    """,
    (
        trip_id,
        destination_id
    ))

    cards = cursor.fetchall()

    conn.close()

    return [
        {
            "id": card[0],
            "category": card[1],
            "title": card[2],
            "description": card[3],
            "image": card[4]
        }
        for card in cards
    ]


def get_next_card(user_id, trip_id, destination_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT id
    FROM card_collection
    WHERE user_id = ?
    """,
    (
        user_id,
    ))

    collected_cards = [
        row[0]
        for row in cursor.fetchall()
    ]


    if collected_cards:
        placeholders = ",".join(
            "?" * len(collected_cards)
        )

        query = f"""
        SELECT 
            id,
            category,
            title,
            description,
            image
        FROM cards
        WHERE trip_id = ?
        AND destination_id = ?
        AND id NOT IN ({placeholders})
        ORDER BY position
        LIMIT 1
        """

        cursor.execute(
            query,
            (
                trip_id,
                destination_id,
                *collected_cards
            )
        )

    else:

        cursor.execute("""
        SELECT
            id,
            category,
            title,
            description,
            image
        FROM cards
        WHERE trip_id = ?
        AND destination_id = ?
        ORDER BY position
        LIMIT 1
        """,
        (
            trip_id,
            destination_id
        ))


    card = cursor.fetchone()

    conn.close()


    if not card:
        return None


    return {
        "id": card[0],
        "category": card[1],
        "title": card[2],
        "description": card[3],
        "image": card[4]
    }