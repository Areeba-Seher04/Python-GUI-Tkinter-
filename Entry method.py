from tkinter import *

def say_hello():
##    name_of_user = var_2.get()
##    var_1.set('Hello ' + name_of_user)
    var_1.set('Hello '+ var_2.get())
  
        
window=Tk()
var_1=StringVar()
var_2=StringVar()

label_1=Label(window,text="Please enter your name",pady=10)
entry_1=Entry(window,font='aerial 23',textvariable=var_2)
button_1=Button(window,text='Click here to see name',command=say_hello,pady=10)
label_2=Label(window,textvariable=var_1,pady=10)

label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
button_1.grid(row=1,column=0)
label_2.grid(row=1,column=1)

window.mainloop()
