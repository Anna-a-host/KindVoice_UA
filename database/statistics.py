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
        FROM users
        ORDER BY joined_at DESC
    """)

    users = cursor.fetchall()

    print("\n" + "=" * 80)
    print("KINDVOICE USER STATISTICS")
    print("=" * 80)

    for user in users:

        print(f"""
User ID: {user[0]}
Language: {user[1]}
Mode: {user[2]}
Messages: {user[4]}
Joined: {user[3]}
{'-' * 80}
""")

    conn.close()


def print_total_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM users
    """)

    total = cursor.fetchone()[0]

    print(f"\nTOTAL USERS: {total}")

    conn.close()


def print_popular_modes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            mode,
            COUNT(*) as amount
        FROM users
        GROUP BY mode
        ORDER BY amount DESC
    """)

    rows = cursor.fetchall()

    print("\nMOST POPULAR MODES")
    print("-" * 40)

    for row in rows:

        print(f"{row[0]}: {row[1]}")

    conn.close()


def print_top_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            chat_id,
            message_count
        FROM users
        ORDER BY message_count DESC
        LIMIT 10
    """)

    users = cursor.fetchall()

    print("\nTOP USERS")
    print("-" * 40)

    for user in users:

        print(
            f"User {user[0]} -> {user[1]} messages"
        )

    conn.close()


def print_dashboard():

    conn = get_connection()
    cursor = conn.cursor()

    print("\n")
    print("=" * 80)
    print("KINDVOICEUA ANALYTICS DASHBOARD")
    print("=" * 80)

    cursor.execute("""
        SELECT COUNT(*)
        FROM users
    """)

    total_users = cursor.fetchone()[0]

    cursor.execute("""
        SELECT SUM(message_count)
        FROM users
    """)

    result = cursor.fetchone()
    total_messages = result[0] if result[0] else 0

    print(f"Total users: {total_users}")
    print(f"Total messages: {total_messages}")

    print("=" * 80)

    conn.close()