__author__ = 'Leonard Schmid'
from Vereinskasse import Club_Accounts
from typing import Union

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

    def __init__(self, name, password, account: Club_Accounts):
        super().__init__(name, password)
        self.account = account

    def deposit_money(self, amount: float, description: str):
        self.account.deposit_money(amount)
        print(f"Deposited money: {amount} - {description}")

    def remove_money(self, amount: float, description: str):
        self.account.remove_money(amount)
        print(f"Removed money: {amount} - {description}")

class Referent_in_Finanzen(User):
    role: str = 'referent'

    def __init__(self, name, password, account: Club_Accounts):
        super().__init__(name, password)
        self.account = account

    def view_all_transactions(self):
        for transaction in self.account.transactions:
            print(f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}")

    def view_transaction_history(self):
        history = f"Transaction History:\n"
        for transaction in self.account.transactions:
            history += f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}\n"
        return history

class Administrator(User):
    def __init__(self, name: str, password: str):
        super().__init__(name, password)
        self.role = 'admin'
        self.created_departments = {}
        self.lst_of_departments = []

    def create_department(self, name, balance: Union[int, float]):
        finder = False
        name = name.lower()

    def del_department(self, name):
        for obj in self.lst_of_departments:
            if obj._department == name:
                self.lst_of_departments.remove(obj)
                self.lst_of_departments.remove(obj)

    def backup(self, table):
        bill = open('Rechnung.txt', 'w')
        bill.write(f"Der Endpreis ist {table.price}€. Sie saßen am Tisch {table.table_number}."
                   f"\n{table.get_order()}")

    def create_User(self, name):
        pass

    def del_user(self, name):
        pass
