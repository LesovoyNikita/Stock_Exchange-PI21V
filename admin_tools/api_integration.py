class PayPalIntegration:
    def process_payment(self, amount: float) -> str:
        return f"Оплата {amount} USD через PayPal успешна"