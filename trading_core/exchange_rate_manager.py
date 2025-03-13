import requests

class ExchangeRateManager:
    """Получение курсов валют из внешних API."""
    
    @staticmethod
    def get_cbr_rates() -> dict:
        """Запрашивает курсы валют ЦБ РФ.
        
        Returns:
            dict: Ответ API в формате JSON.
        """
        response = requests.get("https://api.cbr.ru/currency/rates")
        return response.json()

    @staticmethod
    def get_coingecko_rates() -> dict:
        """Запрашивает курсы криптовалют с CoinGecko.
        
        Returns:
            dict: Ответ API в формате JSON.
        """
        response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
        return response.json()