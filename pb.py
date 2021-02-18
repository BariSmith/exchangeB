import re
import requests
import json


#TOKEN = "1618715746:AAHkA_pzzG-nLIgIJuEOiSV-QQy52VEoK68"

URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
#'https://api.exchangeratesapi.io/latest?base=USD HTTP/1.1'



#loads exchange rate from link URL in dict format
def load_exchange():
    return json.loads(requests.get(URL).text)

#returns exchange rate of current exchange
def get_exchange(ccy_key):
    for exc in load_exchange():
        if ccy_key == ['ccy']:
            return exc
    return False

#returns a list of currencies according to the template
def get_exchanges(ccy_pattern):
    result = []
    ccy_pattern = re.escape(ccy_pattern) + '.*'
    for exc in load_exchange():
        if re.match(ccy_pattern, exc['ccy'], re.IGNORECASE) is not None:
            result.append(exc)
        return result


