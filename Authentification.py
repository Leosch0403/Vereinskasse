import tkinter as tk

# Init main frame
root = tk.Tk()
root.title('Startbildschirm')
root.geometry('400x300')
root.configure(background='white')

def info():
    name = name_entry.get()
    print(f"Your name is {name}")


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
                         command= info)
start_button.pack(pady= 10)

root.mainloop()