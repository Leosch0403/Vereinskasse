__author__ = 'Leonard Schmid'

from User import *
import tkinter as tk

#init main frame
root = tk.Tk()
root.title('Administrator')
root.configure(background='white')
root.geometry("800x400")

# Create Testobjects
admin = Administrator('Hans', 'p0815')
lst_of_Accounts.append(admin)
admin.create_department('Tanzen', 26)
admin.create_department('FUßBALL', 126)

# Create left frame that displays the created users and departments
info_frame = tk.Frame(root,
                      background='#bcbfd7',
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
                        text=f"{user._name}",
                        width=l_width,
                        height=l_height)

    accounts_obj.grid(row=count_2, column=1)
    count_2 += 1



root.mainloop()

#print(lst_of_Accounts,lst_of_departments)