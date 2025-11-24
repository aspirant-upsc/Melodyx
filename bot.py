from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from handlers.start import start_handler
from handlers.callbacks import callback_router
from handlers.play import play_handler
from handlers.inline_message import generic_message
from handlers.profile import get_fancy_for_user
from system.database import init_db
from system.logger import get_logger
from config import TELEGRAM_BOT_TOKEN

logger = get_logger(__name__)

def main():
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError('TELEGRAM_BOT_TOKEN not set')
    init_db()
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start_handler))
    app.add_handler(CommandHandler('play', play_handler))
    app.add_handler(CallbackQueryHandler(callback_router))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generic_message))
    logger.info('Bot starting...')
    app.run_polling()

if __name__ == '__main__':
    main()
