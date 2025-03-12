class WalletManager:
    def __init__(self):
        self.balances = {}

    def deposit(self, user_id: str, currency: str, amount: float):
        self.balances.setdefault(user_id, {}).update({currency: amount})