from tkinter import *


def click():
    name = entry_box.get()
    msg = 'Hello ' + name
    output_box['text'] = msg
    output_box['bg'] = 'black'
    output_box['fg'] = 'white'
    return


window = Tk()
window.title('Window Title')
window.geometry('450x300')
entry_box = Entry(text='Enter you name')
entry_box.place(x=50, y=20)
button1 = Button(text='Click here', command=click)
button1.place(x=50, y=50)
output_box = Message(text='')
output_box.place(x=50, y=80)
output_box['bg'] = 'black'
output_box['fg'] = 'white'
window.mainloop()
