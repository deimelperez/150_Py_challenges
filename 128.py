from tkinter import *


def convert_km():
    num = int(entry_box.get())
    entry_box.delete(0, END)
    out_box_km['text'] = str(num)
    out_box_mi['text'] = str(num * 0.6214)
    return


def convert_mi():
    num = int(entry_box.get())
    entry_box.delete(0, END)
    out_box_mi['text'] = str(num)
    out_box_km['text'] = str(num * 1.6093)
    return


window = Tk()
window.title('Distance')
window.geometry('450x400')

lbl = Label(text='Enter number:')
lbl.place(x=50, y=0, width=100, height=25)

entry_box = Entry(text=0)
entry_box.place(x=50, y=20, width=230, height=25)

button1 = Button(text='KM-->Mi', command=convert_km)
button1.place(x=50, y=50, width=100, height=25)

button2 = Button(text='KM<--Mi', command=convert_mi)
button2.place(x=180, y=50, width=100, height=25)

lbl = Label(text='KM:')
lbl.place(x=50, y=80, width=100, height=25)

lbl2 = Label(text='Mi:')
lbl2.place(x=180, y=80, width=100, height=25)

out_box_km = Message(text="KM")
out_box_km.place(x=50, y=80, width=100, height=25)

out_box_mi = Message(text="Mi")
out_box_mi.place(x=180, y=80, width=100, height=25)

window.mainloop()
