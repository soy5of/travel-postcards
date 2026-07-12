import sqlite3


DB_PATH = "database/travel.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Users of the bot
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE NOT NULL,
        username TEXT
    )
    """)


    # Trips created by users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        owner_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(owner_id)
        REFERENCES users(id)
    )
    """)


    # Cities/places inside a trip
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS destinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trip_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        country TEXT,

        FOREIGN KEY(trip_id)
        REFERENCES trips(id)
    )
    """)


    # Collectible cards
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        trip_id INTEGER NOT NULL,
        destination_id INTEGER,

        category TEXT NOT NULL,
        position INTEGER,

        title TEXT NOT NULL,
        description TEXT NOT NULL,
        image TEXT,

        FOREIGN KEY(trip_id)
        REFERENCES trips(id),

        FOREIGN KEY(destination_id)
        REFERENCES destinations(id)
    )
    """)


    # Cards collected by users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS card_collection (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,
        card_id INTEGER NOT NULL,

        collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        UNIQUE(user_id, card_id),

        FOREIGN KEY(user_id)
        REFERENCES users(id),

        FOREIGN KEY(card_id)
        REFERENCES cards(id)
    )
    """)


    cursor.execute("""                 
    CREATE TABLE IF NOT EXISTS user_trip_state (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,
        trip_id INTEGER NOT NULL,

        current_destination_id INTEGER,

        FOREIGN KEY(user_id)
        REFERENCES users(id),

        FOREIGN KEY(trip_id)
        REFERENCES trips(id),

        FOREIGN KEY(current_destination_id)
        REFERENCES destinations(id),

        UNIQUE(user_id, trip_id)
    )
    """)
    

    conn.commit()
    conn.close()