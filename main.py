from controller import *

@bot.message_handler(commands=['start'])
def welcome(message):
    initUser(user_id= message.chat.id, username= message.chat.username)
    answerMessage = f"Привет, {message.from_user.first_name}, это бот для общения со случайным человеком \n" \
                    f"чтобы узнать твой статус в чате, оправляй мне /status" \
                    f"Для того, чтобы узнать весь список команд и что они делают, отправляй /help"

    sti = open('sticers/hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, answerMessage)

@bot.message_handler(commands=['help'])
def help(message):
    answer = f"/status - узнать есть ли у тебя собеседник \n" \
           f"/next_partner - выбрать следующего партнера"
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['status'])
def status(message):
    result = getStatus(message.chat.id)
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['next_partner'])
def set_as_woman(message):
    nextPartner(message.chat.id)


@bot.message_handler(content_types=['text'])
def message_handler(message):
    partner_id = getPartnerId(message.chat.id)
    if partner_id != -1:
        bot.send_message(partner_id, message.text)
    else:
        bot.send_message(message.chat.id,
                        "У вас еще нет собеседника, введите /next_partner для поиска нового собеседника")

@bot.message_handler(content_types=['voice'])
def message_handler(message):
    partner_id = getPartnerId(message.chat.id)
    if partner_id != -1:
        bot.send_voice(partner_id, message.voice.file_id)
    else:
        bot.send_message(message.chat.id,
                        "У вас еще нет собеседника, введите /next_partner для поиска нового собеседника")

@bot.message_handler(content_types=['sticker'])
def message_handler(message):
    partner_id = getPartnerId(message.chat.id)
    print()
    if partner_id != -1:
        bot.send_sticker(partner_id, message.sticker.file_id)
    else:
        bot.send_message(message.chat.id,
                        "У вас еще нет собеседника, введите /next_partner для поиска нового собеседника")

@bot.message_handler(content_types=['photo'])
def message_handler(message):
    partner_id = getPartnerId(message.chat.id)
    if partner_id != -1:
        bot.send_photo(partner_id, message.photo[0].file_id)
    else:
        bot.send_message(message.chat.id,
                        "У вас еще нет собеседника, введите /next_partner для поиска нового собеседника")


if __name__ == '__main__':

    bot.polling(none_stop=True)