__author__ = 'Leonard Schmid'

from typing import Union

class Club_Accounts:

    num_accounts = 0
    lst_accounts = []

    def __init__(self, department : str, balance : Union[int, float]):
        Club_Accounts.num_accounts += 1
        self.department = department
        self.balance = round(balance, 2)
        Club_Accounts.lst_accounts.append(self)

    def __repr__(self):
        return self.department

    def get_information(self):

        print(f"Der Kontostand der Abteilung {self.department} ist {self.balance}€")

    def deposit_money(self, amount : Union[int, float]):
        amount = round(amount, 2)
        if amount <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
        self.balance += amount
        print(f"{amount}€ wurde in das Konto der {self.department} Abteilung eingezahlt. "
              f"Neuer Kontostand: {self.balance}€")


    def remove_money(self, amount : Union[int, float]):
        amount = round(amount, 2)
        if amount <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
        if amount > self.balance:
            raise ValueError(f"Der Betrag überschreitet den aktuellen Kontostand von {self.balance}.")
        self.balance -= amount
        print(f"{amount}€ wurde von dem Konto der {self.department} Abteilung abgebucht. "
              f"Neuer Kontostand: {self.balance}€")

    def __del__(self):
        """
        Deletes a created object and reduces the total number of objects
        """
        Club_Accounts.num_accounts -= 1
        if self.department in Club_Accounts.lst_accounts:
            Club_Accounts.lst_accounts.remove(self.department)