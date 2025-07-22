# import sqlite3

# DB_NAME = "finance_manager.db"

# def create_user_table():
#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def register_user():
#     username = input("Enter a new username: ").strip()
#     password = input("Enter a new password: ").strip()

#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()

#     try:
#         c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#         conn.commit()
#         print("✅ Registration successful!\n")
#     except sqlite3.IntegrityError:
#         print("❌ Username already exists. Please choose a different one.\n")
#     finally:
#         conn.close()

# def login_user():
#     username = input("Username: ").strip()
#     password = input("Password: ").strip()

#     conn = sqlite3.connect(DB_NAME)
#     c = conn.cursor()
#     c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
#     result = c.fetchone()
#     conn.close()

#     if result:
#         print("✅ Login successful!\n")
#         return result[0]  # Return user_id
#     else:
#         print("❌ Invalid credentials.\n")
#         return None




import sqlite3
from database import get_db_connection

def register_user():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ Registration successful!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists.")
    conn.close()

def login_user():
    username = input("Username: ")
    password = input("Password: ")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()
    conn.close()

    if user:
        print("✅ Login successful!")
        return user[0]
    else:
        print("❌ Invalid credentials.")
        return None
