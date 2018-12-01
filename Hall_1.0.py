from tkinter import *
import datetime
import calendar
import sys
import calendar;
import time;

if sys.version[0] == '2':
    import Tkinter as tk
else:
    import tkinter as tk

''' To find the screen resolution '''
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()


'''Opening a full screen window'''

root = Tk()

frame = tk.Frame(root)
frame.grid()


root.minsize(width=screen_width,height=screen_height)
labelfont = ('times', 20, 'bold')
widget = Label(frame, text='SKCET Event App')
widget.config(bg='white', fg='blue')
widget.config(width=200)
widget.config(height=100)
widget.config(font=labelfont)           
widget.config(height=15, width=85)       
widget.grid()#pack(expand=YES, fill=BOTH)

def reset():
    '''To delete all the widgets'''
    for child in frame.winfo_children():
        child.destroy()


button_book=Button(frame, text ="Book Now",bg='red',fg='white',font=('Helvetica', '50'),command=reset)
button_book.grid()#pack(expand=YES, fill=BOTH)


root.mainloop()
