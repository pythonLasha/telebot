import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    reg = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = reg.json()
    sell_price = response['btc_usd']['sell']
    print(f'{datetime.now().strftime("%Y_%m_%d %H:%M")}\nSell BTC price: {sell_price} ')


def tele_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'hello')
        'something was wrong...'

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                reg = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = reg.json()
                sell_price = response['btc_usd']['sell']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                )

            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'something went wrong...'
                )
        else:
            bot.send_message(message.chat.id, 'Chek the command..!' )


    bot.polling() # Проверка на поступление сообщений


if __name__ == '__main__':
    # get_data()
    tele_bot(token)