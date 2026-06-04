from database.db import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

        chat_id BIGINT PRIMARY KEY,

        language TEXT DEFAULT 'uk',

        mode TEXT DEFAULT 'general',

        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        message_count INTEGER DEFAULT 0
    
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")