class CurrencyManager:
    SUPPORTED_CURRENCIES = ["USD", "RUB", "CNY", "BTC", "ETH"]

    def __init__(self):
        self.currencies = self.SUPPORTED_CURRENCIES.copy()

    def add_currency(self, currency_code: str):
        if currency_code not in self.currencies:
            self.currencies.append(currency_code)

    def convert(self, amount: float, from_curr: str, to_curr: str) -> float:
        return amount * 80.0 