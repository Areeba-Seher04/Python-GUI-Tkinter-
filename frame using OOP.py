from tkinter import *

class MyFrame(Frame):
    def __init__(self,window,height=None,width=None,bg=None):
        super().__init__()
        self["height"]=height
        self["width"]=width
        self["bg"]=bg

class MyLabel(Label):
    def __init__(self,mylabel,height=None,width=None,bg=None,text=None,image=None):
        super().__init__()
        self["height"]=height
        self["width"]=width
        self["bg"]=bg
        self["text"]=text
        self["image"]=image

class MyButton(Button):
    def __init__(self,my,height=2,bd=3,width=7,image=None):
        super().__init__()
        self["image"]=image
        self["height"]=height
        self["width"]=width
        self["image"]=image
        

win = Tk()
frame = MyFrame(win,200,300,"red")
frame.grid(row=0,column=0)
frame2=MyFrame(win,200,300,"green")
frame2.grid(row=0,column=1)
label = MyLabel(frame,5,10,"white","hello world")
label.grid(row=0,column=0)
button1=MyButton(frame)
button2=MyButton(frame)
button3=MyButton(frame2)
button4=MyButton(frame2)


button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)
button4.grid(row=3,column=0)
win.mainloop()
