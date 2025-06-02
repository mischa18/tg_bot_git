# bot.py

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start, unknown
import config

def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()

    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()