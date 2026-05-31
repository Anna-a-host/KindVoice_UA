from database.db import get_connection


def add_user(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1
            FROM Users
            WHERE chat_id = ?
        )
        INSERT INTO Users(chat_id)
        VALUES (?)
    """, chat_id, chat_id)

    conn.commit()
    conn.close()


def update_language(chat_id, language):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Users
        SET language = ?
        WHERE chat_id = ?
    """, language, chat_id)

    conn.commit()
    conn.close()


def update_mode(chat_id, mode):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Users
        SET mode = ?
        WHERE chat_id = ?
    """, mode, chat_id)

    conn.commit()
    conn.close()


def increase_message_count(chat_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Users
        SET message_count = message_count + 1
        WHERE chat_id = ?
    """, chat_id)

    conn.commit()
    conn.close()