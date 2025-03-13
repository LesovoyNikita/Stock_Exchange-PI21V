class PayPalIntegration:
    """Интеграция с платежным шлюзом PayPal."""
    
    def process_payment(self, amount: float) -> str:
        """Обрабатывает платеж через PayPal.
        
        Args:
            amount (float): Сумма платежа.
            
        Returns:
            str: Статус платежа.
        """
        return f"Оплата {amount} USD через PayPal успешна"