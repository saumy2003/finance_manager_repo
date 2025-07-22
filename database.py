# # database.py

# import sqlite3

# DB_NAME = 'finance_manager.db'

# def get_connection():
#     return sqlite3.connect(DB_NAME)

# def initialize_database():
#     with get_connection() as conn:
#         cursor = conn.cursor()
        
#         # Users table
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT UNIQUE NOT NULL,
#                 password TEXT NOT NULL
#             )
#         ''')

#         # Transactions table
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS transactions (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER,
#                 type TEXT CHECK(type IN ('income', 'expense')),
#                 category TEXT,
#                 amount REAL,
#                 date TEXT,
#                 note TEXT,
#                 FOREIGN KEY(user_id) REFERENCES users(id)
#             )
#         ''')

#         # Budgets table
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS budgets (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER,
#                 category TEXT,
#                 amount REAL,
#                 month INTEGER,
#                 year INTEGER,
#                 FOREIGN KEY(user_id) REFERENCES users(id)
#             )
#         ''')

#         conn.commit()



import sqlite3

def get_db_connection():
    return sqlite3.connect("finance_manager.db")

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            category TEXT,
            type TEXT CHECK(type IN ('income', 'expense')),
            date TEXT,
            description TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            limit REAL,
            month INTEGER,
            year INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()
