import telebot
import urllib.request as urllib2
TOKEN = '462090271:AAG0VDy8tX1ryHEO_wH2CBk3v-_O2B20v5o'
bot = telebot.TeleBot(TOKEN)

print(bot.get_updates())

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2} \n Текст - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Я покажу тебе твое расписание! Пришли мне сообщение вида "251", где 2 - номер курса, 5 - номер группы, а 1 - день недели (пн).')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я покажу тебе твое расписание. Для этого просто отправь мне сообщение со своим курсом, номером группы и днем недели! Показываю пример - "2 5 пн" или "2 5 1"  или "251".')
    bot.send_message(message.chat.id,  '(Для дней недели используй сокращения из двух букв: "пн", "вт", "ср", "чт", "пт", "сб", "вс" или номер дня недели)')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '251' or message.text == '2 5 1' or message.text == '2 5 пн' or message.text == '25пн':
        bot.send_message(message.chat.id, 'Еее, пар нет!')

    elif message.text == '252' or message.text == '2 5 2' or message.text == '2 5 вт' or message.text == '25вт':
        url = 'https://pp.userapi.com/c845221/v845221616/3665c/WyzksO1wSEc.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '253' or message.text == '2 5 3' or message.text == '2 5 ср' or message.text == '25ср':
        url = 'https://pp.userapi.com/c846122/v846122616/33d49/8pIpuhjGJVk.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '254' or message.text == '2 5 4' or message.text == '2 5 чт' or message.text == '25чт':
        url = 'https://pp.userapi.com/c845221/v845221616/3666a/yWEyv680sAs.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '255' or message.text == '2 5 5' or message.text == '2 5 пт' or message.text == '25пт':
        url = 'https://pp.userapi.com/c845221/v845221616/36671/6xrCamIheZI.jpg'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == '256' or message.text == '2 5 6' or message.text == '2 5 сб' or message.text == '25сб':
        bot.send_message(message.chat.id, 'Еее, пар нет!')

    elif message.text == '257' or message.text == '2 5 7' or message.text == '2 5 вс' or message.text == '25вс':
        bot.send_message(message.chat.id, 'Еее, пар нет!')

bot.polling()
