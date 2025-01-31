__author__ = 'Leonard Schmid'

from Vereinskasse import Clb_dep_acc

class User:
    lst_of_users = []

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._role = 'user'
        User.lst_of_users.append(self)

    def change_password(self, old_password, new_password):

        if old_password == self._password:
            self._password = new_password
            return (f"Das Passwort von {self._username} wurde "
                    f"von {old_password} zu {new_password} geändert.")
        else:
            return (f"Das eingegebene alte Passwort {old_password} ist Falsch. "
                    f"Daher kommt es zu keiner Änderung.")

    def get_info(self):
        return f"Name: {self._username}, Passwort: {self._password}, Rolle: {self._role}"

class Kassenwart(User):

    def __init__(self, username, password, department):
        super().__init__(username, password)
        self._role = 'kassenwart'
        self._department = department

    def get_info(self):
        return (f"Name: {self._username}, Passwort: {self._password}, "
                f"Rolle: {self._role}, Abteilung: {self._department}")

class Referent_Finanzen(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self._role = 'referent_finanzen'

    def view_trans_history(self, name):
        # Alle Sachen in lst_of_dep durchgehen und dann den richtigen suchen
        # Muss einfach nur self.transactions von dem Objekt aufrufen
        pass

class Administrator(User):
    """
    Administrator class inherits from User and provides functionalities
    to manage departments and users, including creating and deleting departments,
    and managing different types of users (e.g., Kassenwart, Admin, User, Referent_Finanzen).
    """

    def __init__(self,  username: str, password: str):
        super().__init__(username, password)
        self._role = 'admin'

    @classmethod
    def create_department(self, name, balance : int | float, trans_history=None):
        """
        Creates a new department with the specified name, balance, and transaction history.
        Checks if the balance is valid and whether the department already exists.
        """
        name = name.lower()
        # Check the value and type of input balance
        if not isinstance(balance, (int, float)) or balance < 0:
            return "Abteilung kann nicht erstellt werden, der Anfangsbestand muss eine positive Zahl sein."

        # Check whether object already exists
        for dpt in Clb_dep_acc.lst_of_dep:
            if name == dpt._department:
                return f"Die Abteilung {name} existiert schon."

        # If object doesn't exist create it and add to list
        new_account = Clb_dep_acc(name, balance, trans_history)
        return f"Abteilung {name} mit einem Kontostand von {balance} erstellt"

    @classmethod
    def del_department(self, name):
        """
        Deletes the department with the given name if it exists.
        Returns a message indicating success or failure.
        """
        name = name.lower()
        # Iterate through list of objects and finds the department
        for obj in Clb_dep_acc.lst_of_dep:
            if obj._department == name:
                Clb_dep_acc.lst_of_dep.remove(obj)
                return f"Die Abteilung {name} wurde gelöscht."

        return f"Die Abteilung {name} existiert nicht und kann nicht gelöscht werden."

    @classmethod
    def create_kassenwart(self, username, password, department):
        """
        Creates a Kassenwart user and assigns them to a department.
        Checks if the user or department already exists before creating the user.
        """
        # boolean indicates, whether object already exists
        finder_d = False
        # Error prevention
        name = username.lower()
        department = department.lower()

        # Check whether user already exists
        for user in User.lst_of_users:
            if name in user._username:
                return f"Der User {name} existiert schon."

        # Check whether department doesn't exist
        for dpt in Clb_dep_acc.lst_of_dep:
            if department == dpt._department:
                finder_d = True
        if not finder_d:
            return (f"Die Abteilung {department} existiert noch nicht. "
                    f"Daher kann der Kassenwart nicht zugeordnet werden")

        # Create User
        new_user = Kassenwart(username, password, department)
        return (f"Es wurde ein Kassenwart {name} mit der "
                f"zugehörigen Abteilung {department} erstellt")

    @classmethod
    def create_user(self, username, password, usertype):
        """
        Creates a user of the specified type (referent_finanzen, user, admin).
        Checks if the user already exists before creating the user.
        """
        # Error prevention
        name = username.lower()
        usertype = usertype.lower()

        # Check whether user already exists
        for user in User.lst_of_users:
            if name in user._username:
                return f"Der User {name} existiert bereits."

        # Create User
        if usertype == 'referent_finanzen':
            new_user = Referent_Finanzen(name, password)
            return f"Es wurde ein Finanzreferent erstellt"
        if usertype == 'user':
            new_user = User(name, password)
            return f"Es wurde ein normaler User erstellt"
        if usertype == 'admin':
            new_user = Administrator(name, password)
            return f"Es wurde ein Administrator erstellt"
        else:
            return f"Den Usertyp {usertype} gibt es nicht, daher kann er nicht erstellt werden"

    @classmethod
    def del_user(self, name):
        """
        Deletes a user by their username.
        Searches through the list of users and removes the user if found.
        """

        finder_u = False  # Indicates whether the user was found
        name = name.lower()  # Error prevention
        index = []  # list to store index of found user

        # Search for username and add its index to the list
        for i in range(len(User.lst_of_users)):
            if name == User.lst_of_users[i]._username:
                finder_u = True
                index.append(i)
        # If found delete the object according to index
        for num in index:
            del User.lst_of_users[num]
            return f"Der User {name} wurde gelöscht."

        if not finder_u:
            return f"Der User {name} existiert nicht und kann daher nicht gelöscht werden."

    @classmethod
    def backup(self):
        """
        Creates backups of department data and user data.
        Saves department structure, balance, and transaction history to 'department_csv.csv'.
        Saves usernames, passwords, roles, and departments (if applicable) to 'users_csv.csv'.
        """
        # Backup of department structure and balance
        d_csv = open('department_csv.csv', 'w')
        d_csv.write(f"department;balance;transaction_history\n")
        for dep in Clb_dep_acc.lst_of_dep:
            # Write each department's data to the CSV
            d_csv.write(f"{dep._department};{dep.balance};{dep.transactions}\n")

        # Backup of usernames and passwords
        u_csv = open('users_csv.csv', 'w')
        u_csv.write(f"username;password;role;department\n")
        for user in User.lst_of_users:
            # Write each user's data to the CSV
            if user._role == 'kassenwart':
                u_csv.write(f"{user._username};{user._password};{user._role};{user._department}\n")
            else:
                u_csv.write(f"{user._username};{user._password};{user._role}\n")
        return f"Backup erfolgreich erstellt"

    @classmethod
    def get_users(self):
        """
        Prints information about all users in the system.
        """
        for usr in User.lst_of_users:
            print(usr.get_info())

    @classmethod
    def get_departments(self):
        """
        Prints information about all departments in the system.
        """
        for dep in Clb_dep_acc.lst_of_dep:
            print(dep.get_information())


if __name__ == '__main__':
    print(User.lst_of_users)
    print(Clb_dep_acc.lst_of_dep)
    Administrator.create_department('Schach', 34)
    print(Clb_dep_acc.lst_of_dep)
    Administrator.create_department('Schwimen', 20, [80,-60])
    print(Clb_dep_acc.lst_of_dep)
    Administrator.get_departments()


'''    admin.del_user('bob')
    admin.create_department('Tanzen', 26)
    admin.create_department('FUßBALL', 126)
    kassenwart_1 = Kassenwart('kathy', '#dead', 'fußball')
    admin.create_user('mika', 'hallo', 'referent')
    admin.create_user('Jochen', 'hiwi', 'admin')
    admin.create_user('dennis_05', 'jaaahr', 'user')
    admin.create_kassenwart('mina', 'm&m', 'tanzen')

    admin.get_users()
    print('')
    admin.del_user('dennis_05')
    admin.del_user('MiKa')
    admin.change_password('#dead', 'neues Passwort')
    admin.get_users()
    #admin.backup()'''
