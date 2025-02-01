'''Creates a GUI via tkinter that displays the functionalities of a Kassenwart'''

__author__ = "8569130, Schmid, 7996364, Salehi"

from csv_reader import start_tk_module
from entry_field import *
from User import Kassenwart, Administrator
import tkinter as tk
import subprocess
import sys
from tkinter import messagebox
from Vereinskasse import Clb_dep_acc

# Import data from CSV files and set the current user
current_user = start_tk_module()

#init main frame
root = tk.Tk()
root.title('Kassenwart')
root.configure(background='white')
root.geometry("800x400")

def trns_his():
    """
    Creates and displays a frame showing the transaction history of a department and their balances.
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

    # Set the header labels
    user = tk.Label(info_frame, font='Arial 16 bold', foreground='white', background='black', text="Transaktionen")
    user.grid(row=0, column=0, sticky="ew")
    role = tk.Label(info_frame, font='Arial 16 bold', foreground='black', background='lightblue', text="Kontostand")
    role.grid(row=0, column=1, sticky="ew")
    role = tk.Label(info_frame, font='Arial 16 bold', foreground='black', background='lightgreen', text="Grund")
    role.grid(row=0, column=2, sticky="ew")

    # fill rest of grid
    count = 1
    balance = 0
    for dep in Clb_dep_acc.lst_of_dep:
        if current_user._department == dep._dep_name:
            for num in dep.transactions:
                transfer = tk.Label(info_frame, background='white', text=f"{num[0]}")
                transfer.grid(row=count, column=0)
                balance += num[0]
                ovr_balance = tk.Label(info_frame, background='white', text=f"{balance}")
                ovr_balance.grid(row=count, column=1)
                reason = tk.Label(info_frame, background='white', text=f"{num[1]}")
                reason.grid(row=count, column=2)

                count += 1

def add_mny():
    """
    Prompts the user to enter the department name to delete and removes the corresponding department.
    """
    # Define the header of the entry field and open it
    cache(['Zu einzahlender Betrag (positive Zahl):', 'Einzahlungsgrund:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = current_user.deposit(data[0], data[1])  # Delete User
    messagebox.showinfo('User erstellen',f"{user}")

def rmv_mny():
    """
    Prompts the user to enter the department name to delete and removes the corresponding department.
    """
    # Define the header of the entry field and open it
    cache(['Zu abbuchender Betrag (positive Zahl):', 'Abbuchungsgrund:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = current_user.remove(data[0], data[1])  # Delete User
    messagebox.showinfo('User erstellen',f"{user}")

def trf_to():
    """
    Prompts the user to enter the department name to delete and removes the corresponding department.
    """
    # Define the header of the entry field and open it
    cache(['Zu sendender Betrag (positive Zahl):', 'Zielabteilung:', 'Abbuchungsgrund:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = current_user.transfer_to(data[0], data[1], data[2])  # Transfer to
    messagebox.showinfo('Geld transfer',f"{user}")

def trf_from():
    """
    Prompts the user to enter the department name to delete and removes the corresponding department.
    """
    # Define the header of the entry field and open it
    cache(['Zu abbuchender Betrag (positive Zahl):', 'Zielabteilung:', 'Abbuchungsgrund:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = current_user.transfer_from(data[0], data[1], data[2])  # Delete User
    messagebox.showinfo('Geld transfer',f"{user}")

def chng_pswd():
    """
    Prompts the user to change their password by showing an entry field to input old and new passwords.
    """

    # Define the header of the entry field and open it
    cache(['Altes Passwort:', 'Neues Passwort:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    user = current_user.change_password(data[0], data[1])  # change password
    messagebox.showinfo('Passwort ändern',f"{user}")

def logout():
    """
    Logs the user out, shows a confirmation message, and restarts the authentication process.
    Exits the program after triggering the authentication script.
    """
    messagebox.showinfo('Logout', f"Logout erfolgreich")
    subprocess.Popen([sys.executable, 'Login.py'])
    sys.exit()

def backup_csv():
    """
    Initiates a CSV backup process and shows a confirmation message once the backup is successful.
    """
    messagebox.showinfo('Backup', f"CSV Backup erfolgreich")
    Administrator.backup()

# Create left frame that displays the buttons
button_frame = tk.Frame(root,
                        width=400
                        )
button_frame.pack(side='left',
                  fill='y')

# Welcome current user
lbl_name = tk.Label(button_frame,
                    text=f"Willkommen {current_user._username}")
lbl_name.pack()

# Declare according department
lbl_dep = tk.Label(button_frame,
                    text=f"Verantwortlich für Abteilung: {current_user._department}")
lbl_dep.pack()

# View transaction History
btn_th = tk.Button(button_frame,
                       text="Transaktionshistorie einsehen",
                       command=trns_his)
btn_th.pack(fill='x')

# deposit money
btn_dm = tk.Button(button_frame,
                       text="Geld einzahlen",
                       command=add_mny)
btn_dm.pack(fill='x')

# remove money
btn_rm = tk.Button(button_frame,
                       text="Geld abbuchen",
                       command=rmv_mny)
btn_rm.pack(fill='x')

# transfer to other department
btn_tto = tk.Button(button_frame,
                       text="Geld zu anderer Abteilung senden",
                       command=trf_to)
btn_tto.pack(fill='x')

# transfer from other department
btn_tfrom = tk.Button(button_frame,
                       text="Geld von anderer Abteilung abbuchen",
                       command=trf_from)
btn_tfrom.pack(fill='x')

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

# Create CSV Backup
btn_create_csv = tk.Button(button_frame,
                        text="Änderungen speichern",
                        command=backup_csv)
btn_create_csv.pack(fill='x')

root.mainloop()