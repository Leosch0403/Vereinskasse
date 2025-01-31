import csv

from User import Administrator, User
from entry_field import read_cache

def read_dep_csv():
    """
    Reads the 'department_csv.csv' file and processes each line. If the line has 2 columns,
    it creates a department with just the name and balance. If the line has 3 columns,
    it also includes the transaction history.
    """
    with open('department_csv.csv') as csv_of_dep:  # Open CSV file and read each line
        lst_of_lines = list(csv.reader(csv_of_dep, delimiter=';'))
        del lst_of_lines[0]  # Remove the header line
        # Checks information in line and creates department
        for line in lst_of_lines:
            if len(line) <= 2:
                Administrator.create_department(line[0], float(line[1]))
            else:
                Administrator.create_department(line[0], float(line[1]), line[2])

def read_user_csv():
    """
    Reads the 'users_csv.csv' file, processes each line, and creates users with specific roles
    such as 'kassenwart', 'admin', 'user', and 'referent_finanzen'.
    """
    with open('users_csv.csv') as csv_of_usr:  # Open CSV file and read each line
        lst_of_lines = list(csv.reader(csv_of_usr, delimiter=';'))
        del lst_of_lines[0]  # Remove the header line
        # Checks information in line and creates user according to role
        for line in lst_of_lines:
            role = line[2]
            if role == 'kassenwart':
                Administrator.create_kassenwart(line[0], line[1], line[3])
            if role == 'admin' or 'user' or 'referent_finanzen':
                Administrator.create_user(line[0], line[1], line[2])

def read_all_csv():
    """
    Read both the department and user CSV files and process them.
    """
    read_dep_csv()
    read_user_csv()

def start_tk_module():
    """
    Initializes the process of reading CSV files and checks the cache for a user.
    Returns the user object that matches the username from the cache.
    """
    read_all_csv()
    user = read_cache()[0]  # Get the first cached user
    # Iterates through the user list and returns correct user object
    for usr in User.lst_of_users:
        if user == usr._username:
            return usr

if __name__ == '__main__':
    read_all_csv()
    Administrator.get_users()
    Administrator.del_user('mika')
    print('')
    Administrator.get_users()
    Administrator.get_departments()
    print(Administrator.create_department('Golf',0))
    print('')
    Administrator.get_departments()
    Administrator.del_department('Schach')
    print('')
    Administrator.get_departments()