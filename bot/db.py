import sqlite3

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            status TEXT DEFAULT 'not_filled' -- 'not_filled' or 'filled'
        )
    """)
    conn.commit()
    conn.close()

def add_user(name, surname, email, phone, birth_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (name, surname, email, phone, birth_date)
        VALUES (?, ?, ?, ?, ?)
    """, (name, surname, email, phone, birth_date))
    conn.commit()
    conn.close()

def get_next_user():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE status = 'not_filled' LIMIT 1
    """)
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_status(user_id, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users SET status = ? WHERE id = ?
    """, (status, user_id))
    conn.commit()
    conn.close()
