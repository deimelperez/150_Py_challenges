from tkinter import *


def add():
    num = int(entry_box.get())
    entry_box.delete(0, END)
    ans = int(output_txt['text'])
    output_txt['text'] = str(num + ans)
    return


def reset():
    output_txt['text'] = 0
    entry_box.delete(0, END)
    return


window = Tk()
window.title('Window Title')
window.geometry('450x400')
lbl = Label(text='Enter number:')
lbl.place(x=50, y=0, width=100, height=25)

entry_box = Entry(text=0)
entry_box.place(x=50, y=20, width=100, height=25)

button1 = Button(text='Add', command=add)
button1.place(x=50, y=50, width=100, height=25)

lbl2 = Label(text='Total:')
lbl2.place(x=50, y=100, width=100, height=25)

output_txt = Message(text=0)
output_txt.place(x=160, y=100, width=100, height=25)

button2 = Button(text='Reset', command=reset)
button2.place(x=50, y=150, width=100, height=25)

window.mainloop()
