import requests
EXCHANGE_API = "https://api.cbr.ru/old-api"
class ExchangeRateManager:
    @staticmethod
    def get_cbr_rates():
        response = requests.get("https://api.cbr.ru/currency/rates")
        return response.json()

    @staticmethod
    def get_coingecko_rates():
        response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
        return response.json()