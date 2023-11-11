import telebot

bot=telebot.TeleBot('not for you')
@bot.message_handler(commands=['start','hello!'])
def hello(messege):
    bot.send_message(messege.chat.id, '<b>Hello!(UwU)</b>', parse_mode='html')

@bot.message_handler(commands=['best'])
def hello(messege):
    bot.send_message(messege.chat.id, f'IM-32 , (and your mom ,{messege.from_user.first_name}))))')



bot.polling(none_stop=True)
