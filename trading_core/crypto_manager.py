import os

class CryptoManager:
    """Генерация криптовалютных кошельков."""
    
    @staticmethod
    def generate_wallet() -> str:
        """Создает случайный адрес кошелька.
        
        Returns:
            str: Адрес кошелька в формате '0x...'.
        """
        return "0x" + os.urandom(20).hex()