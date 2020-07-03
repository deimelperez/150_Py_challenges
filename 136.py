from tkinter import *


def add_list():
    name = entry_name.get()
    gender = select_gender.get()
    record = name + ',' + gender + '\n'
    list_box.insert(END, record)
    entry_name.delete(0, END)
    select_gender.set('Select gender')
    return


window = Tk()
window.title('Window Title')
window.geometry('450x400')

entry_name = Entry(text='')
entry_name.place(x=30, y=20, width=100, height=25)

select_gender = StringVar(window)
select_gender.set('Select gender')
genderList = OptionMenu(window, select_gender, 'Male', 'Female')
genderList.place(x=150, y=20, width=110, height=25)

button1 = Button(text='Add to list', command=add_list)
button1.place(x=30, y=50, width=100, height=25)

list_box = Listbox()
list_box.place(x=150, y=50, width=150, height=125)

window.mainloop()
