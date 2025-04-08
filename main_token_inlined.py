
import time
import telebot
import threading

# Токен вставлено прямо в код
TOKEN = '7391704797:AAFKSZ4tpkoCkdl0QpN7OdG3_EnHIlfC-P8'
CHAT_ID = None

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    bot.send_message(CHAT_ID, "Привіт! Бот запущено та сигнали будуть надсилатися сюди!")

def send_signal():
    while True:
        if CHAT_ID:
            signal = "BTCUSDT (M1): ВГОРУ\nRSI: 29.5 | EMA: нижче | Обʼєм: високий"
            bot.send_message(CHAT_ID, signal)
        time.sleep(60)

threading.Thread(target=send_signal).start()
bot.polling()
