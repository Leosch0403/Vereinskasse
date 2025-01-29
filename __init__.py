# kassenwart.py

class Kassenwart:
    def __init__(self):
        self.transactions = []  # List to store transactions
        self.balance = 0.0      # Current balance

    def add_transaction(self, amount, description):
        """Add a transaction to the club's finances."""
        self.transactions.append({'amount': amount, 'description': description})
        self.balance += amount
        print(f"Transaction added: {description} of amount {amount}. New balance: {self.balance}")

    def view_balance(self):
        """Return the current balance."""
        return self.balance

    def generate_report(self):
        """Generate a report of all transactions."""
        report = "Transaction Report:\n"
        for transaction in self.transactions:
            report += f"{transaction['description']}: {transaction['amount']}\n"
        report += f"Current Balance: {self.balance}"
        return report

# Example usage
if __name__ == "__main__":
    kassenwart = Kassenwart()
    kassenwart.add_transaction(100.0, "Membership Fees")
    kassenwart.add_transaction(-20.0, "Event Expenses")
    print(kassenwart.view_balance())
    print(kassenwart.generate_report())