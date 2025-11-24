from telegram import Update
from telegram.ext import ContextTypes
from system.content_filter import contains_bad_word

async def generic_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if contains_bad_word(getattr(msg, 'text', '')):
        try:
            await msg.delete()
            return
        except:
            pass
    await msg.reply_text('Message received (stub)')
