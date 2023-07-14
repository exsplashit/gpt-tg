from telegram_bot.customer import interactions
from telegram.ext import CallbackContext
import pytest

# Mock objects for testing


class MockUpdate:
    def __init__(self, text):
        self.message = MockMessage(text)


class MockMessage:
    def __init__(self, text):
        self.text = text


class MockBot:
    def __init__(self):
        self.sent_messages = []

    def send_message(self, chat_id, text):
        self.sent_messages.append((chat_id, text))


class MockContext:
    def __init__(self, bot_data):
        self.bot_data = bot_data

# Test handle_customer_message


def test_handle_customer_message():
    bot = MockBot()
    bot_data = {
        'chatgpt': MockGPT(),
        'telegram_bot': bot
    }
    context = MockContext(bot_data)
    update = MockUpdate('Customer message')
    handle_customer_message(update, context)
    assert len(bot.sent_messages) == 1
    # Add more assertions as needed

# Add more tests for customer interactions as needed
