import json
import sqlite3


DB_PATH = "database/travel.db"


def get_connection():
    return sqlite3.connect(DB_PATH)



def load_trip_file():

    with open(
        "data/asia2026.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def create_user(cursor):

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (
        telegram_id,
        username
    )

    VALUES (?, ?)
    """,
    (
        111111111,
        "sofia"
    ))


    cursor.execute("""
    SELECT id
    FROM users
    WHERE telegram_id = ?
    """,
    (111111111,))


    return cursor.fetchone()[0]



def create_trip(cursor, data, user_id):

    cursor.execute("""
    SELECT id
    FROM trips
    WHERE code = ?
    """,
    (
        data["trip"]["code"],
    ))


    existing = cursor.fetchone()


    if existing:
        return existing[0]


    cursor.execute("""
    INSERT INTO trips
    (
        code,
        title,
        owner_id
    )

    VALUES (?, ?, ?)
    """,
    (
        data["trip"]["code"],
        data["trip"]["title"],
        user_id
    ))


    return cursor.lastrowid



def create_destination(cursor, trip_id, destination):

    cursor.execute("""
    INSERT INTO destinations
    (
        trip_id,
        name,
        country
    )

    VALUES (?, ?, ?)
    """,
    (
        trip_id,
        destination["name"],
        destination["country"]
    ))


    return cursor.lastrowid



def create_card(
        cursor,
        trip_id,
        destination_id,
        card
):

    cursor.execute("""
    INSERT INTO cards
    (
        trip_id,
        destination_id,
        category,
        position,
        title,
        description,
        image
    )

    VALUES (?, ?, ?, ?, ?, ?, ?)

    """,
    (
        trip_id,
        destination_id,
        card["category"],
        card["position"],
        card["title"],
        card["description"],
        card["image"]
    ))



def create_random_card(cursor, trip_id, card):

    cursor.execute("""
    INSERT INTO cards
    (
        trip_id,
        destination_id,
        category,
        position,
        title,
        description,
        image
    )

    VALUES (?, NULL, ?, ?, ?, ?, ?)

    """,
    (
        trip_id,
        card["category"],
        card["position"],
        card["title"],
        card["description"],
        card["image"]
    ))



def seed_trip():

    data = load_trip_file()

    conn = get_connection()
    cursor = conn.cursor()


    user_id = create_user(cursor)


    trip_id = create_trip(
        cursor,
        data,
        user_id
    )


    for destination in data["destinations"]:

        destination_id = create_destination(
            cursor,
            trip_id,
            destination
        )


        for card in destination["cards"]:

            create_card(
                cursor,
                trip_id,
                destination_id,
                card
            )



    for card in data["random_cards"]:

        create_random_card(
            cursor,
            trip_id,
            card
        )


    conn.commit()
    conn.close()


    print("✨ Trip created successfully!")



if __name__ == "__main__":
    seed_trip()