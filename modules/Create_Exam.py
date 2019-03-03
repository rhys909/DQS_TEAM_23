from tkinter import *

class Create_Exam(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()

    def init_window(self):
            self.master.title("New Test")
            lblStrAgr = Label(self, text = 'True', font=("MS", 16, "bold"))
            lblStrAgr.grid(row=3, column= 4, rowspan=2)
            lblStrAgr = Label(self, text = 'False', font=("MS", 16, "bold"))
            lblStrAgr.grid(row=3, column= 5, rowspan=2)


            self.varQ1 = IntVar()
            R1Q1 = Radiobutton(self, variable=self.varQ1, value=0)
            R1Q1.grid(row=5, column= 4)
            R2Q1 = Radiobutton(self, variable=self.varQ1, value=1)
            R2Q1.grid(row=5, column= 5)

root = Tk()
root.title("New Exam")
app = Create_Exam(root)
root.mainloop()
