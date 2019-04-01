import tkinter as tk
import time
def count_down():
    for t in range(120, -1, -1):
        sf = "{:02d}:{:02d}".format(*divmod(t, 60))
        time_str.set(sf)
        root.update()
        time.sleep(1)
root = tk.Tk()
time_str = tk.StringVar()
label_font = ('helvetica', 40)
tk.Label(root, textvariable=time_str, font=label_font, bg='white', 
         fg='blue', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)
tk.Button(root, text='Count Start', command=count_down).pack()
tk.Button(root, text='Count Stop', command=root.destroy).pack()
root.mainloop()
