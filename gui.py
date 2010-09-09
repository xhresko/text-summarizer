from tkinter import *
from textutil import *

root = Tk()

fram = Frame(root)
Label(fram,text='Result percentage:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Summarize')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

summary = Text(root)
summary.insert('1.0','''''')
summary.pack(side=BOTTOM)
original = Text(root)
original.insert('1.0','''Vlozte text ...''')
original.pack(side=BOTTOM)

def summarize():
    if edit.get()=='' :
        percentage = 1
    else :
        percentage = int(edit.get())
    result = rate_sentences(original.get('1.0','end'), percentage)
    summary.delete('1.0','end')
    summary.insert('1.0',str(result))

butt.config(command=summarize)
root.mainloop()