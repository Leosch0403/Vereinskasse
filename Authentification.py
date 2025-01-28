import tkinter as tk
from User_verwaltung import *
from tkinter import messagebox

# Init main frame
root = tk.Tk()
root.title('Startbildschirm')
root.geometry('400x300')
root.configure(background='white')

admin_name = ['Hannes', 'Anna']
admin_password = ['p_0815', 'anna_03']

admin_lst = []
# Erstellen eines neuen Auto-Objekts und Hinzufügen zur Liste
for name, password in zip(admin_name, admin_password):
    neuer_admin = Administrator(name, password)
    admin_lst.append(neuer_admin)

def authentificator():
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
            messagebox.showinfo('Authentifizierung erfolgreich', f"Willkommen {obj._name}, du bist {obj.role}")

    if not name_count and not password_count:
        print(f"Der eingegebene Benutzername {input_name} "
              f"und Passwort {input_password} existieren nicht")
    elif not name_count:
        print(f"Der eingegebene Benutzername {input_name} existiert nicht")
    elif not password_count:
        print(f"Das eingegebene Passwort {input_password} ist falsch")

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
                         text= 'Eingabe bestätigen',
                         command= authentificator)
start_button.pack(pady= 10)

root.mainloop()