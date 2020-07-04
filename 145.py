from tkinter import *
import sqlite3


def add():
    with sqlite3.connect('145_grades.db') as db:
        cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    name text NOT NULL,
    grade integer NOT NULL);""")
    name = entry_box_name.get()
    entry_box_name.delete(0, END)
    grade = int(entry_box_grade.get())
    entry_box_grade.delete(0, END)
    entry_box_name.focus()
    cursor.execute("""INSERT INTO students(name,grade)
    VALUES(?,?)""", (name, grade))
    db.commit()
    db.close()
    return


def reset():
    entry_box_name.delete(0, END)
    entry_box_grade.delete(0, END)
    return


window = Tk()
window.title('Window Title')
window.geometry('450x200')
lbl = Label(text='Enter name:')
lbl.place(x=50, y=20, width=100, height=25)

entry_box_name = Entry(text='')
entry_box_name.place(x=150, y=20, width=230, height=25)
entry_box_name.focus()

lbl = Label(text='Enter grade:')
lbl.place(x=50, y=50, width=100, height=25)

entry_box_grade = Entry(text=0)
entry_box_grade.place(x=150, y=50, width=230, height=25)
entry_box_grade.focus()

button1 = Button(text='Add', command=add)
button1.place(x=150, y=80, width=100, height=25)

button2 = Button(text='Reset', command=reset)
button2.place(x=280, y=80, width=100, height=25)

window.mainloop()

