'''Creates a GUI via tkinter that displays the functionalities of a finance referent'''

__author__ = "8569130, Schmid, 7996364, Salehi"

from csv_reader import start_tk_module
from entry_field import *
from User import Referent_Finanzen
import tkinter as tk
import subprocess
import sys
from tkinter import messagebox

# Import data from CSV files and set the current user
current_user = start_tk_module()

#init main frame
root = tk.Tk()
root.title('Referent Finanzen')
root.configure(background='white')
root.geometry('1600x300')

def logout():
    """
    Logs the user out, shows a confirmation message, and restarts the authentication process.
    Exits the program after triggering the authentication script.
    """
    messagebox.showinfo('Logout', f"Logout erfolgreich")
    subprocess.Popen([sys.executable, 'Login.py'])
    sys.exit()

def trns_his():
    """
    Creates and displays a frame showing the transaction history of a department and their balances.
    """
    # Define the header of the entry field and open it
    cache(['Transaktionshistorie von folgender Abteilung einsehen:'])
    process = subprocess.Popen([sys.executable, 'entry_field.py'])
    process.wait()  # Wait until entry field is closed
    data = read_cache()  # Read input data
    trns_history = Referent_Finanzen.view_transaction_history(data[0])  # Search for input department
    if isinstance(trns_history, list):
        pass
    else:
        messagebox.showinfo('User erstellen', f"{trns_history}")
        return

    # Checks whether the frame already exists and deletes it
    global info_frame
    if 'info_frame' in globals():
        info_frame.pack_forget()

    # Init frame
    info_frame = tk.Frame(root, background='white', width=400)
    info_frame.pack(side='left', fill='y')

    # Department name label
    label = tk.Label(info_frame, font='Arial 16 bold', foreground='white',
                     background='black', text=f"Abteilung {trns_history[0]}")
    label.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Set the header labels
    user = tk.Label(info_frame, font='Arial 16 bold', background='red', text="Transaktionen")
    user.grid(row=1, column=0, sticky="ew")
    role = tk.Label(info_frame, font='Arial 16 bold', foreground='black', background='lightblue', text="Kontostand")
    role.grid(row=1, column=1, sticky="ew")
    role = tk.Label(info_frame, font='Arial 16 bold', foreground='black', background='lightgreen', text="Grund")
    role.grid(row=1, column=2, sticky="ew")

    # fill rest of grid
    count = 2
    balance = 0
    for info in trns_history[1]:
        transfer = tk.Label(info_frame, background='white', text=f"{info[0]}")
        transfer.grid(row=count, column=0)
        balance += info[0]
        ovr_balance = tk.Label(info_frame, background='white', text=f"{balance}")
        ovr_balance.grid(row=count, column=1)
        reason = tk.Label(info_frame, background='white', text=f"{info[1]}")
        reason.grid(row=count, column=2)

        count += 1

def trns_ev_his():
    """
    Creates and displays a frame showing the transaction history of all departments .
    """
    all_trans = Referent_Finanzen.view_all_transactions()

    # Checks whether the frame already exists and deletes it
    global info_frame
    if 'info_frame' in globals():
        info_frame.pack_forget()

    # Initialize the frame for displaying transaction information
    info_frame = tk.Frame(root, background='white')  # Create a new frame with white background
    info_frame.pack(side='left', fill='y')  # Pack the frame to the left side of the window, fill vertically

    iterations = 0
    # Iterate through all transactions
    for list in all_trans:
        department = list[0]
        transaction_history = list[1]
        # Department name label
        label = tk.Label(info_frame, font='Arial 12 bold', foreground='white',
                         background='black', text=f"Abteilung {department}")
        label.grid(row=0, column=0+iterations, columnspan=3, sticky="nsew")

        # Header labels for transaction details
        user = tk.Label(info_frame, font='Arial 12 bold', foreground='black',
                        background='red', text="Transactions")
        user.grid(row=1, column=0+iterations, sticky="ew")

        balance_label = tk.Label(info_frame, font='Arial 12 bold', foreground='black',
                                 background='lightblue', text="Balance")
        balance_label.grid(row=1, column=1+iterations, sticky="ew")

        reason_label = tk.Label(info_frame, font='Arial 12 bold', foreground='black',
                                background='lightgreen', text="Reason")
        reason_label.grid(row=1, column=2+iterations, sticky="ew")

        # Filling the remaining rows with transaction data
        count = 2  # Start at row 2 for transaction data
        balance = 0

        for info in transaction_history:  # Iterate through each transaction in the department's history
            transfer = tk.Label(info_frame, background='white', text=f"{info[0]}")
            transfer.grid(row=count, column=0+iterations)  # Display transaction amount in column 0

            balance += info[0]  # Update balance with the transaction amount
            ovr_balance = tk.Label(info_frame, background='white', text=f"{balance}")
            ovr_balance.grid(row=count, column=1+iterations)  # Display updated balance in column 1

            reason = tk.Label(info_frame, background='white', text=f"{info[1]}")
            reason.grid(row=count, column=2+iterations)  # Display reason for transaction in column 2

            count += 1  # Increase the row number for the next transaction

        iterations += 3

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

# View transaction History
btn_th = tk.Button(button_frame,
                       text="Einzelne Transaktionshistorie einsehen",
                       command=trns_his)
btn_th.pack(fill='x')

# View every transaction History
btn_eth = tk.Button(button_frame,
                       text="Alle Transaktionshistorien einsehen",
                       command=trns_ev_his)
btn_eth.pack(fill='x')

# Logout
btn_logout = tk.Button(button_frame,
                       text="Ausloggen",
                       command=logout)
btn_logout.pack(fill='x')

root.mainloop()