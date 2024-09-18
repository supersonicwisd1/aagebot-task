# Flask and Telegram Bot Integration

This project demonstrates how to integrate a Flask web server with a Telegram bot using SQLite as the database. The bot generates unique UUIDs for users, which are stored in the database, and users can access their Telegram user ID by visiting a specific link.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or above installed on your local machine.
- `pip` for managing Python packages.
- A Telegram bot API key (you can create a bot by talking to [BotFather](https://core.telegram.org/bots#botfather) on Telegram).

## Installation

Follow these steps to install and set up the project:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/aagebot-task.git
   cd aagebot-task
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Telegram Bot Token**:
   - Obtain a bot token by talking to [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
   - Create a `.env` file in the project root and add your bot token:

   ```env
   API_KEY=your-telegram-api-key
   ```

## Deploying on Render

1. **Push your code to GitHub**:
   Ensure your repository is pushed to GitHub. Render will link to your GitHub repo for deployment.

2. **Create a new web service on Render**:
   - Go to [Render](https://render.com) and log in or sign up.
   - Click on “New” and select “Web Service”.
   - Connect your GitHub repository.
   - Choose your branch and set the build command to:

     ```bash
     pip install -r requirements.txt
     ```

   - Set the start command to:

     ```bash
     python main.py
     ```

   - Choose a region and deploy.

3. **Configure environment variables**:
   - In Render, go to your service settings.
   - Add the environment variable for your Telegram bot token:

     ```bash
     API_KEY=your-telegram-api-key
     ```

## How to Use the Bot

1. **Start a conversation with the bot**:
   Open Telegram and search for your bot by its username: `@UUIDTelegramBot`.

2. **Commands**:

   - `/start`: Start a conversation with the bot. Click on the start button.
   - `/create`: Generate a UUID and receive a unique link that points to the Flask web server.

3. **Access your link**:
   After generating a UUID using the `/create` command, you will receive a link in this format:

   ```
   https://aagebot-task.onrender.com/link/<uuid>
   ```

4. **Get Telegram User ID**:
    Use `Postman` or `curl` to get the user telegram ID

    - **Postman**
    - - Send a `GET` request to `https://aagebot-task.onrender.com/link/<uuid>`
    - - In the response, you will find the user telegram ID in the `user_id`

    - **curl**
    - - in the terminal run `curl https://aagebot-task.onrender.com/link/<uuid>`


**NOTE**
A `GET` to
```
https://aagebot-task.onrender.com/
```
   will generate this -> `Visit the link in your browser to see your Telegram user ID.`

## Project Structure

```bash
aagebot-task/
│
├── bot/
│   ├── __init__.py
│   ├── bot.py            # Telegram bot logic
│   ├── db.py       # SQLite database management
│
├── web/
│   ├── __init__.py
│   ├── server.py         # Flask web server logic
│
├── database.db           # SQLite database
├── main.py               # Entry point to start both bot and server
├── requirements.txt      # Python package dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
```

## Troubleshooting

If you encounter any issues:

- Ensure your environment variables are set up correctly in Render.
- Double-check that the SQLite database is created with the necessary tables.
- Verify that your Flask app is running by visiting the public URL provided by Render.

## Bot Username

The Telegram bot can be found at: **UUIDTelegramBot**.