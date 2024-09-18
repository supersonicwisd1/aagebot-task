import threading
from web.server import WebServer
from bot.bot import TelegramBot
from bot.db import Database

if __name__ == '__main__':
    db = Database()
    
    bot = TelegramBot(db)
    web_server = WebServer()

    # Create threads to run the Flask server and bot in parallel
    server_thread = threading.Thread(target=web_server.start)
    bot_thread = threading.Thread(target=bot.start)

    server_thread.start()
    bot_thread.start()

    server_thread.join()
    bot_thread.join()
