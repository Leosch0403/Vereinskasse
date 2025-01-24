__author__ = 'Leonard Schmid'
import csv
from typing import Union

class Club_Accounts:

    num_accounts = 0
    lst_accounts = []

    def __init__(self, department : str, balance : Union[int, float]):
        Club_Accounts.num_accounts += 1
        Club_Accounts.lst_accounts.append(department)
        self.department = department
        self.balance = round(balance, 2)

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


class User:

    def __init__(self, name, password):
        self._name = name
        self._password = password

    def change_password(self, old_password, new_password):

        if old_password == self._password:
            self._password = new_password
            print('Sie haben das Passwort erfolgreich geändert')
        else:
            raise ValueError('Sie haben ein falsches Passwort eingegeben')


class Kassenwart(User):

    def __init__(self):
        super().__init__(name, password)
        self.role = Kassenwart

class Referent_Finanzen(User):
    pass


class Administrator(User):

    def __init__(self):
        super().__init__(name, password)

    def backup(self):
        bill = open('Rechnung.txt', 'w')
        bill.write(f"Der Endpreis ist {table.price}€. Sie saßen am Tisch {table.table_number}."
                   f"\n{table.get_order()}")

    def create_Kassenwart(self,name):
        pass

    def create_department(self, name, balance : Union[int, float]):
        name = name.lower()

        if name in Club_Accounts.lst_accounts:
            print('Die Abteilung existiert schon')
        else:
            pass

    def del_department(self, name):
        name = name.lower()

        if name in Club_Accounts.lst_accounts:
            name.__del__()
        else:
            print(f"Die Abteilung {name} existiert nicht.")


if __name__ == '__main__':
    Schach = Club_Accounts('Schach', 100)
    Handball = Club_Accounts('Handball', 25)
    Fußball = Club_Accounts('Fußball', 500)
    Schach.remove_money(34.576)
    Handball.deposit_money(23.41)
    Handball.get_information()
    Schach.get_information()
    Fußball.__del__()
    print(Club_Accounts.lst_accounts)
    print(Club_Accounts.num_accounts)