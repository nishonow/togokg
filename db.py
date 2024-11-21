import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id TEXT NOT NULL,
    name TEXT NOT NULL,
    username TEXT
)
''')


# add users

def add_user(telegram_id, name, username=None):
    cursor.execute('INSERT INTO users (telegram_id, name, username) VALUES (?, ?, ?)',
                   (telegram_id, name, username))
    conn.commit()

# check user

def user_exists(telegram_id):
    cursor.execute("SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,))
    return cursor.fetchone() is not None

# statistics

def count_users():
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    return result[0] if result else 0

def get_all_user_ids():
    cursor.execute("SELECT telegram_id FROM users")
    result = cursor.fetchall()
    return [row[0] for row in result] if result else []