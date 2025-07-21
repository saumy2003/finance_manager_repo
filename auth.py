# auth.py

import hashlib
import getpass
from database import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter a new username: ")
    password = getpass.getpass("Enter a new password: ")

    hashed = hash_password(password)

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            conn.commit()
            print("✅ Registration successful!\n")
    except Exception as e:
        print("❌ Registration failed:", e)

def login_user():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashed = hash_password(password)

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, hashed))
        user = cursor.fetchone()
        
        if user:
            print("✅ Login successful!\n")
            return user[0]  # user_id
        else:
            print("❌ Invalid credentials.\n")
            return None
