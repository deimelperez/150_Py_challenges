from tkinter import *
import random


num1 = random.randint(10, 50)
num2 = random.randint(10, 50)


def check():
    ans = int(entry_box_name.get())
    num1 = int(num1_box['text'])
    num2 = int(num2_box['text'])
    if ans == (num1 + num2):
        photo = PhotoImage(file='134_correct.gif')
        photobox = Label(window, image=photo)
        photobox.image = photo
        photobox.place(x=130, y=50, width=200, height=120)
    else:
        photo = PhotoImage(file='134_incorrect.gif')
        photobox = Label(window, image=photo)
        photobox.image = photo
        photobox.place(x=130, y=50, width=200, height=120)
    return


def again():
    entry_box_name.delete(0, END)
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    num1_box['text'] = num1
    num2_box['text'] = num2
    photo = PhotoImage(file='')
    photobox = Label(window, image=photo)
    photobox.image = photo
    photobox.place(x=130, y=50, width=200, height=120)
    return


window = Tk()
window.title('Window Title')
window.geometry('450x400')
window.wm_iconbitmap('132_icon.ico')


num1_box = Message(text=num1)
num1_box.place(x=50, y=20, width=30, height=25)

plus_box = Message(text=' + ')
plus_box.place(x=80, y=20, width=30, height=25)

num2_box = Message(text=num2)
num2_box.place(x=110, y=20, width=30, height=25)

equal_box = Message(text=' = ')
equal_box.place(x=140, y=20, width=30, height=25)

entry_box_name = Entry(text=0)
entry_box_name.place(x=180, y=20, width=100, height=25)
entry_box_name.focus()

button1 = Button(text='Check!', command=check)
button1.place(x=285, y=20, width=100, height=25)

button2 = Button(text='Again!', command=again)
button2.place(x=180, y=180, width=100, height=25)

window.mainloop()
