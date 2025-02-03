from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция для начала диалога
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я помогу вам найти авиабилеты. Откуда вы летите?")
    context.user_data["step"] = "origin"  # Устанавливаем первый шаг диалога

# Функция для обработки текстовых сообщений
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.strip()
    step = context.user_data.get("step")

    if step == "origin":
        # Сохраняем город отправления
        context.user_data["origin"] = user_message.capitalize()
        update.message.reply_text(f"Отлично! Вы летите из {user_message}. Куда вы направляетесь?")
        context.user_data["step"] = "destination"  # Переходим к следующему шагу

    elif step == "destination":
        # Сохраняем город назначения
        context.user_data["destination"] = user_message.capitalize()
        update.message.reply_text(f"Хорошо! Вы летите в {user_message}. Когда вы планируете вылететь? (Укажите дату в формате YYYY-MM-DD)")
        context.user_data["step"] = "date"  # Переходим к следующему шагу

    elif step == "date":
        # Сохраняем дату вылета
        context.user_data["date"] = user_message
        origin = context.user_data["origin"]
        destination = context.user_data["destination"]
        date = context.user_data["date"]

        # Выводим собранную информацию
        update.message.reply_text(
            f"Вы хотите найти билеты из {origin} в {destination} на {date}."
        )

        # Очищаем данные пользователя
        context.user_data.clear()

# Основная функция для запуска бота
def main():
    token = "Y7781444422:AAHo6srAWEMMj8t6PsaVo-vzj3AjVJKWZjY"  # Замените на ваш токен
    updater = Updater(token)

    # Добавляем обработчики команд и сообщений
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
