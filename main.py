import telebot
import webbrowser
from telebot import types

bot=telebot.TeleBot('not for you')
@bot.message_handler(commands=['hello!'])
def hello(messege):
    bot.send_message(messege.chat.id, '<b>Hello!(UwU)</b>', parse_mode='html')

@bot.message_handler(commands=['who_am_i'])
def who_am_i(messege):
    bot.send_message(messege.chat.id, f'you are kitty  ,{messege.from_user.first_name}')

@bot.message_handler(commands=['help'])
def help(messege):
    markup = types.InlineKeyboardMarkup()
    btn_about = types.InlineKeyboardButton('About', callback_data='about')
    btn_marks = types.InlineKeyboardButton('Marks', callback_data='marks')
    btn_time = types.InlineKeyboardButton('Time', callback_data='time')
    btn_meme = types.InlineKeyboardButton('MEME', callback_data='meme')
    markup.row(btn_marks,btn_time)
    markup.row(btn_about,btn_meme)
    bot.send_message(messege.chat.id, 'What i can:', reply_markup=markup)

@bot.message_handler(commands=['about'])
def about(messege):
    markup = types.InlineKeyboardMarkup()
    btn_we = types.InlineKeyboardButton('Our site', url='https://fictadvisor.com/')
    markup.row(btn_we)
    bot.send_message(messege.chat.id, 'I`m Pinki and i bot who can help with your student`s activity(UwU)',reply_markup=markup)



bot.polling(none_stop=True)
