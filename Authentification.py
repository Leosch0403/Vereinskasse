import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
from entry_field import cache
from csv_reader import *

# Init main frame
root = tk.Tk()
root.title('Startbildschirm')
root.geometry('400x300')
root.configure(background='white')

read_user_csv()
print(User.lst_of_users)

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
    p_entry = tk.Entry(root)
    p_entry.pack()

    # Button to submit login details
    start_button = tk.Button(root, font='Arial', text='Eingabe bestaetigen',
                             command=lambda: login(n_entry.get(), p_entry.get()))
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
    for obj in User.lst_of_users:
        if input_name == obj._username:
            name_count = True  # Username found
            user_name = obj._username
            if input_password == obj._password:
                password_count = True  # password found
                user_role = obj._role
                break  # Stop searching since user is found

    # Authentication successful
    if name_count and password_count:
        messagebox.showinfo('Login erfolgreich',
                            f"Willkommen {input_name}, du bist {user_role}.")

        # Save username in Zwischenspeicher
        cache([user_name.lower()])

        # Open a new script according to userrole
        if user_role == 'admin':
            subprocess.Popen([sys.executable, 'Administrator.py'])
        elif user_role == 'kassenwart':
            pass
        root.destroy()  # close the current application

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