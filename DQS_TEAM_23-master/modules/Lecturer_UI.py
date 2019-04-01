from tkinter import *
from modules.Create_Exam import *

class Lecturer_UI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("Lecturer")
        o_exams = Label(self, text="Your open exams:", font=("MS", 16, "bold")).grid(row=0, column=0, sticky=W)
        openExams = [
            ("Exam1", 1),
            ("Exam2", 2),
            ("Exam3", 3),
            ("Exam4", 4),
            ("Exam5", 5),
        ]
        self.v1 = IntVar()
        position = 1

        for text, val in openExams:
            b1 = Radiobutton(self, text=text, variable=self.v1, value=val)
            b1.grid(row=position, column=0, sticky=W)
            position += 1

        modify = Button(self, text="modify")
        modify.grid(row=position, column=0, sticky=W)

        dele = Button(self, text="delete")
        dele.grid(row=position, column=1, sticky=W)

        position += 1

        c_exams = Label(self, text="Your closed exams:", font=("MS", 16, "bold")).grid(row=position, column=0, sticky=W)

        position += 1

        self.v2 = IntVar()

        formExams = [
            ("Exam1", 1),
            ("Exam2", 2),
            ("Exam3", 3),
            ("Exam4", 4),

        ]
        for text, val in formExams:
            b2 = Radiobutton(self, text=text,variable=self.v2, value=val)
            b2.grid(row=position, column=0, sticky=W)

            position += 1

        stats = Button(self, text="View statistics")
        stats.grid(row=position, column=0, sticky=W)


        createExam = Button(self, text="Create exam", command = self.create_new_exam)
        createExam.grid(row=position, column=1, sticky=W)

    def create_new_exam(self):
            t1 = Toplevel()
            Create_Exam(t1)

