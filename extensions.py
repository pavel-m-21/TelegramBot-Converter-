import json
import requests
from config import keys

class ConvertException(Exception):
    pass

class Convert(ConvertException):
    @staticmethod
    def get_price(quote, base, amount):

        if quote == base:
            raise ConvertException("Нельзя переводить одинаковые валюты")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertException(f"Неправильно ввели значение {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertException(f"Неправильно ввели значение {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException(f"Неправильно ввели значение {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        text = float(json.loads(r.content)[keys[base]])
        return text

