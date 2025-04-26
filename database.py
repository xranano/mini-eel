from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def connect_to_db():
    try:
        conn = psycopg2.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn

    except Exception as e:
        print(f"Error: {e}")
        return None

