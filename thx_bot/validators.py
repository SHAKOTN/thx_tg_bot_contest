from functools import wraps

from telegram import Update
from telegram.constants import CHAT_GROUP
from telegram.constants import CHAT_PRIVATE
from telegram.ext import CallbackContext

from thx_bot.constants import ADMIN_ROLES


NOT_ADMIN_TEXT = """
💬  You are not admin of the chat our group_id context is missing. 
Please go to the channel you want to setup and hit /setup there!
"""

NOT_PRIVATE_CHAT_TEXT = """
⛔️You can use this command only in a private chat with the bot for security reasons!
"""


def only_chat_admin(f):
    @wraps(f)
    def wrapper(update: Update, context: CallbackContext):
        bot = context.bot

        if update.effective_chat.type == CHAT_GROUP:
            chat_id = update.effective_chat.id
        else:
            chat_id = context.user_data.get('channel_id')

        if not chat_id:
            update.message.reply_text(NOT_ADMIN_TEXT)
            return

        chat_member_status = bot.get_chat_member(int(chat_id), update.effective_user.id).status
        if chat_member_status not in ADMIN_ROLES:
            update.message.reply_text(NOT_ADMIN_TEXT)
            return
        return f(update, context)
    return wrapper


def only_in_private_chat(f):
    @wraps(f)
    def wrapper(update: Update, context: CallbackContext):
        """
        Allow to setup bot only in a private channel.
        """
        bot = context.bot
        if not update.effective_chat.type == CHAT_PRIVATE:
            update.message.reply_text(NOT_PRIVATE_CHAT_TEXT)
            return
        return f(update, context)
    return wrapper
