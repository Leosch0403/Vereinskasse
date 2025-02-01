'''Creates a GUI via tkinter that starts the System of a club system manager'''

__author__ = "8569130, Schmid, 7996364, Salehi"

from csv_reader import start_tk_module
from User import Administrator, User
from entry_field import *
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

# Import data from CSV files
start_tk_module()

def destroy():
    old_count = User.user_count
    user = Administrator.create_user(entry_u.get(), entry_p.get(), 'admin')
    messagebox.showinfo('Admin erstellen', f"{user}")

    if User.user_count > old_count:
        Administrator.backup()
        messagebox.showinfo('Initialisierung erfolgreich',
                            f"Initialisierung erfolgreich: Du wirst zum Login weitergeführt")
        subprocess.Popen([sys.executable, 'Login.py'])
        sys.exit()
    else:
        pass

# Init main frame
root = tk.Tk()
root.title('Initialisierung eines Administrators')
root.geometry('600x400')
root.configure(background='white')

# Welcome current user
lbl_name = tk.Label(root, bg='white', text=f"")
lbl_name.pack()
lbl_name = tk.Label(root, bg='white',
                    text=f"Willkommen, beginne mit der Erstellung eines Administrators")
lbl_name.pack()
lbl3_name = tk.Label(root, bg='white',
                    text=f"Gib dafür den gewünschten Usernamen und Passwort in das Eingabefeld ein.")
lbl3_name.pack()
lbl4_name = tk.Label(root, bg='white',
                    text=f"Bestätige die Erstellung durch klicken des Knopfes")
lbl4_name.pack()
lbl2_name = tk.Label(root, bg='white',
                    text=f"Du kannst zusätzliche User oder Abteilungen über die Dateien")
lbl2_name.pack()
lbl5_name = tk.Label(root, bg='white',
                    text=f"users_csv.csv und department_csv.csv laden")
lbl5_name.pack()
lbl_name = tk.Label(root, bg='white', text=f"")
lbl_name.pack(pady=30)

# Create Entry field
lbl_name = tk.Label(root, bg='white', text=f"Username:")
lbl_name.pack()
entry_u = tk.Entry(root)
entry_u.pack()
lbl_name = tk.Label(root, bg='white', text=f"Passwort:")
lbl_name.pack()
entry_p = tk.Entry(root)
entry_p.pack()

btn = tk.Button(root, text='Eingabe bestaetigen', command=destroy)
btn.pack(pady=20)

root.mainloop()