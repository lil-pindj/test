import telebot
from telebot.types import Message
import s_taper
import create_db
from config import token
bot = telebot.TeleBot(token)
items = {}

@bot.message_handler(commands=['start'])
def start_bot(message:Message):
    clients = create_db.clients.read_all()
    for client in clients:
        if message.chat.id == client[1]:
            bot.send_message(message.chat.id, text = f'Здравствуйте, {client[0]}')
            return
    bot.send_message(message.chat.id, text='Введите свой ник')
    bot.register_next_step_handler(message, registration)
def registration(message):
    answer = message.text
    create_db.clients.write([answer, message.chat.id, items])
    bot.send_message(chat_id=message.chat.id, text='Пользователь добавлен')


bot.infinity_polling()
