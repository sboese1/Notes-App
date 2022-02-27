from tkinter import *
import sqlite3

con = sqlite3.connect('main.db')  # Connects to be database
cur = con.cursor()  # Gives an actionable variable for the database


# Creates a note in the database
def create_note():
    title_text = title.get('1.0', END)  # Gets all the text from the title entry
    note_text = notes.get('1.0', END)  # Gets all the text from the notes entry

    try:
        cur.execute("INSERT INTO main_notes VALUES (?, ?)", (title_text.strip(), note_text.strip()))  # Inserts the title and notes entries into the title and note spot in the database
    except sqlite3.IntegrityError:
        cur.execute("UPDATE main_notes SET note=? WHERE title=?", (note_text.strip(), title_text.strip()))


root = Tk()  # Initializes the tkinter object
main_frame = Frame(root)  # Constructs a frame object
root.geometry("400x750")  # Sets the size of the window
root.resizable(False, False)  # User can't resize the window
indicator = 0

title = Text(root, bd=2, height=1, width=35)  # Creates a text box
title.pack()

notes = Text(root, bd=2, height=44, width=50)  # Creates a text box
notes.pack()

save_button = Button(root, text='Save', command=create_note)  # Creates a save button
save_button.pack()

buttons = []


# Displays the note in the title box and entry box
def display_note(index):
    total_text = cur.execute("SELECT * FROM main_notes WHERE title=?", (index,))  # Gets all of the text that fits index (title)
    title.delete('1.0', 'end')  # Clear the title text box
    text = total_text.fetchall()  # Gets all of the text from total_text
    title.insert(INSERT, text[0][0])  # Inserts the title text in the title text box

    notes.delete('1.0', 'end')  # Gets all of the text from notes
    notes.insert(INSERT, text[0][1])  # Inserts the notes text in the notes text box


# Opens the menu that holds all of the notes saved
def open_menu():
    global indicator
    title.pack_forget()  # Hides the title entry box
    notes.pack_forget()  # Hides the notes entry box
    save_button.pack_forget()  # Hides the save button
    menu.place_forget()  # Hides the menu button

    for index1, i in enumerate(cur.execute('SELECT * FROM main_notes')):  # For every item in the database
        buttons.append(Button(root, text=str(i[0]), height=1, bd=0, command=lambda i=i: display_note(str(i[0]))))  # Create a new button and add it the buttons
        buttons[index1].grid(row=index1, column=0, columnspan=5, sticky=W)  # Add that button to the grid at index index1


# Opens the note-taking form
def open_main():
    for i in buttons:  # Hides all the buttons
        i.grid_forget()
    buttons.clear()

    title.pack()  # Shows the title entry box
    notes.pack()  # Shows the notes entry box
    save_button.pack()  # Shows the save button
    menu.place(x=12, y=0)  # Places the menu button at those coordinates


menu = Button(root, text='Notes', height=1, bd=0, command=open_menu)  # Creates a menu button
menu.place(x=12, y=0)  # Places the menu button at a certain position

back_button = Button(root, text='Back', height=1, bd=0, command=open_main)  # Creates a back button
back_button.place(x=355, y=0)  # Places the back button at a certain position

mainloop()

cur.close()
