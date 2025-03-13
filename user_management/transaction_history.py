import csv
from datetime import datetime

class TransactionHistory:
    """Экспорт истории транзакций в CSV."""
    
    def export_to_csv(self, transactions: list, filename: str) -> None:
        """Сохраняет транзакции в файл CSV.
        
        Args:
            transactions (list): Список транзакций.
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amount", "Currency"])
            for tx in transactions:
                writer.writerow([datetime.now(), tx["type"], tx["amount"], tx["currency"]])