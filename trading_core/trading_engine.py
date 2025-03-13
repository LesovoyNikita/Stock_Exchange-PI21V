from typing import List, Dict

class TradingEngine:
    """Обработка торговых ордеров."""
    
    def __init__(self):
        """Инициализирует пустой список ордеров."""
        self.orders: List[Dict] = []

    def place_limit_order(self, order_type: str, price: float, amount: float) -> None:
        """Добавляет лимитный ордер в стакан.
        
        Args:
            order_type (str): Тип ордера (BUY/SELL).
            price (float): Цена за единицу.
            amount (float): Объем актива.
        """
        self.orders.append({
            "type": order_type,
            "price": price,
            "amount": amount
        })