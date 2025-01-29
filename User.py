__author__ = 'Leonard Schmid'
import csv
from Vereinskasse import Club_Accounts

# Lists that contain the created objects
lst_of_Accounts = []
lst_of_departments = []

class User:

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._role = 'user'

    def change_password(self, old_password, new_password):

        if old_password == self._password:
            self._password = new_password
            return 'Sie haben das Passwort erfolgreich geändert'
        else:
            return 'Sie haben ein falsches Passwort eingegeben'

    def info(self):
        return f"Name: {self._username}, Passwort: {self._password}, Rolle: {self._role}"


class Kassenwart(User):

    def __init__(self, username, password, department):
        super().__init__(username, password)
        self._role = 'kassenwart'
        self._department = department

    def info(self):
        return (f"Name: {self._username}, Passwort: {self._password}, "
                f"Rolle: {self._role}, Abteilung: {self._department}")

class Referent_Finanzen(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self._role = 'referent_finanzen'


class Administrator(User):

    def __init__(self,  username: str, password: str):
        super().__init__(username, password)
        self._role = 'admin'

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

    def del_department(self, name):
        name = name.lower()

        for obj in lst_of_departments:
            if obj._department == name:
                lst_of_departments.remove(obj)

    def create_kassenwart(self, username, password, department):

        # boolean indicates, whether object already exists
        finder_u = False
        finder_d = False

        # Error prevention
        name = username.lower()
        department = department.lower()

        # Check whether user already exists
        for user in lst_of_Accounts:
            if name in user._username:
                finder_u = True
                return print(f"Der User {name} existiert schon.")

        # Check whether department doesn't exist
        for dpt in lst_of_departments:
            if department == dpt._department:
                finder_d = True
        if not finder_d:
            return print(f"Die Abteilung {department} existiert noch nicht. "
                      f"Daher kann der Kassenwart nicht zugeordnet werden")

        # Create User
        if not finder_u:
            new_user = Kassenwart(username, password, department)
            lst_of_Accounts.append(new_user)

    def create_user(self, username, password, usertype):

        # boolean indicates, whether object already exists
        finder_u = False
        # Error prevention
        name = username.lower()
        usertype = usertype.lower()

        # Check whether user already exists
        for user in lst_of_Accounts:
            if name in user._username:
                finder_u = True
                return print(f"Der User {name} existiert schon.")

        # Create User
        if not finder_u:
            if usertype == 'referent':
                new_user = Referent_Finanzen(name, password)
                lst_of_Accounts.append(new_user)
            if usertype == 'user':
                new_user = User(name, password)
                lst_of_Accounts.append(new_user)
            if usertype == 'admin':
                new_user = Administrator(name, password)
                lst_of_Accounts.append(new_user)
            else:
                return f"Den Usertyp {usertype} gibt es nicht"


    def del_user(self, name):

        finder_u = False
        name = name.lower()
        index = []

        # Search for username and add its index to the list
        for i in range(len(lst_of_Accounts)):
            if name == lst_of_Accounts[i]._username:
                finder_u = True
                index.append(i)
        # If found delete the object according to index
        for num in index:
            del lst_of_Accounts[num]

        if not finder_u:
            return print(f"Der User {name} existiert nicht und kann daher nicht gelöscht werden.")

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
            u_csv.write(f"{user._username};{user._role}\n")

    def get_users(self):
        for usr in lst_of_Accounts:
            print(usr.info())


if __name__ == '__main__':
    admin = Administrator('Hans', 'p0815')
    lst_of_Accounts.append(admin)

    admin.del_user('bob')
    admin.create_department('Tanzen', 26)
    admin.create_department('FUßBALL', 126)
    kassenwart_1 = Kassenwart('kathy', '#dead', 'fußball')
    lst_of_Accounts.append(kassenwart_1)
    admin.create_user('mika', 'hallo', 'referent')
    admin.create_user('Jochen', 'hiwi', 'admin')
    admin.create_user('dennis_05', 'jaaahr', 'user')
    admin.create_kassenwart('mina', 'm&m', 'tanzen')

    admin.get_users()
    print('')
    admin.del_user('dennis_05')
    admin.del_user('MiKa')
    lst_of_Accounts[1].change_password('#dead', 'neues Passwort')
    admin.get_users()

