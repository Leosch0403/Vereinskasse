__author__ = 'Leonard Schmid'
import csv
from Vereinskasse import Club_Accounts

# Lists that contain the created objects
lst_of_Accounts = []
lst_of_departments = []

class User:

    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._role = 'user'

    def change_password(self, old_password, new_password):

        if old_password == self._password:
            self._password = new_password
            return 'Sie haben das Passwort erfolgreich geändert'
        else:
            return 'Sie haben ein falsches Passwort eingegeben'


class Kassenwart(User):

    def __init__(self):
        super().__init__(name, password)
        self._role = 'kassenwart'

class Referent_Finanzen(User):
    pass


class Administrator(User):

    def __init__(self,  name: str, password: str):
        super().__init__(name, password)
        self._role = 'admin'
        self.created_departments = {}

    def create_department(self, name, balance : int | float):

        # boolean indicates, whether object already exists
        finder = False
        name = name.lower()

        # Check the value and type of input balance
        if not isinstance(balance, (int, float)) or balance < 0:
            print("Der Anfangsbestand muss eine positive Zahl sein.")
            return

        # Check whether object already exists
        if len(lst_of_departments) == 0:
            pass
        else:
            for dpt in lst_of_departments:
                if name in dpt._department:
                    print(f"Die Abteilung {name} existiert schon.")
                    finder = True

        # If object doesn't exist create it and add to list
        if not finder:
            new_account = Club_Accounts(name, balance)
            lst_of_departments.append(new_account)
            print(f"Die Abteilung {name} wurde mit einem Anfangsbestand von {balance}€ erstellt.")

    def del_department(self, name):
        name = name.lower()

        for obj in lst_of_departments:
            if obj._department == name:
                lst_of_departments.remove(obj)

    def backup(self):
        # Backup of department structure + balance
        d_csv = open('department_csv.csv', 'w')
        d_csv.write(f"department;balance\n")
        for dep in lst_of_departments:
            d_csv.write(f"{dep._department};{dep.balance}\n")

        # Backup of usernames and passwords
        u_csv = open('users_csv.csv', 'w')
        u_csv.write(f"username;role\n")
        for user in lst_of_Accounts:
            u_csv.write(f"{user._name};{user._role}\n")

    def create_User(self,name):
        pass

    def del_user(self, name):
        pass

if __name__ == '__main__':
    print(lst_of_departments)
    admin = Administrator('Hans', 'p0815')
    admin.create_department('Tanzen', 26)
    admin.create_department('FUßBALL', 126)
    print(lst_of_departments)
    tanzen = lst_of_departments[0]
    print(lst_of_departments[0].get_information())
    tanzen.deposit_money(76.558)
    admin.del_department('Tanzen')
    print(lst_of_departments)
    print(lst_of_departments[0].get_information())
    print(admin.role)