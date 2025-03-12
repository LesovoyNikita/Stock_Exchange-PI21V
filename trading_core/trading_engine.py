from typing import List, Dict

class TradingEngine:
    def __init__(self):
        self.orders: List[Dict] = []

    def place_limit_order(self, order_type: str, price: float, amount: float):
        self.orders.append({
            "type": order_type,
            "price": price,
            "amount": amount
        })