from tkinter import *
from modules.Create_Exam import *
from modules.Take_Summative import *
from modules.Take_Formative import *
from modules.Statistics import *
from exams.exams import summativeExams
from exams.exams import formativeExams

class Lecturer_UI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        with open("modules/passInfo.txt", "r") as readInfo:
            self.username = readInfo.readlines()[0].rstrip("\n")
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("Lecturer")
        welcome = Label(self, text="Welcome, " + self.username + "!", font=("MS", 16, "bold")).grid(row=0, column=0, sticky=W)
        o_exams = Label(self, text="Your open exams:", font=("MS", 16, "bold")).grid(row=1, column=0, sticky=W)
        openExams = []
        for exam in summativeExams:
            openExams.append((summativeExams[exam][0], exam))
        for exam in formativeExams:
            openExams.append((formativeExams[exam][0], exam))
        self.v1 = IntVar()
        position = 2
        for text, val in openExams:
            b1 = Radiobutton(self, text=text, variable=self.v1, value=val)
            b1.grid(row=position, column=0, sticky=W)
            position += 1   

        modify = Button(self, text="modify")
        modify.grid(row=position, column=0, sticky=W)

        dele = Button(self, text="delete")
        dele.grid(row=position, column=1, sticky=W)

        position += 1
        f_exams = Label(self, text="Your closed exams:", font=("MS", 16, "bold")).grid(row=position, column=0, sticky=W)
        position += 1
        closedExams = []
        self.v2 = IntVar()
        position += 1
        for k in summativeExams:
            closedExams.append((summativeExams[k][0], k))
        for k in formativeExams:
            closedExams.append((formativeExams[k][0], k))
       
        for text, val in closedExams:
            b2 = Radiobutton(self, text=text,variable=self.v2, value=val)
            b2.grid(row=position, column=0, sticky=W)
            position += 1

        position += 1

        stats = Button(self, text="View statistics", command = self.view_statistics)
        stats.grid(row=position, column=0, sticky=W)


        createExam = Button(self, text="Create exam", command = self.create_new_exam)
        createExam.grid(row=position, column=1, sticky=W)

    def create_new_exam(self):
        t1 = Toplevel()
        Create_Exam(t1)

    def view_statistics(self):
        with open("modules/passInfo.txt", "a") as viewExam:
            viewExam.write("exams/" + formativeExams[self.v2.get()][1])

        t1 = Toplevel()
        Statistics(t1)
        t1.lift()
        t1.title(formativeExams[self.v2.get()][1])
        t1.attributes("-topmost", True)
        t1.resizable(False, False)

