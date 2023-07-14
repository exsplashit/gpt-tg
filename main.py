from telegram_bot.bot import TelegramBot
from gpt.chatgpt import ChatGPT
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram bot token
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def main():
    # Create instances of Telegram bot and ChatGPT
    bot = TelegramBot(TOKEN)
    gpt = ChatGPT(OPENAI_API_KEY)

    # Perform initial setup with ChatGPT
    initial_response = gpt.initial_setup()
    print("ChatGPT initial setup response:", initial_response)

    # Start the Telegram bot
    bot.start()

    # Collect and save user IDs of customers
    bot.collect_user_ids()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
