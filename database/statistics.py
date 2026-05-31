from database.db import get_connection


def print_all_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            chat_id,
            language,
            mode,
            joined_at,
            message_count
        FROM Users
        ORDER BY joined_at DESC
    """)

    users = cursor.fetchall()

    print("\n" + "=" * 80)
    print("KINDVOICE USER STATISTICS")
    print("=" * 80)

    for user in users:

        print(
            f"""
User ID: {user.chat_id}
Language: {user.language}
Mode: {user.mode}
Messages: {user.message_count}
Joined: {user.joined_at}
{'-' * 80}
"""
        )

    conn.close()


def print_total_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM Users
    """)

    total = cursor.fetchone()[0]

    print("\nTOTAL USERS:", total)

    conn.close()


def print_popular_modes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            mode,
            COUNT(*) as amount
        FROM Users
        GROUP BY mode
        ORDER BY amount DESC
    """)

    rows = cursor.fetchall()

    print("\nMOST POPULAR MODES")

    for row in rows:

        print(
            f"{row.mode}: {row.amount}"
        )

    conn.close()



def print_top_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT TOP 10
            chat_id,
            message_count
        FROM Users
        ORDER BY message_count DESC
    """)

    users = cursor.fetchall()

    print("\nTOP USERS")

    for user in users:

        print(
            f"User {user.chat_id} -> {user.message_count} messages"
        )

    conn.close()


def print_dashboard():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n")
    print("=" * 80)
    print("KINDVOICEUA ANALYTICS DASHBOARD")
    print("=" * 80)

    cursor.execute("SELECT COUNT(*) FROM Users")
    total_users = cursor.fetchone()[0]

    cursor.execute("""
        SELECT SUM(message_count)
        FROM Users
    """)

    total_messages = cursor.fetchone()[0] or 0

    print(f"Total users: {total_users}")
    print(f"Total messages: {total_messages}")

    print("=" * 80)

    conn.close()