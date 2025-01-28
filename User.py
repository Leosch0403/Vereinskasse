__author__ = 'Leonard Schmid'
import csv
from typing import Union
from Vereinskasse import Club_Accounts

class User:

    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._role = 'user'

    def change_password(self, old_password, new_password):

        if old_password == self._password:
            self._password = new_password
            print('Sie haben das Passwort erfolgreich geändert')
        else:
            print('Sie haben ein falsches Passwort eingegeben')


class Kassenwart(User):

    def __init__(self, name, password):
        super().__init__(name, password)
        self._role = 'kassenwart'
        self._balance = 0.0
        self._transactions = []

    def add_income(self, amount, description):
        """Add income to the balance."""
        self._balance += amount
        self._transactions.append({'type': 'income', 'amount': amount, 'description': description})
        print(f"Added income: {amount} - {description}")

    def add_expense(self, amount, description):
        """Add expense to the balance."""
        if amount > self._balance:
            print("Insufficient funds for this expense.")
            return
        self._balance -= amount
        self._transactions.append({'type': 'expense', 'amount': amount, 'description': description})
        print(f"Added expense: {amount} - {description}")

    def get_balance(self):
        """Return the current balance."""
        return self._balance

    def generate_report(self):
        """Generate a report of all transactions."""
        report = f"Current Balance: {self._balance}\nTransactions:\n"
        for transaction in self._transactions:
            report += f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}\n"
        return report

    def save_report(self):
        """Save the report to a CSV file."""
        with open('report.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Amount', 'Description'])
            for transaction in self._transactions:
                writer.writerow([transaction['type'], transaction['amount'], transaction['description']])

    def load_report(self):
        """Load the report from a CSV file."""
        with open('report.csv', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                self._transactions.append({'type': row[0], 'amount': float(row[1]), 'description': row[2]})
    
class Referent_Finanzen(User):
    
    def __init__(self):
        super().__init__(name, password)
        self.role = 'referent_finanzen'

    def generate_report(self): 
        """Generate a report of all transactions."""
        report = f"Current Balance: {self.balance}\nTransactions:\n"
        for transaction in self.transactions:
            report += f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}\n"
        return report

    def add_income(self, amount, description):
        """Add income to the balance."""
        self.balance += amount
        self.transactions.append({'type': 'income', 'amount': amount, 'description': description})
        print(f"Added income: {amount} - {description}")

    def add_expense(self, amount, description):
        """Add expense to the balance."""
        if amount > self.balance:
            print("Insufficient funds for this expense.")
            return
        self.balance -= amount
        self.transactions.append({'type': 'expense', 'amount': amount, 'description': description})
        print(f"Added expense: {amount} - {description}")

    def get_balance(self):
        """Return the current balance."""
        return self.balance
    
