__author__ = 'Leonard Schmid'


class Club_Accounts:

    num_accounts = 0

    def __init__(self, department : str, balance : int | float):
        Club_Accounts.num_accounts += 1
        self._department = department
        self.balance = round(balance, 2)
        self.transactions = []

    def get_information(self):

        return f"Der Kontostand der Abteilung {self._department} ist {self.balance}€"

    def deposit_money(self, amount : int | float):
        amount = round(amount, 2)
        if amount <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
        self.balance += amount
        print(f"{amount}€ wurde in das Konto der {self._department} Abteilung eingezahlt. "
              f"Neuer Kontostand: {self.balance}€")


    def remove_money(self, amount : int | float):
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
        if self._department in Club_Accounts.lst_accounts:
            Club_Accounts.lst_accounts.remove(self._department)