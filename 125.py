from tkinter import *
import random


def click():
    num = random.randint(1, 6)
    output_box['text'] = str(num)
    return


window = Tk()
window.title('Window Title')
window.geometry('200x200')
button1 = Button(text='Click to roll', command=click)
button1.place(x=65, y=50)
output_box = Message(text='')
output_box.place(x=65, y=80)
window.mainloop()
