from flask import Flask
import sqlite3

class WebServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return "Please visit the Telegram bot to get your link."

        @self.app.route('/link/<uuid>', methods=['GET'])
        def show_user(uuid):
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT telegram_user_id FROM UserLink WHERE uuid=?", (uuid,))
            result = cursor.fetchone()
            conn.close()

            if result:
                return f"Telegram User ID: {result[0]}"
            else:
                return "Invalid link or UUID not found.", 404

    def start(self):
        self.app.run(host='0.0.0.0', port=5000)