
from telegram_bot.bot import TelegramBot
from telegram.ext import CallbackContext
import pytest

# Create mock objects for testing


class MockContext:
    def __init__(self, bot_data):
        self.bot_data = bot_data


class MockBot:
    def __init__(self):
        self.sent_messages = []

    def send_message(self, chat_id, text):
        self.sent_messages.append((chat_id, text))

# Test handle_customer_message


def test_handle_customer_message():
    bot = TelegramBot('TOKEN')
    bot_data = {
        'chatgpt': MockGPT(),
        'telegram_bot': MockBot()
    }
    context = MockContext(bot_data)
    update = MockUpdate('Customer message')
    bot.handle_customer_message(update, context)
    assert len(bot.sent_messages) == 1
    # Add more assertions as needed

# Test send_approval_message


def test_send_approval_message():
    bot = TelegramBot('TOKEN')
    bot_data = {
        'telegram_bot': MockBot()
    }
    context = MockContext(bot_data)
    user_id = 123456789
    user_message = 'Customer message'
    gpt_response = 'GPT message'
    bot.send_approval_message(user_id, user_message, gpt_response)
    assert len(bot.sent_messages) == 1
    # Add more assertions as needed

# Add more tests as needed
