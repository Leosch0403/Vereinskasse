import tkinter as tk

def read_cache():
    """
    Reads data from 'Zwischenspeicher.txt' and returns the first two lines.

    Returns:
        tuple: A tuple containing the first and second lines from the file.
    """
    lines = []
    with open('Zwischenspeicher.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines[0], lines[1]

def cache(info_1, info_2):
    """
    Writes the provided 2 information into 'Zwischenspeicher.txt' in 2 seperate lines,
    replacing its current content.

    Args:
        info_1 (str): The first piece of information to write.
        info_2 (str): The second piece of information to write.
    """
    with open('Zwischenspeicher.txt', 'w') as new_file:
        new_file.write(info_1)
        new_file.write("\n")
        new_file.writelines(info_2)

def end_entry_field(info_1, info_2, root):
    """
    Saves the input data and closes the input window.

    Args:
        info_1 (str): The first input data to save.
        info_2 (str): The second input data to save.
        root_2 (tk.Tk): The tkinter root window to be closed.
    """
    cache(info_1, info_2)
    root.destroy()

def entry_field(fst_line, snd_line):
    """
    Creates a window with two input fields and a submit button.

    Args:
        fst_line (str): The label text for the first input field.
        snd_line (str): The label text for the second input field.
    """
    root_2 = tk.Tk()  # Create a new tkinter window
    root_2.title('Input Field')
    root_2.configure(background='white')

    # Label for the first input field
    fst_label = tk.Label(root_2, font='Arial', text=fst_line, background='white')
    fst_label.pack(pady=10)

    # First input field
    fst_entry = tk.Entry(root_2)
    fst_entry.pack()

    # Label for the second input field
    snd_label = tk.Label(root_2, font='Arial', text=snd_line, background='white')
    snd_label.pack(pady=10)

    # Second input field
    snd_entry = tk.Entry(root_2)
    snd_entry.pack()

    # Submit button to confirm the input
    start_button = tk.Button(root_2, font='Arial', text='Eingabe bestaetigen',
                             command=lambda: end_entry_field(fst_entry.get(), snd_entry.get(), root_2))
    start_button.pack(pady=10)

    root_2.mainloop()

def run_entry_field():
    """
    Reads the cache data and opens the input window.
    This function is executed when the script is run directly.
    """
    fst_line, snd_line = read_cache()  # Read the cache data
    entry_field(fst_line, snd_line)  # Open the input window


if __name__ == '__main__':
    run_entry_field()
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