import csv
from datetime import datetime

class TransactionHistory:
    def export_to_csv(self, transactions: list, filename: str):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Amount", "Currency"])
            for tx in transactions:
                writer.writerow([datetime.now(), tx["type"], tx["amount"], tx["currency"]])