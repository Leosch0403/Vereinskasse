import tkinter as tk
from User import *
from tkinter import messagebox
import sys
import subprocess

# Init main frame
root = tk.Tk()
root.title('Startbildschirm')
root.geometry('400x300')
root.configure(background='white')

#Testfaelle
admin_name = ['Hannes', 'Anna']
admin_password = ['p_0815', 'anna_03']

# Erstellen eines neuen Auto-Objekts und Hinzufügen zur Liste
admin_lst = []
for name, password in zip(admin_name, admin_password):
    neuer_admin = Administrator(name, password)
    admin_lst.append(neuer_admin)

def login():
    input_name = name_entry.get()
    input_password = password_entry.get()

    name_count = False
    password_count = False
    for obj in admin_lst:
        if input_name == obj._name:
            name_count = True
        if input_password == obj._password:
            password_count = True

        if input_password == obj._password and input_name == obj._name:
            messagebox.showinfo('Authentifizierung erfolgreich',
                                f"Willkommen {obj._name}, du bist {obj.role}.")

            # Open new and end current Program
            subprocess.Popen([sys.executable, 'Administrator.py'])
            sys.exit()

    # Messages via messagebox if the login was unsuccessful because of a false username or password
    if not name_count and not password_count:
        messagebox.showinfo('falscher Name und Passwort',
                            f"Der eingegebene Benutzername {input_name} "
                            f"und Passwort {input_password} existieren nicht")

    elif name_count and password_count:
        messagebox.showinfo('falsches Passwort',
                            f"Das eingegebene Passwort {input_password} "
                            f"für den Benutzernamen {input_name} ist falsch.")

    elif not name_count:
        messagebox.showinfo('falscher Name',
                            f"Der eingegebene Benutzername {input_name} existiert nicht")

    elif not password_count:
        messagebox.showinfo('falsches Passwort',
                            f"Das eingegebene Passwort {input_password} ist falsch")

# Entry field for name
name_label = tk.Label(root,
                      font= 'Arial',
                      text= 'Nutzername:',
                      background= 'white'
                      )
name_label.pack(pady= 20)

name_entry = tk.Entry(root)
name_entry.pack()

# Entry field for password
password_label = tk.Label(root,
                      font= 'Arial',
                      text= 'Passwort:',
                      background= 'white'
                      )
password_label.pack(pady= 20)

password_entry = tk.Entry(root)
password_entry.pack()

# Button for authorization
start_button = tk.Button(root,
                         font= 'Arial',
                         text= 'Eingabe bestaetigen',
                         command= login)
start_button.pack(pady= 10)

root.mainloop()