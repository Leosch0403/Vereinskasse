import csv
from User import Administrator, User

def read_dep_csv():
    with open('department_csv.csv') as csv_of_dep:
        lst_of_lines = list(csv.reader(csv_of_dep, delimiter=';'))
        del lst_of_lines[0]
        for line in lst_of_lines:
            if len(line) <= 2:
                Administrator.create_department(line[0], float(line[1]))
            else:
                Administrator.create_department(line[0], float(line[1]), line[2])

def read_user_csv():
    with open('users_csv.csv') as csv_of_usr:
        lst_of_lines = list(csv.reader(csv_of_usr, delimiter=';'))
        del lst_of_lines[0]
        for line in lst_of_lines:
            role = line[2]
            if role == 'kassenwart':
                Administrator.create_kassenwart(line[0], line[1], line[3])
            if role == 'admin' or 'user' or 'referent_finanzen':
                Administrator.create_user(line[0], line[1], line[2])
def read_all_csv():
    read_dep_csv()
    read_user_csv()

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