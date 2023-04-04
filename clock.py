# We will make a clock that pops from a new window, so lets import the tkinter module for the window and the time module for the clock.
# I tried with different modules
from tkinter import *
# If I imported all (*) from tkinter, do I need to import ttk again?
from tkinter import ttk
from time import *

root = Tk()

# Lets put a name in the header
root.title("My Clock")

# Lets define time, its parameter %I for hours to be shown in 24 hour, %M for minutes, %S for seconds
def time():
  string = strftime('%I:%M:%S')
  lbl.config(text=string)
# Lets add a call function, so it updates every 1 second, or 1000 miliseconds
  lbl.after(1000, time)

#Gotta make it look cute, we can choose font, size, background color, and font color (foregoung). Colors can be by name or hex.
lbl = Label(root,
            font=('arial', 50),
            background='orange',
            foreground='white',)

lbl.pack(anchor='center')
time()
 
mainloop()

# Exercise failed
# Could not change the time zone :(
