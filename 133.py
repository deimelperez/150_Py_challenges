from tkinter import *
import csv


def add_csv():
    file = open('131 File.csv', 'a')
    record = entry_box_name.get() + ',' + entry_box_age.get() + '\n'
    file.write(str(record))
    file.close()
    entry_box_name.delete(0, END)
    entry_box_age.delete(0, END)
    entry_box_name.focus()
    return


def show_list():
    file = list(csv.reader(open('131 File.csv')))
    tmp = []
    name_list.delete(0, END)
    for row in file:
        tmp.append(row)
    x = 0
    for row in tmp:
        name = tmp[x][0]
        age = tmp[x][1]
        x += 1
        element = 'Name: ' + name + ' ' + 'Age: ' + age
        name_list.insert(END, element)
    return


window = Tk()
window.title('132')
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

button3 = Button(text='Add to csv', command=add_csv)
button3.place(x=50, y=50, width=100, height=25)

button1 = Button(text='Show list', command=show_list)
button1.place(x=50, y=80, width=100, height=25)

name_list = Listbox()
name_list.place(x=160, y=80, width=200, height=100)

window.mainloop()


