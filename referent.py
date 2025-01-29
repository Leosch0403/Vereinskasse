# kassenwart.py

class Kassenwart:
    def __init__(self):
        self.balance = 0.0
        self.expenses = []
        self.income = []

    def add_income(self, amount, description):
        """Add income to the balance."""
        self.income.append({'amount': amount, 'description': description})
        self.balance += amount
        print(f"Added income: {amount} - {description}")

    def add_expense(self, amount, description):
        """Add expense to the balance."""
        if amount > self.balance:
            print("Insufficient balance to add this expense.")
            return
        self.expenses.append({'amount': amount, 'description': description})
        self.balance -= amount
        print(f"Added expense: {amount} - {description}")

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def generate_report(self):
        """Generate a financial report."""
        report = {
            'balance': self.balance,
            'income': self.income,
            'expenses': self.expenses
        }
        return report

# Example usage
if __name__ == "__main__":
    kassenwart = Kassenwart()
    kassenwart.add_income(1000, "Membership Fees")
    kassenwart.add_expense(200, "Event Costs")
    print("Current Balance:", kassenwart.get_balance())
    print("Financial Report:", kassenwart.generate_report())