import requests
import json
from config import currency


# Класс исключений
class ConvertionException(Exception):
    pass


# Класс обработок ошибок
class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        # если одинаковые валюты
        if quote == base:
            raise ConvertionException(f'Введены одинаковые валюты {base}')

        # валюта неизвестна
        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConvertionException(f'Валюта {quote} неизветна')

        # валюта неизвестна
        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConvertionException(f'Валюта {base} неизветна')

        # количество неправильное
        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise ConvertionException(f'Количество {amount} указано неверно')

        # fsym - Перевод из валюты
        # tsyms - В валюту
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        # значение переменной которую мы получаем
        total_base = json.loads(r.content)[currency[base]]*amount

        return round(total_base, 2)
