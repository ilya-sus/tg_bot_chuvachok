import logging

import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from random import randrange


reply_keyboard = [['/start', '/help', '/close']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

good = ["Отлично", "Замечательно", "Великолепно", "Восхитительно", "Потрясающе", "Хорошо"]

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

    elif answer in bad:
        update.message.reply_text(
            f"Плохо. Чем ты занимаешься?")
    else:
        update.message.reply_text(
            f"Я не ожидал такого ответа. Чем ты занимаешься?")
    return 2


def second_response(update, context):
    update.message.reply_text("Прикольно, к сожалению я не знаю что тебе  ещё сказать, но я могу предложить "
                              "тебе поиграть во что то, хочешь?")
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


def rules_c(update, context):
    update.message.reply_text("В игре Быки и Коровы, я загадываю случайное число от 1000 до 9999,"
                              " у тебя 5 попыток угадать моё число. Каждый ход ты вводишь 4 значное число, если"
                              "ты угадываешь 1 цифру, я пишу 1 корова, если ты угадываешь и цифру и расположение,"
                              "я пишу 1 бык, если всё понял, пиши /play_cows")


def cows(update, context):
    update.message.reply_text("Привет, ты знаешь правила игры Быки и Коровы? Если нет пиши /rules_c , если готов пиши"
                              " /play_cows")


def play_cows(update, context):
    global number
    b = 0
    c = 0
    k = 5

    number = str(randrange(1000, 10000))

    update.message.reply_text("Введи своё число")
    update.message.reply_text(number)
    return 1


def first_try(update, context):
    number1 = update.message.text
    update.message.reply_text(number)
    update.message.reply_text(number1)

    b = 0
    c = 0

    for i in range(4):
        if number[i] == number1[i]:
            b += 1
        elif number1[i] in number:
            c += 1

    if number == number1:
        update.message.reply_text(f"Поздравляю, ты выйграл!")
    else:
        update.message.reply_text(f"В твоём числе - {b} быков и {c} коров")
        update.message.reply_text("Введи своё число")
        return 2


def second_try(update, context):
    number1 = update.message.text

    b = 0
    c = 0

    for i in range(4):
        if number[i] == number1[i]:
            b += 1
        elif number1[i] in number:
            c += 1

    if number == number1:
        update.message.reply_text(f"Поздравляю, ты выйграл!")
    else:
        update.message.reply_text(f"В твоём числе - {b} быков и {c} коров")
        update.message.reply_text("Введи своё число")
        return 3


def third_try(update, context):
    number1 = update.message.text

    b = 0
    c = 0

    for i in range(4):
        if number[i] == number1[i]:
            b += 1
        elif number1[i] in number:
            c += 1

    if number == number1:
        update.message.reply_text(f"Поздравляю, ты выйграл!")
    else:
        update.message.reply_text(f"В твоём числе - {b} быков и {c} коров")
        update.message.reply_text("Введи своё число")
        return 4


def forth_try(update, context):
    number1 = update.message.text

    b = 0
    c = 0

    for i in range(4):
        if number[i] == number1[i]:
            b += 1
        elif number1[i] in number:
            c += 1

    if number == number1:
        update.message.reply_text(f"Поздравляю, ты выйграл!")
    else:
        update.message.reply_text(f"В твоём числе - {b} быков и {c} коров")
        update.message.reply_text("Введи своё число")
        return 5


def fifth_try(update, context):
    number1 = update.message.text

    b = 0
    c = 0

    for i in range(4):
        if number[i] == number1[i]:
            b += 1
        elif number1[i] in number:
            c += 1

    if number == number1:
        update.message.reply_text(f"Поздравляю, ты выйграл!")
    else:
        update.message.reply_text(f"К сожалению, ты проиграл. :(")


def milion(update, context):
    update.message.reply_text("Привет, добро пожаловать в игру Кто готов стать милионером! Если ты не занешь правила,"
                              " пиши /rules_m . Если ты готов играть, пиши /play_milion")


def rules_m(update, context):
    update.message.reply_text("В игре Кто хочет стать миллионером я задам тебе 10 вопросов, если ты ответишь"
                              "на все вопросы правильно - ты выиграл. Ты можешь три раза "
                              "использовать подсказку 50 на 50. Если ты всё понял пиши /play_milion")


def play_milion(update, context):
    reply_keyboard = [['Полярный день', 'Полярная ночь', 'Что?', "Не знаю"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    update.message.reply_text("1.Как называют период времени,"
                              " когда солнце в северных широтах не опускается за горизонт?", reply_markup=markup)

    return 1


def first_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Великий утюг', 'Норильск', 'Великий Устюг', "Москва"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Полярный день":
        update.message.reply_text("2.Какой город объявлен официальной родиной"
                                  " русского Деда Мороза?", reply_markup=markup)
        return 2
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 1 вопросе.")


def second_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Не меняется', 'Не премножается', 'Не приходиться', "Не знаю"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Великий Устюг":
        update.message.reply_text("3.Как заканчивается русская поговорка: «Раз на раз…»?", reply_markup=markup)
        return 3
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 2 вопросе.")


def third_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Уровня моря', 'Остроты перца', 'Качество воды', "Качество воздуха"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Не приходиться":
        update.message.reply_text("4.Шкала Сковилла - это шкала оценки...?", reply_markup=markup)
        return 4
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 3 вопросе.")


def forth_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Берлин', 'Париж', 'Лондон', "Москва"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Остроты перца":
        update.message.reply_text("5.Назовите столицу Франции.", reply_markup=markup)
        return 5
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 4 вопросе.")


def fifth_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Британская', 'Сфинская', 'Аполлонская', "Мейнкун"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Париж":
        update.message.reply_text("6.Как называется порода бесшёрстных кошек?", reply_markup=markup)
        return 6
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 5 вопросе.")


def sixth_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Омск', 'Новомосковск', 'Ленинград', "Пермь"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Сфинская":
        update.message.reply_text("7.Какой город оказался в блокаде во время Великой"
                                  " Отечественной войны?", reply_markup=markup)
        return 7
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 6 вопросе.")


def seventh_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Рейсовки', 'Путёвки', 'Курсовка', "Маршрутка"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Ленинград":
        update.message.reply_text("8.Как называют микроавтобусы, совершающие поездки по"
                                  " определённым маршрутам?", reply_markup=markup)
        return 8
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 7 вопросе.")


def eighth_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Кинолог', 'Уфолог', 'Психолог', "Психиатр"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Маршрутка":
        update.message.reply_text("9.Какой специалист занимается изучением"
                                  " неопознанных летающих объектов?", reply_markup=markup)
        return 9
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 8 вопросе.")


def ninth_qui(update, context):
    answer = update.message.text

    reply_keyboard = [['Гафний', 'Кобальт', 'Бериллий', "Теллур"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Уфолог":
        update.message.reply_text("10.Какой химический элемент назван"
                                  " в честь злого подземного гнома?", reply_markup=markup)
        return 10
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 9 вопросе.")


def tenth_qui(update, context):
    answer = update.message.text
    reply_keyboard = [['/start', '/help', '/close']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    if answer == "Кобальт":
        update.message.reply_text("Поздравляю, ты выиграл миллион")
    else:
        update.message.reply_text("Неправильно, к сожалению ты проиграл на 10 вопросе.", reply_markup=markup)


def main():
    updater = Updater('5112138662:AAEkm1RjVMgKFMIwfutIlfr5SSSf44ZEcgk', use_context=True)
    bot = telegram.Bot(token='5112138662:AAEkm1RjVMgKFMIwfutIlfr5SSSf44ZEcgk')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("games", games))
    dp.add_handler(CommandHandler("rules_c", rules_c))
    dp.add_handler(CommandHandler("rules_m", rules_m))
    dp.add_handler(CommandHandler("cows", cows))
    dp.add_handler(CommandHandler("play_cows", play_cows))
    dp.add_handler(CommandHandler("milion", milion))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('dialog', dialog)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_response)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    play_mil_handler = ConversationHandler(
        entry_points=[CommandHandler('play_milion', play_milion)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_qui)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_qui)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_qui)],
            4: [MessageHandler(Filters.text & ~Filters.command, forth_qui)],
            5: [MessageHandler(Filters.text & ~Filters.command, fifth_qui)],
            6: [MessageHandler(Filters.text & ~Filters.command, sixth_qui)],
            7: [MessageHandler(Filters.text & ~Filters.command, seventh_qui)],
            8: [MessageHandler(Filters.text & ~Filters.command, eighth_qui)],
            9: [MessageHandler(Filters.text & ~Filters.command, ninth_qui)],
            10: [MessageHandler(Filters.text & ~Filters.command, tenth_qui)],
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    play_cows_handler = ConversationHandler(
        entry_points=[CommandHandler('play_cows', play_cows)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, first_try)],
            2: [MessageHandler(Filters.text & ~Filters.command, second_try)],
            3: [MessageHandler(Filters.text & ~Filters.command, third_try)],
            4: [MessageHandler(Filters.text & ~Filters.command, forth_try)],
            5: [MessageHandler(Filters.text & ~Filters.command, fifth_try)],
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(play_mil_handler)
    dp.add_handler(play_cows_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()