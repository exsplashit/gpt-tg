from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext
from telegram_bot.bot import BUSINESS_SUPPORT_MEMBER_CHAT_ID


def handle_business_approval(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.message.chat_id
    user_message = query.message.text

    if query.data == "approve":
        # Send the GPT response to the customer
        context.bot_data['telegram_bot'].send_gpt_response(
            user_id, user_message)
    elif query.data == "edit":
        # Handle the edit action, e.g., prompt the business customer support member to provide an edited response
        context.bot_data['telegram_bot'].prompt_edit_response(
            user_id, user_message)

    # Answer the callback query
    query.answer()


def send_approval_message(telegram_bot, user_id, user_message, gpt_response):
    # Create the message template
    message_template = f"{user_message}\n\nTo this, I'm going to answer:\n{gpt_response}\n\nDo you want to approve it or edit?"

    # Create inline keyboard buttons
    keyboard = [
        [InlineKeyboardButton("SEND", callback_data="approve")],
        [InlineKeyboardButton("EDIT", callback_data="edit")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message to the business customer support member
    telegram_bot.send_message(chat_id=BUSINESS_SUPPORT_MEMBER_CHAT_ID,
                              text=message_template, reply_markup=reply_markup)
