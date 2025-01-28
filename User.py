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
    role: str = 'kassenwart'

    def deposit_money(self, amount: float, description: str):
        """Deposit money to the balance."""
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount, 'description': description})
        print(f"Deposited money: {amount} - {description}")

    def remove_money(self, amount: float, description: str):
        """Remove money from the balance."""
        if amount > self.balance:
            print("Insufficient funds to remove this amount.")
            return
        self.balance -= amount
        self.transactions.append({'type': 'removal', 'amount': amount, 'description': description})
        print(f"Removed money: {amount} - {description}")

    def transfer_money(self, amount: float, description: str):
        """Transfer money from the balance."""
        if amount > self.balance:
            print("Insufficient funds to transfer this amount.")
            return
        self.balance -= amount
        self.transactions.append({'type': 'transfer', 'amount': amount, 'description': description})
        print(f"Transferred money: {amount} - {description}")

class Referent_in_Finanzen(User):
    role: str = 'referent'

    def view_all_transactions(self):
        """View all transactions."""
        for transaction in self.transactions:
            print(f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}")

    def view_transaction_history(self):
        """View the transaction history."""
        history = f"Transaction History:\n"
        for transaction in self.transactions:
            history += f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}\n"
        return history
