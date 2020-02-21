"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from ephem import *
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet_talk(bot, update):
    # Вот здесь что-то
    
    pl = update.message.text.split()
    planet = pl[1]
    #
    
    time = date.today()
    if planet == 'Venus':
      stars=constellation(Venus(time))
    if planet == 'Mars':
      stars=constellation(Mars(time))
    if planet == 'Jupiter':
      stars=constellation(Jupiter(time))
    if planet == 'Saturn':
      stars=constellation(Saturn(time))
    if planet == 'Uranus':
      stars=constellation(Uranus(time))
    if planet == 'Neptune':
      stars=constellation(Neptune(time))
    if planet == 'Pluto':
      stars=constellation(Pluto(time))
    if planet == 'Sun':
      stars=constellation(Sun(time))
    if planet == 'Moon':
      stars=constellation(Moon(time))
    if planet == 'Mercury':
      stars=constellation(Mercury(time))
    
    update.message.reply_text(stars[1])

def main():
    mybot = Updater("1007684944:AAHyQ5_tF2_qer8lWGyWytHILaAOf5uYT_8", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_talk))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
