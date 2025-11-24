from telegram import Update
from telegram.ext import ContextTypes
from music.vc_player import vc_player

async def play_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text('Usage: /play <song name or url>')
        return
    track = ' '.join(args)
    vc_player.enqueue({'title': track, 'duration': 5})
    await update.message.reply_text(f'Queued (stub): {track}')
    # start player loop if not running
    import asyncio
    if not vc_player.playing:
        asyncio.create_task(vc_player.play_loop())
