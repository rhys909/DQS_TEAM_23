from tkinter import *

class New_Exam(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("New Exam")

root = Tk()
root.title("New Exam")
app = New_Exam(root)
root.mainloop()
