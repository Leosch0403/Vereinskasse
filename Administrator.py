__author__ = 'Leonard Schmid'

from User import *
from entry_field import *
import tkinter as tk
import subprocess
import sys
from tkinter import messagebox

#init main frame
root = tk.Tk()
root.title('Administrator')
root.configure(background='white')
root.geometry("800x400")

def logout():
    messagebox.showinfo('Logout', f"Logout erfolgreich")
    subprocess.Popen([sys.executable, 'Authentification.py'])
    sys.exit()

def backup_csv():
    messagebox.showinfo('Backup', f"CSV Backup erfolgreich")
    admin.backup()

def chng_pswd():
    # Define the header of the entry field and open it
    cache(['Altes Passwort:', 'Neues Passwort:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = admin.change_password(data[0], data[1])  # create user
    messagebox.showinfo('Passwort ändern',f"{user}")

def lst_dep():
    """
    Creates and displays a frame showing a list of departments and their balances.
    If a frame with department information already exists, it will first be hidden
    and replaced with the new one.
    """

    # Checks whether the frame already exists and innthat case deletes it
    global info_frame
    if 'info_frame' in globals():
        info_frame.pack_forget()

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
    """
    Creates and displays a frame showing a list of departments and their balances.
    If a frame with department information already exists, it will first be hidden
    and replaced with the new one.
    """

    # Checks whether the frame already exists and innthat case deletes it
    global info_frame
    if 'info_frame' in globals():
        info_frame.pack_forget()

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
    # Define the header of the entry field and open it
    cache(['Abteilungsname:', 'Guthaben:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data

    # Check whether input data is convertable to float
    try:
        guthaben = float(data[1])
    except ValueError:
        messagebox.showinfo('Abteilung erstellen', f"Fehler: '{data[1]}' ist keine gültige Zahl.")
        return

    dep = admin.create_department(data[0], guthaben)  # create department
    messagebox.showinfo('Abteilung erstellen',f"{dep}")

def create_usr():
    # Define the header of the entry field and open it
    cache(['Username:', 'Passwort:', 'Rolle:'])
    messagebox.showinfo('User erstellen', f"Es gibt folgende Rollen: Admin, User, Referent_finanzen")
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = admin.create_user(data[0], data[1], data[2])  # create user
    messagebox.showinfo('User erstellen',f"{user}")

def del_dep():
    # Define the header of the entry field and open it
    cache(['Zu löschende Abteilung:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = admin.del_department(data[0])  # Delete User
    messagebox.showinfo('User erstellen',f"{user}")

def del_usr():
    # Define the header of the entry field and open it
    cache(['Zu löschender Username:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = admin.del_user(data[0])  # Delete User
    messagebox.showinfo('User erstellen',f"{user}")


# Create left frame that displays the created users and departments
button_frame = tk.Frame(root,
                        width=400
                        )
button_frame.pack(side='left',
                  fill='y')

# Welcome current user
lbl_name = tk.Label(button_frame,
                    text=f"Willkommen {admin._username}")
lbl_name.pack()

# Create department
btn_create_dep = tk.Button(button_frame,
                       text="Abteilung erstellen",
                       command=create_dep)
btn_create_dep.pack(fill='x')

# Delete department
btn_del_dep = tk.Button(button_frame,
                        text="Abteilung löschen",
                        command=del_dep)
btn_del_dep.pack(fill='x')

# list of departments
btn_lst_dep = tk.Button(button_frame,
                        text="Alle erstellten Abteilungen einsehen",
                        command=lst_dep)
btn_lst_dep.pack(fill='x')

# create user
btn_create_usr = tk.Button(button_frame,
                        text="User erstellen",
                        command=create_usr)
btn_create_usr.pack(fill='x')

# delete user
btn_del_usr = tk.Button(button_frame,
                        text="User löschen",
                        command=del_usr)
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
                        command=chng_pswd)
btn_ch_pswd.pack(fill='x')

# Logout
btn_logout = tk.Button(button_frame,
                       text="Ausloggen",
                       command=logout)
btn_logout.pack(fill='x')

root.mainloop()

if __name__ == '__main__':
    # Create Testobjects
    admin = Administrator('Hans', 'p0815')
    lst_of_Accounts.append(admin)
    admin.create_department('Tanzen', 26)
    admin.create_department('FUßBALL', 166)
    admin.create_user('mika', 'hallo', 'referent')
    admin.create_user('Jochen', 'hiwi', 'admin')
    admin.create_user('dennis_05', 'jaaahr', 'user')
    admin.create_kassenwart('mina', 'm&m', 'tanzen')
