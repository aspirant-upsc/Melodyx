from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import OWNER_NAME
from handlers.profile import get_fancy_for_user

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = f"Welcome to MelodyX! Owner: {OWNER_NAME}. Use the buttons below." 
    kb = [
        [InlineKeyboardButton('Play ▶️', callback_data='play_menu'), InlineKeyboardButton('Learn 📚', callback_data='learn_menu')],
        [InlineKeyboardButton('Help ❓', callback_data='help_menu'), InlineKeyboardButton('Owner 👤', callback_data='owner_info')],
        [InlineKeyboardButton('Fancy Name ✨', callback_data='fancy_menu'), InlineKeyboardButton('Add me baby 💖', callback_data='add_me_baby')],
    ]
    fancy = get_fancy_for_user(user.id)
    if fancy:
        text += f"\nYour fancy name: {fancy}"
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb))
