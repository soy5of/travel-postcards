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
    
    cities = cursor.fetchall()

    conn.close()

    if cities:
        return [
        {
            "id": city[0],
            "name": city[1]
        }
        for city in cities
        ]
    return None

    
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