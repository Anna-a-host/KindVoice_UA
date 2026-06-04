from database.db import get_connection


def add_user(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (chat_id)
    VALUES (%s)
    ON CONFLICT (chat_id) DO NOTHING
""", (chat_id,))

    conn.commit()
    conn.close()


def update_language(chat_id, language):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET language = %s
        WHERE chat_id = %s
    """, (language, chat_id))

    conn.commit()
    conn.close()


def update_mode(chat_id, mode):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET mode = %s
        WHERE chat_id = %s
    """, (mode, chat_id))

    conn.commit()
    conn.close()


def increase_message_count(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET message_count = message_count + 1
        WHERE chat_id = %s
    """, (chat_id,))

    conn.commit()
    conn.close()