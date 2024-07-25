from extensions import Convert, ConvertException
import telebot
from config import TOKEN, keys


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands= ['start', 'help'])
def help_start(message):
    text = ("Чтобы начать перевод валют, укажите данные через пробел: \n<Название переводимой валюты> \
<В какую валюту нужно перевести> <Количество переводимой валюты> \nНапример: евро рубль 10  \
\nСписок доступных валют - /value")
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands= ['value'])
def value_(message):
    text = "Доступные валюты: \n" + "\n".join(keys.keys())
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types= ['text'])
def value_text(message):
    try:
        value = message.text.split(' ')

        if len(value) != 3:
            raise ConvertException("Не то количество параметров")
        quote, base, amount = value

        text = Convert.get_price(quote, base, amount)
        result = text * float(amount)

    except ConvertException as e:
        bot.send_message(message.chat.id, f"Ошибка пользователя! \n{e}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Не удалось обработать команду \n{e}")
    else:
        bot.send_message(message.chat.id, f'В {amount} {quote} -> {result} {base}')



bot.polling(none_stop=True)
