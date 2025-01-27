import tkinter as tk

# Init main frame
root = tk.Tk()
root.title('Startbildschirm')
root.geometry('500x500')
root.configure(background='white')
condition = 0

def say_hello():
    messagebox.showinfo('Test', "Hallo, Welt!")

def change_label():
    global condition
    list_of_names = ['Reaktion', 'Hans', 'Baum', 'Test', 'Alice', 1 , 2, 3, 4]
    if condition < len(list_of_names):
        label1.configure(text=list_of_names[condition])
        condition += 1
    else:
        condition = 0




label1 = (tk.Label(
    root,
    text="Was passiert hier?",
    height=3,
    width=15,
    bg='black',
    foreground='white')
)

label1.pack()

action_button = tk.Button(
    root,
    text='Aktion',
    command= change_label)

action_button.pack()

end_button = tk.Button(
    root,
    text='beenden',
    command= root.destroy
).pack()

# Init button 1
hello_button = tk.Button(
    root,
    text='Say hi',
    command=say_hello)

hello_button.pack(
    anchor='nw',
    pady=120,
    padx= 100)
hello_button.configure(
    foreground='#d15c30', font='Arial 18')



# start mainloop
root.mainloop()

'''
activebackground: Hintergrundfarbe, wenn das Widget aktiv ist (z. B. wenn ein Button gedrückt wird).
activeforeground: Vordergrundfarbe (z. B. Textfarbe), wenn das Widget aktiv ist.
anchor: Ausrichtung des Inhalts innerhalb des Widgets (z. B. n, ne, e, se, s, sw, w, nw, center).
background / bg: Hintergrundfarbe.
borderwidth / bd: Breite des Rahmens.
cursor: Form des Mauszeigers, wenn er über dem Widget ist.
font: Schriftart und -größe (z. B. "Arial 12 bold").
foreground / fg: Vordergrundfarbe (z. B. Textfarbe).
height: Höhe des Widgets (in Pixeln oder Zeilen, je nach Widget).
highlightbackground: Farbe des Hervorhebungsrahmens, wenn das Widget nicht aktiv ist.
highlightcolor: Farbe des Hervorhebungsrahmens, wenn das Widget aktiv ist.
highlightthickness: Dicke des Hervorhebungsrahmens.
padx: Horizontaler Abstand innerhalb des Widgets.
pady: Vertikaler Abstand innerhalb des Widgets.
relief: Stil des Rahmens (flat, raised, sunken, groove, ridge).
state: Zustand des Widgets (normal, disabled, active).
takefocus: Gibt an, ob das Widget den Fokus erhalten kann (True oder False).
width: Breite des Widgets (in Pixeln oder Zeichen, je nach Widget).'''