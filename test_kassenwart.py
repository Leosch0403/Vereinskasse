# kassenwart.py

class Kassenwart:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0

    def add_transaction(self, amount, description):
        """Add a transaction to the club's finances."""
        self.transactions.append({'amount': amount, 'description': description})
        self.balance += amount
        print(f"Transaction added: {description} of amount {amount}. New balance: {self.balance}")

    def remove_transaction(self, index):
        """Remove a transaction by index."""
        if 0 <= index < len(self.transactions):
            transaction = self.transactions.pop(index)
            self.balance -= transaction['amount']
            print(f"Transaction removed: {transaction['description']}. New balance: {self.balance}")
        else:
            print("Invalid transaction index.")

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def get_transactions(self):
        """Return a list of all transactions."""
        return self.transactions

    def generate_report(self):
        """Generate a financial report."""
        report = f"Current Balance: {self.balance}\nTransactions:\n"
        for i, transaction in enumerate(self.transactions):
            report += f"{i}: {transaction['description']} - {transaction['amount']}\n"
        return report