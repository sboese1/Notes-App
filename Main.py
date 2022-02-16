from tkinter import *
import sqlite3

con = sqlite3.connect('main.db')
cur = con.cursor()


def create_note():
    title_text = title.get('1.0', END)
    note_text = notes.get('1.0', END)

    cur.execute("INSERT INTO main_notes VALUES (?, ?)", (title_text.strip(), note_text.strip()))
    for i in cur.execute('SELECT * FROM main_notes'):
        print(i)


root = Tk()
frame = Frame(root)
root.resizable(False, False)

title = Text(root, bd=2, height=1, width=35)
title.pack()

notes = Text(root, bd=2, height=50, width=50)
notes.pack()

submit_button = Button(root, text='Submit', command=create_note)
submit_button.pack()


def open_menu():
    title.pack_forget()
    notes.pack_forget()
    submit_button.pack_forget()


menu = Button(root, text='Notes', height=1, bd=0, command=open_menu)
menu.place(x=12, y=0)

mainloop()

cur.close()
