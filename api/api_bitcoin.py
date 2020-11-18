import requests


def get_price_for_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)

    return response.json()["bpi"]["USD"]["rate_float"]


get_price_for_bitcoin()