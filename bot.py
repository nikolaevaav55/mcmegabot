import telebot
from telebot import types
import config_exmp
import emoji
import random

from parser import poem_generator


DRINK_LIST = [":beer_mug:", ":tumbler_glass:"]
MUSIC_LIST = ['minus_1.mp3', 'minus_2.mp3', 'minus_3.mp3']

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome_help(message):
    mess = f"""
    What's up, <b>{message.from_user.first_name}, ёёу</b>
    
    Брат, рэп течет в моей крови - 
    Только позови..
    
    Напиши мне <b>Брат, задай бит</b>
    И музыка зазвучит.
    
    Напиши мне <b>Брат, нужны новые строчки</b>
    Я верну тебе буквы и точки...
    """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Брат, задай бит')
    btn2 = types.KeyboardButton('Брат, нужны новые строчки')
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "Брат, задай бит":
        bot.send_message(message.chat.id, emoji.emojize(random.choice(DRINK_LIST)))
        audio = open(f'music/{random.choice(MUSIC_LIST)}', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == "Брат, нужны новые строчки":
        answer = "Введи первые две строчки" + emoji.emojize(":brain:")
        bot.send_message(message.chat.id, answer)
    else:
        try:
            mess = poem_generator(message.text)
            bot.send_message(message.chat.id, mess)
        except:
            bot.send_message(message.chat.id, "Братан, тебе хватит")


bot.polling(none_stop=True)




