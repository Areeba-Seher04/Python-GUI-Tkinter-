from tkinter import *

window=Tk()
window.configure(bg='grey56')

label1=Label(window,text='red text in times font',bg='pink',fg='red',font=('Times'))
label2=Label(window,text='green text in broadway font',bg='pink',fg='green',font=('Broadway'))
label3=Label(window,text='blue text in vardana font',bg='pink',fg='blue',font=('Vardana 32 bold italic'))

label4=Label(window,text='AREEBA',bg='pink',fg='red',font=('Times'))
label5=Label(window,text='AREEBA',bg='pink',fg='green',font=('Broadway'))
label6=Label(window,text='AREEBA',bg='pink',fg='blue',font=('Vardana 32 bold italic'))

label1.pack()
label2.pack()
label3.pack()

label6.pack()
label5.pack()
label4.pack()
window.mainloop()

