import tkinter as tk
import subprocess
import sys

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
    return lines

def cache(infomations):
    """
    Writes the provided 2 information into 'Zwischenspeicher.txt' in 2 seperate lines,
    replacing its current content.

    Args:
        info_1 (str): The first piece of information to write.
        info_2 (str): The second piece of information to write.
    """
    with open('Zwischenspeicher.txt', 'w') as new_file:
        for line in infomations:
            new_file.write(line + "\n")

def end_entry_field(information, root):
    """
    Saves the input data (second to last object in list) via the cache function in a txt file,
    sends the user to the next program (first object in list)
    and closes the input window at the end.

        :param information: the list of information
        :param root: The tkinter root window to be closed.
    """
    cache(information)
    root.destroy()

def entry_field(information):
    """
    Creates a window with two input fields and a submit button.

    Args:
        fst_line (str): The label text for the first input field.
        snd_line (str): The label text for the second input field.
    """
    root_2 = tk.Tk()  # Create a new tkinter window
    root_2.title('Eingabefeld')
    root_2.configure(background='white')

    # Bring window to the front
    root_2.lift()
    root_2.attributes('-topmost', True)

    entries = []
    for i in range(len(information)):
        # Label for the input field
        fst_label = tk.Label(root_2, font='Arial', text=f"{information[i]}", background='white')
        fst_label.pack(pady=10)

        # input field
        fst_entry = tk.Entry(root_2)
        fst_entry.pack()
        entries.append(fst_entry)

    def on_submit():
        """
        Gathers the input data from the entry fields, prints it, and passes it to the end_entry_field function.
        """
        informations = [entry.get() for entry in entries]
        end_entry_field(informations, root_2)

    # Submit button to confirm the input
    start_button = tk.Button(root_2, font='Arial', text='Eingabe bestaetigen', command=on_submit)
    start_button.pack(pady=10)

    root_2.mainloop()

def run_entry_field():
    """
    Reads the cache data and opens the input window.
    This function is executed when the script is run directly.
    """
    infos = read_cache()  # Read the cache data
    entry_field(infos)  # Open the input window


if __name__ == '__main__':
    run_entry_field()