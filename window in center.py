from tkinter import *

window=Tk()

window_width=200        #size of window we want to form
window_height=300

screen_width=window.winfo_screenwidth()      #size of computer window
screen_height=window.winfo_screenheight()

width=(screen_width/2)-(window_width/2)     #for center
height=(screen_height/2)-(window_height/2)

window.geometry('%dx%d+%d+%d' % (window_width,window_height,width,height)) #format method

window.mainloop()

