from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from handlers.profile import set_fancy
from system.owner_api import fetch_owner_info
from config import FANCY_DEFAULT_PREFIX, FANCY_DEFAULT_SUFFIX

async def callback_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data
    user = update.effective_user
    if data == 'help_menu':
        await q.edit_message_text('Help:\n/start - Start\n/help - Help\n/play <query> - Queue\n/fancy - Fancy settings')
    elif data == 'owner_info':
        owner = fetch_owner_info()
        await q.edit_message_text(str(owner))
    elif data == 'fancy_menu':
        kb = [[InlineKeyboardButton('Auto fancy (default)', callback_data='make_fancy_auto')], [InlineKeyboardButton('Custom fancy', callback_data='make_fancy_custom')]]
        await q.edit_message_text('Choose fancy mode:', reply_markup=InlineKeyboardMarkup(kb))
    elif data == 'make_fancy_auto' or data == 'add_me_baby':
        name = user.first_name or 'User'
        fancy = f"{FANCY_DEFAULT_PREFIX}{name}{FANCY_DEFAULT_SUFFIX}"
        set_fancy(user.id, user.username or name, FANCY_DEFAULT_PREFIX, FANCY_DEFAULT_SUFFIX, fancy)
        await q.edit_message_text(f'Fancy name set: {fancy}')
    elif data == 'make_fancy_custom':
        await q.edit_message_text('Send me your desired prefix and suffix separated by a space, e.g. ☆ ☆')
        # set conversation state
        context.user_data['awaiting_fancy_custom'] = True
    else:
        await q.edit_message_text('Not implemented yet')
