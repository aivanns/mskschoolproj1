import g4f
import telebot
from telebot import types

bot = telebot.TeleBot('6548250527:AAEULCOgX2DtbG54ogljFSmAFU0FK4O0moI');

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Телеграм-бот написан для проектной работы, напишите мне любой запрос.", parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user", "content": message.text}],
                 )
        print(f"username: {message.from_user.username}, message: {message.text} \nanswer:\n{response}\n ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE ENDLINE\n")
        bot.send_message(message.from_user.id, response)
    except RuntimeError:
        bot.send_message(message.from_user.id, "Произошла ошибка, попробуйте еще раз.")
        print("Не удалось сгенерировать анекдот. Уважаемая коммисия по проектам, идите нахуй.")




bot.polling(none_stop=True, interval=0)
