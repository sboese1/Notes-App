from tkinter import *
import sqlite3

con = sqlite3.connect('main.db')  # Connects to be database
cur = con.cursor()  # Gives an actionable variable for the database


def create_note():
    title_text = title.get('1.0', END)  # Gets all the text from the title entry
    note_text = notes.get('1.0', END)  # Gets all the text from the notes entry

    cur.execute("INSERT INTO main_notes VALUES (?, ?)", (title_text.strip(), note_text.strip()))  # Inserts the title and notes entries into the title and note spot in the database
    for i in cur.execute('SELECT * FROM main_notes'):
        print(i)


root = Tk()  # Initializes the tkinter object
frame = Frame(root)  # Constructs a frame object
root.resizable(False, False)  # User can't resize the window

title = Text(root, bd=2, height=1, width=35)  # Creates a text box
title.pack()

notes = Text(root, bd=2, height=50, width=50)  # Creates a text box
notes.pack()

submit_button = Button(root, text='Submit', command=create_note)  # Creates a button
submit_button.pack()


def open_menu():
    title.pack_forget()  # Hides the title entry box
    notes.pack_forget()  # Hides the notes entry box
    submit_button.pack_forget()  # Hides the submit button


menu = Button(root, text='Notes', height=1, bd=0, command=open_menu)  # Creates a button
menu.place(x=12, y=0)  # Places the menu button at a certain position

mainloop()

cur.close()
