from telegram import Update
from telegram.ext import CallbackContext


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "This is THX Bot helping dialog\n\n"
        "Avaiable commands: "
    )