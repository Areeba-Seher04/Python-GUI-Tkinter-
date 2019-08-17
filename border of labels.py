from tkinter import *

window=Tk()
window.configure(bg='grey56')

label1=Label(window,text='red text in times font',bg='pink',fg='red',font=('Times'),relief='solid',bd=4)
label2=Label(window,text='green text in broadway font',bg='pink',fg='green',font=('Broadway'),relief='raised',bd=4)
label3=Label(window,text='blue text in vardana font',bg='pink',fg='blue',font=('Vardana 32 bold italic'),relief='sunken',bd=4)

label4=Label(window,text='AREEBA',bg='pink',fg='red',font=('Times'),relief='ridge',bd=4)
label5=Label(window,text='AREEBA',bg='pink',fg='green',font=('Broadway'),relief='groove',bd=4)
label6=Label(window,text='AREEBA',bg='pink',fg='blue',font=('Vardana 32 bold italic'),relief='flat',bd=4)

label1.pack()
label2.pack()
label3.pack()

label6.pack()
label5.pack()
label4.pack()
window.mainloop()
