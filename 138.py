from tkinter import *

ans = 1


def check():
    ans = entry_box_name.get()
    entry_box_name.delete(0, END)
    ph = '138_' + ans + '.gif'
    photo = PhotoImage(file=ph)
    photobox = Label(window, image=photo)
    photobox.image = photo
    photobox.place(x=130, y=60, width=200, height=120)
    return


window = Tk()
window.title('Window Title')
window.geometry('450x400')
window.wm_iconbitmap('132_icon.ico')

entry_box_name = Entry(text=0)
entry_box_name.place(x=50, y=20, width=100, height=25)
entry_box_name.focus()

button1 = Button(text='Check!', command=check)
button1.place(x=170, y=20, width=100, height=25)

window.mainloop()
