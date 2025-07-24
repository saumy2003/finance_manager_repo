import sqlite3
import hashlib
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

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()