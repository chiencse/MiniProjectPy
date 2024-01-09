import tkinter as tk
from tkinter import ttk
from plyer import notification

r = tk.Tk()
r.title('Notifications')

frm = tk.Frame(r)
tk.Label(frm, text = "Notifications on Laptop").pack()
frm.pack(pady= (20, 0))

fr2 = tk.Frame(r)
tk.Label(fr2, text = "Title Notifications: ").grid(row = 3, column= 0, sticky= 'W')
tk.Label(fr2, text = "Content Notifications: ").grid(row = 4, column = 0, sticky= 'W')
tk.Label(fr2, text = "time appears: ").grid(row = 5, column = 0, sticky='W')
t1 = tk.Entry(fr2)
t1.grid(row=3, column=1)

m = tk.Entry(fr2)
m.grid(row=4, column=1)

tm = tk.Entry(fr2)
tm.grid(row=5, column=1)

fr2.pack(padx=20, pady=10)

def start():
    a = int(tm.get())
    notification.notify(
        title=t1.get(),
        message=m.get(),
        timeout=a
    )

ttk.Button(r, text='Chạy', command=start).pack(pady=(0, 20))
r.mainloop()