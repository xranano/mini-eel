from database import connect_to_db

def insert_data(data):
    conn = connect_to_db()
    if not conn:
        print("Connection unsuccessfull")
        return

    cursor = conn.cursor()
    insert_sql = """
        INSERT INTO public.characters(
        id, name, status, species, gender, image, url, created)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """


    for character in data:
        cursor.execute(insert_sql, (
                character["id"],
                character["name"],
                character["status"],
                character["species"],
                character["gender"],
                character["image"],
                character["url"],
                character["created"]
            ))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Inserted {len(data)} characters into the database.")

def insert_location(data):
    conn = connect_to_db()
    if not conn:
        print("Connection unsuccessfull")
        return

    cursor = conn.cursor()
    insert_sql = """INSERT INTO public.locations(
	id, name, type, dimension)
	VALUES (%s, %s, %s, %s);"""

    for location in data:
        cursor.execute(insert_sql, (
            location["id"],
            location["name"],
            location["type"],
            location["dimension"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Inserted {len(data)} locations into the database.")


def insert_episodes(data):
    conn = connect_to_db()
    if not conn:
        print("Connection unsuccessfull")
        return

    cursor = conn.cursor()
    insert_sql = """
    INSERT INTO public.episodes(
	id, name, air_date)
	VALUES (%s, %s, %s);
    """

    for episode in data:
        cursor.execute(insert_sql, (
            episode["id"],
            episode["name"],
            episode["air_date"]
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Inserted {len(data)} episodes into the database.")