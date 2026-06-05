from database.db import get_connection
from data.user_profiles import user_profiles


def get_user_profile(chat_id):

    conn = get_connection() 
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT language, mode FROM users WHERE chat_id = %s", 
        (chat_id,)
    )
    row = cursor.fetchone()
    
    cursor.close()
    conn.close()

    
    if row:
        return {"lang": row[0], "mode": row[1]}
    return None


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

    if chat_id not in user_profiles:
        user_profiles[chat_id] = {
            "lang": None,
            "mode": "general",
            "history": []
        }
    


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

    if chat_id not in user_profiles:
        user_profiles[chat_id] = {"history": []}
    user_profiles[chat_id]["lang"] = language



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
    
    if chat_id not in user_profiles:
        user_profiles[chat_id] = {"lang": "en", "history": []}
    user_profiles[chat_id]["mode"] = mode



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