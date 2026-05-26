from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = 8955376091:AAHqtIJmdtxUkZmouMZSIWSybccA9iy7O88

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "45":
        await update.message.reply_text("🎬 45-kino shu yerga keyin ulanadi")
    else:
        await update.message.reply_text("❌ Kino topilmadi")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handler))

app.run_polling()
