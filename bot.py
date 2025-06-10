
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from handlers.utkarsh import handle_utkarsh

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is up and running! Use /utkarsh <link> to start.")

def main():
    from config import BOT_TOKEN
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("utkarsh", handle_utkarsh))

    app.run_polling()

if __name__ == "__main__":
    main()
