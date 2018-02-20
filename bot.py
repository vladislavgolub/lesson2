from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

date = datetime.datetime.now()
date = date.strftime('%d.%m.%Y')


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', #Запись лога о работе бота
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():

    updater = Updater("548253987:AAFZTH-rmT7xQH6LQhUPYEd32-XvGWa9AwA") # Персональный токен
    
    def greet_user(bot, update):
        text = 'Напиши мне'
        print(text)
        update.message.reply_text(text)

    def talk_to_me(bot, update):
        user_text = update.message.text 
        print(user_text)
        update.message.reply_text(user_text)

   





    def planet_identication(bot, update):
        
        user_text = update.message.text
        user_text = user_text.lower()
        user_message = user_text.split(' ') 
#считаем, что название планеты отделяется от команды пробелом, тогда название планеты будет вторым элементом
# списка (элементом с номером 1) user_message


        if user_message[1] == 'mercury':
            user_text = ephem.Mercury(date)
            user_text = str(user_text)
            print(user_text)
            update.message.reply_text(user_text)

        elif user_message[1] == 'venus':
            user_text = ephem.Venus(date)
            user_text = str(user_text)
            print(user_text)
            update.message.reply_text(user_text)

        elif user_message[1] == 'earth':
            user_text = 'Earth is bad choice'
            print(user_text)
            update.message.reply_text(user_text)
 
        elif user_message[1] == 'mars':
            user_text = ephem.Mars(date)
            user_text = str(user_text)
            print(user_text)
            update.message.reply_text(user_text)

        elif user_message[1] == 'jupiter':
            user_text = ephem.Jupiter(date)
            user_text = str(user_text)
            print(user_text)
            update.message.reply_text(user_text)
 
        elif user_message[1] == 'saturn':
            user_text = ephem.Saturn(date)
            user_text = str(user_text)
            print(user_text)
            update.message.reply_text(user_text)

        elif user_message[1] == 'uranus':
            user_text = ephem.Uranus(date)
            user_text = str(user_text)
            print(user_text)
            update.message.reply_text(user_text)
 
        elif user_message[1] == 'neptune':
            user_text = ephem.Neptune(date)
            user_text = str(user_text)
            print(user_text)
            update.message.reply_text(user_text)

        elif user_message[1] == 'pluto':
            user_text = 'Pluto is not a planet anymore! :('
            print(user_text)
            update.message.reply_text(user_text)
 
        else:
            user_text = user_message[1] + ' is not a planet in solar system!'
            print(user_text)
            update.message.reply_text(user_text)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("planet", planet_identication)) #Вызов planet_identification командой planet
    dp.add_handler(CommandHandler("start", greet_user)) # Вызов greet_user командой start
    dp.add_handler(MessageHandler(Filters.text,talk_to_me)) #В случае получения текстового сообщения вызывает talk_to_me 
                                                            #(команда не считается текстом)


    updater.start_polling() # Подключение
    updater.idle()          # бота

main()