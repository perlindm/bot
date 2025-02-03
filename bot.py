from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! 👋 Я ваш помощник для путешествий.\n"
        "Я могу помочь вам найти авиабилеты, отели и экскурсии.\n\n"
        "Чтобы начать, нажмите кнопку ниже или напишите мне, что вас интересует.",
        reply_markup={
            "keyboard": [[{"text": "Открыть Mini App", "web_app": {"url": "https://your-mini-app-url.com"}}]],
            "resize_keyboard": True,
            "one_time_keyboard": True,
        },
    )

# Функция для обработки текстовых сообщений
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()
    if "авиабилеты" in user_message:
        update.message.reply_text("Вот ссылка на поиск дешевых авиабилетов: [Skyscanner](https://www.skyscanner.com)", parse_mode="Markdown")
    elif "отели" in user_message:
        update.message.reply_text("Вот ссылка на бронирование отелей: [Booking.com](https://www.booking.com)", parse_mode="Markdown")
    elif "экскурсии" in user_message:
        update.message.reply_text("Вот ссылка на экскурсии: [GetYourGuide](https://www.getyourguide.com)", parse_mode="Markdown")
    else:
        update.message.reply_text("Я могу помочь с авиабилетами, отелями или экскурсиями. Просто спросите!")

# Основная функция для запуска бота
def main():
    # Вставьте свой API-токен здесь
    token = "YOUR_TELEGRAM_BOT_TOKEN"
    updater = Updater(token)

    # Добавляем обработчики команд
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()