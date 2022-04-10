import logging

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from random import randrange
import time


reply_keyboard = [['/start', '/help', '/close']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

good = ["Отлично", "Замечательно", "Великолепно", "Восхитительно", "Потрясающе"]

normal = ["Нормально", "Как всегда", "Ничего нового"]

bad = ["Такое себе", "Такое", "Плохо", "Ужасно", "Отвратительно"]


def start(update, context):
    update.message.reply_text(
        "Привет! Я твой бот помощник, что бы посмотреть что я могу, введи команду /help!",
        reply_markup=markup
    )


def help(update, context):
    reply_keyboard = [['/dialog', '/games', '/close']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Со мной можно поговорить или поиграть, используй клавиатуру команд.", reply_markup=markup)


def dialog(update, context):
    update.message.reply_text(
        "Привет. Я могу поговорить с тобой.\n"
        "Ты можете прервать опрос, послав команду /stop.\n"
        "Как у тебя дела?")
    return 1


def first_response(update, context):
    answer = update.message.text

    if answer in good:
        update.message.reply_text(
            f"Это замечательно! Чем ты занимаешься?")

    elif answer in normal:
        update.message.reply_text(
            f"Хорошо. Чем ты занимаешься?")

    elif answer in good:
        update.message.reply_text(
            f"Плохо. Чем ты занимаешься?")
    else:
        update.message.reply_text(
            f"Я не ожидал такого ответа. Чем ты занимаешься?")
    return 2


def second_response(update, context):
    update.message.reply_text("Прикольно, к сожалению я не знаю что тебе  ещё сказать, но я могу предложить "
                              "тебе поиграть во чтото, хочешь?")
    return 3


def third_response(update, context):
    answer = update.message.text
    reply_keyboard = [['/games', '/close']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Да":
        update.message.reply_text("Отлично, используй команду /games", reply_markup=markup)
    elif answer == "Нет":
        update.message.reply_text("Ну ладно, всего доброго!", reply_markup=markup)
    else:
        update.message.reply_text("Буду считать что ты сказал да) пиши /games", reply_markup=markup)
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Ну ладно, всего доброго!")
    return ConversationHandler.END


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def games(update, context):
    update.message.reply_text("Я могу предложить тебе поиграть в Быков и Коров(/cows) или в Кто хочет стать милионером"
                              "(/milion)")


def rules(update, context):
    update.message.reply_text("В игре Быки и Коровы, я загадываю случайное число от 1000 до 9999,"
                              " у тебя 5 попыток угадать моё число. Каждый ход ты вводишь 4 значное число, если"
                              "ты угадываешь 1 цифру, я пишу 1 корова, если ты угадываешь и цифру и расположение,"
                              "я пишу 1 бык, если всё понял, пиши /play_cows")


def cows(update, context):
    update.message.reply_text("Привет, ты знаешь правила игры Быки и Коровы? Если нет пиши /rules , если готов пиши"
                              "/play_cows")


def main():
    updater = Updater('5112138662:AAEkm1RjVMgKFMIwfutIlfr5SSSf44ZEcgk', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("games", games))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("cows", cows))
    dp.add_handler(CommandHandler("play_cows", play_cows))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('dialog', dialog)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_response)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


def play_cows(update, context):
    b = 0
    c = 0
    k = 5

    updater = Updater('5112138662:AAEkm1RjVMgKFMIwfutIlfr5SSSf44ZEcgk', use_context=True)
    updater.start_polling()

    number = str(randrange(1000, 10000))
    number1 = 0

    while k != 0 or number != number1:
        update.message.reply_text("Введи своё число")
        update.message.reply_text(number)
        update.message.reply_text(k)
        update.message.reply_text(number1)
        time.sleep(10)

        number1 = update.message.text
        for i in range(4):
            if number[i] == number1[i]:
                b += 1
            elif number1[i] in number:
                c += 1
        update.message.reply_text(f"В твоём числе - {b} быков и {c} коров")
        k -= 1


if __name__ == '__main__':
    main()
