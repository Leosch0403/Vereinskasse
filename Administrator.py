__author__ = 'Leonard Schmid'

from User import *
from Vereinskasse import Club_Accounts
import tkinter as tk
import subprocess
import sys
from tkinter import messagebox

#init main frame
root = tk.Tk()
root.title('Administrator')
root.configure(background='white')
root.geometry("800x400")

# Create Testobjects
admin = Administrator('Hans', 'p0815')
lst_of_Accounts.append(admin)
print(admin._role)
admin.create_department('Tanzen', 26)
admin.create_department('FUßBALL', 166)
admin.create_user('mika', 'hallo', 'referent')
admin.create_user('Jochen', 'hiwi', 'admin')
admin.create_user('dennis_05', 'jaaahr', 'user')
admin.create_kassenwart('mina', 'm&m', 'tanzen')

user = #you get that from authentification

def logout():
    messagebox.showinfo('Logout', f"Logout erfolgreich")
    subprocess.Popen([sys.executable, 'Authentification.py'])
    sys.exit()

def backup_csv():
    messagebox.showinfo('Backup', f"CSV Backup erfolgreich")
    admin.backup()

def chng_pswd():




def lst_dep():
    # Init frame
    info_frame = tk.Frame(root, background='white', width=400)
    info_frame.pack(side='left', fill='y')
    info_frame.columnconfigure(0, weight=1)
    info_frame.columnconfigure(1, weight=1)

    # Set the header labels for the user and role
    user = tk.Label(info_frame, font='Arial 16 bold', foreground='white', background='black', text="Abteilung")
    user.grid(row=0, column=0, sticky="ew")
    role = tk.Label(info_frame, font='Arial 16 bold', foreground='black', background='lightblue', text="Kontostand")
    role.grid(row=0, column=1, sticky="ew")

    # fill rest of grid with the usernames
    count = 1
    for dep in lst_of_departments:
        username = tk.Label(info_frame, background='white', text=f"{dep._department}")
        username.grid(row=count, column=0)

        userrole = tk.Label(info_frame, background='white', text=f"{dep.balance}")
        userrole.grid(row=count, column=1)

        count += 1

def lst_usr():
    # Init frame
    info_frame = tk.Frame(root, background='white', width=400)
    info_frame.pack(side='left', fill='y')
    info_frame.columnconfigure(0, weight=1)
    info_frame.columnconfigure(1, weight=1)

    # Set the header labels for the user and role
    user = tk.Label(info_frame, font='Arial 16 bold', foreground='white', background='black', text="Username")
    user.grid(row=0, column=0, sticky="ew")
    role = tk.Label(info_frame, font='Arial 16 bold', foreground='black', background='lightblue', text="Role")
    role.grid(row=0, column=1, sticky="ew")

    # fill rest of grid with the usernames
    count = 1
    for user in lst_of_Accounts:
        username = tk.Label(info_frame, background='white', text=f"{user._username}")
        username.grid(row=count, column=0)

        userrole = tk.Label(info_frame, background='white', text=f"{user._role}")
        userrole.grid(row=count, column=1)

        count += 1

def create_dep():
    # Init entry field and read the input information
    cache('Abteilung:', 'Kontostand:')
    run_entry_field()
    info1, info2 = read_cache()
    admin.create_department(info1, float(info2))
    messagebox.showinfo('Erstellung erfolgreich',
                        f"Du hast erfolgreich die Abteilung {info1} erstellt.")

def create_usr():

def del_dep():

def del_usr():


def admin_functionality_btns():
    """
    Creates a frame containing buttons with functionalities for the administartor
    """
    # Create left frame that displays the created users and departments
    button_frame = tk.Frame(root,
                            width=400
                            )
    button_frame.pack(side='left',
                      fill='y')

    # Create department
    btn_create_dep = tk.Button(button_frame,
                           text="Abteilung erstellen",
                           command=create_dep)
    btn_create_dep.pack(fill='x')

    # Delete department
    btn_del_dep = tk.Button(button_frame,
                            text="Abteilung löschen",
                            command=)
    btn_del_dep.pack(fill='x')

    # list of departments
    btn_lst_dep = tk.Button(button_frame,
                            text="Alle erstellten Abteilungen einsehen",
                            command=lst_dep)
    btn_lst_dep.pack(fill='x')

    # create user
    btn_create_usr = tk.Button(button_frame,
                            text="User erstellen",
                            command=)
    btn_create_usr.pack(fill='x')

    # delete user
    btn_del_usr = tk.Button(button_frame,
                            text="User löschen",
                            command=)
    btn_del_usr.pack(fill='x')

    # list of users
    btn_lst_usr = tk.Button(button_frame,
                            text="Alle erstellten User einsehen",
                            command=lst_usr)
    btn_lst_usr.pack(fill='x')

    # Create CSV file
    btn_create_csv = tk.Button(button_frame,
                            text="CSV Backup der User und Abteilungen erstellen",
                            command=backup_csv)
    btn_create_csv.pack(fill='x')

    # Change Password
    btn_ch_pswd = tk.Button(button_frame,
                            text="Passwort ändern",
                            command=)
    btn_ch_pswd.pack(fill='x')

    # Logout
    btn_logout = tk.Button(button_frame,
                           text="Ausloggen",
                           command=logout)
    btn_logout.pack(fill='x')
admin_functionality_btns()

info_frame = tk.Frame(root,
                      background='white',
                      width=400
                      )
info_frame.pack(side='left',
                fill='y')

# Set the label size
l_width = 13
l_height = 1

# Set the labels for the departments
accounts = tk.Label(info_frame,
                    font="Arial 20 bold",
                    background='lightgrey',
                    text=f"Abteilung",
                    width=l_width,
                    height=l_height
                    )
accounts.grid(row=0,column=0, padx=20, pady=20)
count = 1
for obj in lst_of_departments:

    accounts_obj = tk.Label(info_frame,
                        font="Arial 20 bold",
                        background='light grey',
                        text=f"{obj._department}",
                        width=l_width,
                        height=l_height)

    accounts_obj.grid(row=count, column=0)
    count += 1

# Set the labels for the users with the role kassenwart
user = tk.Label(info_frame,
                font="Arial 20 bold",
                background='light grey',
                text=f"Kassenwart",
                width=l_width,
                height=l_height
                )

user.grid(row=0,column=1, padx=20, pady=20)

count_2 = 1
for user in lst_of_Accounts:

    accounts_obj = tk.Label(info_frame,
                        font="Arial 20 bold",
                        background='light grey',
                        text=f"{user._username}",
                        width=l_width,
                        height=l_height)

    accounts_obj.grid(row=count_2, column=1)
    count_2 += 1


admin.backup()
root.mainloop()

#print(lst_of_Accounts,lst_of_departments)
lst_of_Accounts =[]
lst_of_departments = []

if __name__ == '__main__':
    print(lst_of_departments)
    admin = Administrator('Hans', 'p0815')
