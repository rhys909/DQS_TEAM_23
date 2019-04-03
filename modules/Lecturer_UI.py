from tkinter import *
from modules.Create_Exam import *
from modules.Take_Summative import *
from modules.Take_Formative import *
from modules.Statistics import *
from modules.modify import *
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
        self.v1 = IntVar()
        position = 2
        with open("exams/list_of_exams.csv") as file:
            exams = list(csv.reader(file))
            for i in range(len(exams)):
                if exams[i][3] == "Summative":
                    b1 = Radiobutton(self, text=exams[i][0] + "\t" + "\t" + "\t" + "Summative", variable=self.v1, value=i)
                    b1.grid(row=position, column=0, sticky=W)
                    position += 1
                else:
                    b1 = Radiobutton(self, text=exams[i][0] + "\t" + "\t" + "\t" + "Formative", variable=self.v1, value=i)
                    b1.grid(row=position, column=0, sticky=W)
                    position += 1


        modify = Button(self, text="Modify exam", command=self.modify)
        modify.grid(row=position, column=0, sticky=W)
        dele = Button(self, text="Delete an exam")
        dele.grid(row=position, column=1, sticky=W)

        position += 1
        c_exams = Label(self, text="Your closed exams:", font=("MS", 16, "bold")).grid(row=position, column=0, sticky=W)
        position += 1
        self.v2 = IntVar()
        position += 1
       
        with open("exams/list_of_exams.csv") as file:
            exams = list(csv.reader(file))
            for i in range(len(exams)):
                if exams[i][3] == "Summative":
                    b2 = Radiobutton(self, text=exams[i][0] + "\t" + "\t" + "\t" + "Summative",variable=self.v2, value=i)
                    b2.grid(row=position, column=0, sticky=W)
                    position += 1
                else:
                    b2 = Radiobutton(self, text=exams[i][0] + "\t" + "\t" + "\t" + "Formative",variable=self.v2, value=i)
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
        ex = int(self.v2.get()) + 1
        try:
            with open("modules/passInfo.txt", "a") as viewExam:
                viewExam.write("exams/" + formativeExams[ex][1])

            t1 = Toplevel()
            Statistics(t1)
            t1.lift()
            t1.title(formativeExams[self.v2.get()][1])
            t1.attributes("-topmost", True)
            t1.resizable(False, False)
        except:
            with open("modules/passInfo.txt", "a") as viewExam:
                viewExam.write("exams/" + summativeExams[ex][1])

            t1 = Toplevel()
            Statistics(t1)
            t1.lift()
            t1.title(summativeExams[self.v2.get()][1])
            t1.attributes("-topmost", True)
            t1.resizable(False, False)

    def modify(self):
        ex = int(self.v1.get()) + 1
        try:
            with open("modules/passInfo.txt", "a") as modifyExam:
                modifyExam.write("exams/" + formativeExams[ex][1])

            t1 = Toplevel()
            modify(t1)
            t1.lift()
            t1.attributes("-topmost", True)
            t1.resizable(False, False)
        except:
            with open("modules/passInfo.txt", "a") as modifyExam:
                modifyExam.write("exams/" + summativeExams[ex][1])

            t1 = Toplevel()
            modify(t1)
            t1.lift()
            t1.attributes("-topmost", True)
            t1.resizable(False, False)
