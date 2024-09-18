import sqlite3

class Database:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS UserLink (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_user_id TEXT NOT NULL,
                uuid TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def insert_user_link(self, telegram_user_id, uuid):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO UserLink (telegram_user_id, uuid) VALUES (?, ?)', (telegram_user_id, uuid))
        conn.commit()
        conn.close()

    def get_user_id_by_uuid(self, uuid):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT telegram_user_id FROM UserLink WHERE uuid=?', (uuid,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
