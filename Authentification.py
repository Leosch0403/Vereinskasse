import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
from User import Administrator

# Init main frame
root = tk.Tk()
root.title('Startbildschirm')
root.geometry('400x300')
root.configure(background='white')

# Testfaelle
admin_name = ['Hannes', 'Anna']
admin_password = ['p_0815', 'anna_03']

# Erstellen eines neuen Auto-Objekts und Hinzufügen zur Liste
admin_lst = []
for name, password in zip(admin_name, admin_password):
    neuer_admin = Administrator(name, password)
    admin_lst.append(neuer_admin)


def entry_field_auth(fst_label, snd_label, tgt_function):
    """
    Creates input fields for username and password along with a submit button.

    Parameters:
        fst_label (str): Label text for the username field.
        snd_label (str): Label text for the password field.
        function (function): The function to execute when the button is clicked.

    Returns:
        tuple: Returns references to the username and password entry fields.
    """

    # Label for username input
    name_label = tk.Label(root, font='Arial', text=fst_label, background='white')
    name_label.pack(pady=10)

    # Input field for username
    n_entry = tk.Entry(root)
    n_entry.pack()

    # Label for password input
    password_label = tk.Label(root, font='Arial', text=snd_label, background='white')
    password_label.pack(pady=10)

    # Input field for password (masked with '*')
    p_entry = tk.Entry(root, show="*")
    p_entry.pack()

    # Button to submit login details
    start_button = tk.Button(root, font='Arial', text='Confirm Entry',
                             command=lambda: tgt_function(n_entry.get(), p_entry.get()))
    start_button.pack(pady=10)


def login(input_name, input_password):
    """
    Handles user authentication by checking the entered username and password
    against the predefined list of admins.

    Parameters:
        name_entry (tk.Entry): The username input field.
        password_entry (tk.Entry): The password input field.
    """
    # Flag to check if parameters exists
    name_count = False
    password_count = False
    user_role = None

    # Iterate through the admin list to check for matches
    for obj in admin_lst:
        if input_name == obj._username:
            name_count = True  # Username found
            if input_password == obj._password:
                password_count = True  # password found
                user_role = obj._role  # Store user role
                break  # Stop searching since user is found

    # Authentication successful
    if name_count and password_count:
        messagebox.showinfo('Login erfolgreich',
                            f"Willkommen {input_name}, du bist {user_role}.")

        # Open a new script and close the current application
        subprocess.Popen([sys.executable, 'Administrator.py'])
        root.destroy()

    # Handle incorrect credentials
    elif not name_count and not password_count:
        messagebox.showerror('Error', "Username und Passwort sind inkorrekt")
    elif not name_count:
        messagebox.showerror('Error', f"Der Username '{input_name}' existiert nicht")
    else:
        messagebox.showerror('Error', "Falsches Passwort")


# Create entry fields and assign the login function to the button
entry_field_auth('Username:', 'Passwort:', login)

# Start the Tkinter event loop
root.mainloop()