import sqlite3
import os

def init_db():
    DB_FILE = os.path.join(os.path.dirname(__file__), "contacts.db")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        name TEXT,
        contact TEXT,
        goal TEXT,
        user_id INTEGER
    )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Базу даних contacts.db ініціалізовано!")
