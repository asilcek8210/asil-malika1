import sqlite3

def init_db():
    conn = sqlite3.connect('wedding_hall.db')
    cursor = conn.cursor()
    
    # Foydalanuvchilar jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT
    )
    ''')
    
    # Band qilish (bron) jadvali
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        event_type TEXT,
        status TEXT DEFAULT 'pending'
    )
    ''')
    
    conn.commit()
    conn.close()

def add_user(user_id, username, full_name):
    conn = sqlite3.connect('wedding_hall.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (user_id, username, full_name) VALUES (?, ?, ?)', 
                   (user_id, username, full_name))
    conn.commit()
    conn.close()

def add_booking(user_id, date, event_type):
    conn = sqlite3.connect('wedding_hall.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bookings (user_id, date, event_type) VALUES (?, ?, ?)', 
                   (user_id, date, event_type))
    conn.commit()
    conn.close()
