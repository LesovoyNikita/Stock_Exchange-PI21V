class WalletManager:
    """Управление балансами кошельков."""
    
    def __init__(self):
        """Инициализирует пустой словарь балансов."""
        self.balances = {}

    def deposit(self, user_id: str, currency: str, amount: float) -> None:
        """Пополняет баланс кошелька.
        
        Args:
            user_id (str): Идентификатор пользователя.
            currency (str): Код валюты.
            amount (float): Сумма пополнения.
        """
        self.balances.setdefault(user_id, {}).update({currency: amount})