from tkinter import *
import csv


def new_csv():
    file = open('131 File.csv', 'w')
    file.close()
    return


def add_csv():
    file = open('131 File.csv', 'a')
    record = entry_box_name.get() + ',' + entry_box_age.get() + '\n'
    file.write(str(record))
    file.close()
    entry_box_name.delete(0, END)
    entry_box_age.delete(0, END)
    entry_box_name.focus()
    return


window = Tk()
window.title('131')
window.geometry('450x400')
lbl = Label(text='Enter name:')
lbl.place(x=50, y=0, width=100, height=25)

entry_box_name = Entry(text='')
entry_box_name.place(x=50, y=20, width=115, height=25)
entry_box_name.focus()

lbl2 = Label(text='Enter age:')
lbl2.place(x=175, y=0, width=100, height=25)

entry_box_age = Entry(text=0)
entry_box_age.place(x=175, y=20, width=115, height=25)
entry_box_age.focus()

button1 = Button(text='New CSV', command=new_csv)
button1.place(x=50, y=210, width=100, height=25)


button3 = Button(text='Add to csv', command=add_csv)
button3.place(x=50, y=50, width=100, height=25)

window.mainloop()
