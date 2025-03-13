class CurrencyManager:
    """Управление списком валют и конвертацией.
    
    Attributes:
        SUPPORTED_CURRENCIES (list): Базовый набор поддерживаемых валют.
    """
    
    SUPPORTED_CURRENCIES = ["USD", "RUB", "CNY", "BTC", "ETH"]

    def __init__(self):
        """Инициализирует менеджер с базовым набором валют."""
        self.currencies = self.SUPPORTED_CURRENCIES.copy()

    def add_currency(self, currency_code: str) -> None:
        """Добавляет новую валюту в список поддерживаемых.
        
        Args:
            currency_code (str): Код валюты (например, 'EUR').
        """
        if currency_code not in self.currencies:
            self.currencies.append(currency_code)

    def convert(self, amount: float, from_curr: str, to_curr: str) -> float:
        """Конвертирует сумму из одной валюты в другую.
        
        Args:
            amount (float): Сумма для конвертации.
            from_curr (str): Исходная валюта.
            to_curr (str): Целевая валюта.
            
        Returns:
            float: Результат конвертации.
        """
        return amount * 75.0


    