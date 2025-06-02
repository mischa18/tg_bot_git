# handlers.py

from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_CHAT_ID

# Заглушки данных
KNOWN_USERS = {
    "@masha": {"name": "Мария Иванова", "role": "student", "group": "Группа 1"},
    "@petr": {"name": "Петр Петров", "role": "teacher", "group": None}
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_nick = update.effective_user.username

    if not user_nick or f"@{user_nick}" not in KNOWN_USERS:
        await update.message.reply_text("Я тебя не знаю.")
        return

    user_data = KNOWN_USERS[f"@{user_nick}"]
    role = "студент" if user_data["role"] == "student" else "преподаватель"
    group_info = f", группа {user_data['group']}" if user_data["group"] else ""

    await update.message.reply_text(f"Привет! Тебя зовут {user_data['name']}, ты {role}{group_info}.")

    # Имитация начала пары (для препода)
    if user_data["role"] == "teacher":
        await update.message.reply_text("🔔 Началась пара. Отметьте отсутствующих:\nВыберите группу: Группа 1 / Группа 2")

    # Имитация окончания пары (для студента)
    elif user_data["role"] == "student":
        await update.message.reply_text("🕒 Пара закончилась. Оцените занятие по шкале от 1 до 5 и напишите комментарий.")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Неизвестная команда.")