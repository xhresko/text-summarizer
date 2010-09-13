from tkinter import *
from textutil import *

root = Tk()


root.title("Text Summarizer")
top_frame = Frame(root)
Label(top_frame,text='Size of summary in % :').pack(side=LEFT)
edit = Entry(top_frame)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(top_frame, text='Summarize')
butt.pack(side=RIGHT)
top_frame.pack(side=TOP)


center_frame = Frame(root)
center_frame.pack(side=TOP)
original = Text(center_frame)
original.insert('1.0','''Put some text here ...''')
original.pack(side=TOP)

summary = Text(center_frame)
summary.insert('1.0','''''')
summary.pack(side=BOTTOM)


def summarize():
    if edit.get()=='' :
        percentage = 1
    else :
        percentage = int(edit.get())

    orig_text = original.get('1.0','end')
    result = rate_sentences(orig_text, percentage)


    summary.delete('1.0','end')
    summary.insert('1.0',str(result))

butt.config(command=summarize)
root.mainloop()