from telegram_bot.business.interactions import handle_business_approval, send_approval_message
from telegram.ext import CallbackContext
import pytest

# Mock objects for testing


class MockUpdate:
    def __init__(self, data):
        self.callback_query = MockCallbackQuery(data)


class MockCallbackQuery:
    def __init__(self, data):
        self.data = data


class MockBot:
    def __init__(self):
        self.sent_messages = []

    def send_message(self, chat_id, text):
        self.sent_messages.append((chat_id, text))


class MockContext:
    def __init__(self, bot_data):
        self.bot_data = bot_data

# Test handle_business_approval


def test_handle_business_approval():
    bot = MockBot()
    bot_data = {
        'telegram_bot': bot
    }
    context = MockContext(bot_data)
    update = MockUpdate('approve')
    handle_business_approval(update, context)
    assert len(bot.sent_messages) == 1
    # Add more assertions as needed


def test_handle_business_approval_edit():
    bot = MockBot()
    bot_data = {
        'telegram_bot': bot
    }
    context = MockContext(bot_data)
    update = MockUpdate('edit')
    handle_business_approval(update, context)
    assert len(bot.sent_messages) == 1
    # Add more assertions as needed

# Test send_approval_message


def test_send_approval_message():
    bot = MockBot()
    bot_data = {
        'telegram_bot': bot
    }
    send_approval_message(bot, 123456789, 'Customer message', 'GPT message')
    assert len(bot.sent_messages) == 1
    # Add more assertions as needed

# Add more tests for business interactions as needed
