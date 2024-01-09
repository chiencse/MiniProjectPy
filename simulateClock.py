from tkinter import *
from time import *

def updateTime():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text = time_string)
    day_string = strftime("%A")
    day_label.config(text = day_string)
    date_string = strftime("%d %B %Y")
    date_label.config(text = date_string)
    time_label.after(1000, updateTime)

window = Tk()
window.title('Time')
time_label = Label(window, font =('Arial', 50), fg = 'white', background= 'black')
time_label.pack()
day_label = Label(window, font =('Arial',20), fg = 'white', background= 'black')
day_label.pack()
date_label = Label(window, font =('Arial',20))
date_label.pack()
updateTime()

window.mainloop()
