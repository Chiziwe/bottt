from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
import telepotpip
import telebot
import urllib.request as urllib2
from telepot.loop import MessageLoop


TOKEN = '462090271:AAG0VDy8tX1ryHEO_wH2CBk3v-_O2B20v5o'
bot = telepot.Bot(TOKEN)
bot1 = telebot.TeleBot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
#Обработка команд

@bot1.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '251' or message.text == '2 5 1' or message.text == '2 5 пн' or message.text == '25пн':
        bot1.send_message(message.chat.id, 'Еее, пар нет!')

    elif message.text == '252' or message.text == '2 5 2' or message.text == '2 5 вт' or message.text == '25вт':
        url = 'https://pp.userapi.com/c845221/v845221616/3665c/WyzksO1wSEc.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot1.send_chat_action(message.from_user.id, 'upload_photo')
        bot1.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '253' or message.text == '2 5 3' or message.text == '2 5 ср' or message.text == '25ср':
        url = 'https://pp.userapi.com/c846122/v846122616/33d49/8pIpuhjGJVk.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot1.send_chat_action(message.from_user.id, 'upload_photo')
        bot1.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '254' or message.text == '2 5 4' or message.text == '2 5 чт' or message.text == '25чт':
        url = 'https://pp.userapi.com/c845221/v845221616/3666a/yWEyv680sAs.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot1.send_chat_action(message.from_user.id, 'upload_photo')
        bot1.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '255' or message.text == '2 5 5' or message.text == '2 5 пт' or message.text == '25пт':
        url = 'https://pp.userapi.com/c845221/v845221616/36671/6xrCamIheZI.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot1.send_chat_action(message.from_user.id, 'upload_photo')
        bot1.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '256' or message.text == '2 5 6' or message.text == '2 5 сб' or message.text == '25сб':
        bot1.send_message(message.chat.id, 'Еее, пар нет!')

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я покажу тебе расписание! Для подробной информации напиши /help')

def textMessage(bot, update):
    request = apiai.ApiAI('e24bda8a3aeb4e6ba11d0b6e1159d0ec').text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot' #ID сессии диалога
    request.query = update.message.text #запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] #вытаскиваем ответ из JSON
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я вас не понимаю!')

# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C

updater.idle()
bot1.polling()