from tkinter import *

cal=Tk() #for making a window
cal.title('Calculator')

screen=Entry(cal,bd=20,justify='right',font=('aerial'))
screen.grid(row=0,columnspan=4) 

num='123456789'
i=0
button=[]
for j in range(1,4):
    for k in range(3):
        button.append(Button(cal,text=num[i],bg='white',bd=10,font=('aerial',20,'bold'),width=10,
               fg='black'))
        button[i].grid(row=j,column=k)
        i+=1

cal.mainloop()
