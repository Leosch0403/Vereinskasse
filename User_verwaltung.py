__author__ = 'Leonard Schmid'
import csv
from typing import Union
from Vereinskasse import Club_Accounts

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

    def __init__(self,  name: str, password: str):
        super().__init__(name, password)
        self.created_departments = {}

    def create_department(self, name, balance : Union[int, float]):
        name = name.lower()

        if name in Club_Accounts.lst_accounts:
            print(f"Die Abteilung {name} existiert schon.")
        else:
            new_account = Club_Accounts(name, balance)
            self.created_departments[name] = new_account
            print(f"Die Abteilung {name} wurde mit einem Anfangsbestand von {balance}€ erstellt.")
            return new_account

    def del_department(self, name):
        name = name.lower()

        if name in Club_Accounts.lst_accounts:
            name.__del__()
        else:
            print(f"Die Abteilung {name} existiert nicht.")

    def backup(self):
        bill = open('Rechnung.txt', 'w')
        bill.write(f"Der Endpreis ist {table.price}€. Sie saßen am Tisch {table.table_number}."
                   f"\n{table.get_order()}")

    def create_Kassenwart(self,name):
        pass


if __name__ == '__main__':
    admin = Administrator('Hans', 'p0815')
    tanzen = admin.create_department('Tanzen', 26)
    admin.create_department('FUßBALL', 126)
    tanzen.deposit_money(76.555)
    tanzen.get_information()
    print(Club_Accounts.lst_accounts)
    print(Club_Accounts.num_accounts)