from tkinter import *


def add():
    num = entry_box.get()
    entry_box.delete(0, END)
    if num.isdigit():
        name_list.insert(END, num)
        entry_box.focus()
    return


def reset():
    name_list.delete(0, END)
    entry_box.delete(0, END)
    return


window = Tk()
window.title('129')
window.geometry('450x400')
lbl = Label(text='Enter number:')
lbl.place(x=50, y=0, width=100, height=25)

entry_box = Entry(text=0)
entry_box.place(x=50, y=20, width=230, height=25)
entry_box.focus()

button1 = Button(text='Add', command=add)
button1.place(x=50, y=50, width=100, height=25)

button2 = Button(text='Reset', command=reset)
button2.place(x=180, y=50, width=100, height=25)

lbl2 = Label(text='List:')
lbl2.place(x=50, y=100, width=100, height=25)

name_list = Listbox()
name_list.place(x=160, y=100, width=100, height=100)

window.mainloop()
