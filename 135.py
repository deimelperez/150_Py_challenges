from tkinter import *


def change_color():
    color = select_color.get()
    window.configure(background=color)
    return


window = Tk()
window.title('Window Title')
window.geometry('450x400')

select_color = StringVar(window)
select_color.set('Select Color')
colorList = OptionMenu(window, select_color, 'blue', 'red', 'black', 'white')
colorList.place(x=30, y=20, width=100, height=25)

button1 = Button(text='Change color', command=change_color)
button1.place(x=150, y=20, width=100, height=25)

window.mainloop()
