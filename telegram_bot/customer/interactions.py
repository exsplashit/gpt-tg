from telegram.ext import CallbackContext
from telegram_bot.bot import send_approval_message


def handle_customer_message(update, context: CallbackContext):
    user_id = update.effective_chat.id
    user_message = update.message.text

    # Generate a response using ChatGPT
    gpt_response = context.bot_data['chatgpt'].generate_response(user_message)

    # Send the message to the business customer support member for approval or editing
    send_approval_message(
        context.bot_data['telegram_bot'], user_id, user_message, gpt_response)
