from tkinter import *


def clicked():
    name = entry_box_name.get()
    out_box_name['text'] = str('Hello, ' + name + '!')
    return


window = Tk()
window.title('132')
window.geometry('450x400')

window.wm_iconbitmap('132_icon.ico')
window.configure(background='black')

photo = PhotoImage(file='132_logo.gif')
photobox = Label(image=photo)
photobox.image = photo
photobox.place(x=30, y=20, width=390, height=120)

lbl = Label(text='Enter your name:')
lbl.place(x=30, y=150, width=100, height=25)

entry_box_name = Entry(text='')
entry_box_name.place(x=130, y=150, width=100, height=25)
entry_box_name.focus()

button1 = Button(text='Click me!', command=clicked)
button1.place(x=30, y=180, width=100, height=25)

out_box_name = Message(text='')
out_box_name.place(x=130, y=180, width=200, height=25)


window.mainloop()
