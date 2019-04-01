from tkinter import *
from modules.Take_Summative import *
from modules.Take_Formative import *
from exams.exams import summativeExams
from exams.exams import formativeExams

class Student_UI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        with open("modules/passInfo.txt", "r") as readInfo:
            self.username = readInfo.readline()
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("Student")
        welcome = Label(self, text="Welcome, " + self.username + "!", font=("MS", 16, "bold")).grid(row=0, column=0, sticky=W)
        s_exams = Label(self, text="Your summative exams:", font=("MS", 16, "bold")).grid(row=1, column=0, sticky=W)
        sumExams = []
        for exam in summativeExams:
            sumExams.append((summativeExams[exam][0], exam))
        self.v1 = IntVar()
        position = 2
        for text, val in sumExams:
            b1 = Radiobutton(self, text=text, variable=self.v1, value=val)
            b1.grid(row=position, column=0, sticky=W)
            position += 1   
        take1 = Button(self, text="Take", command=self.takeSum)
        take1.grid(row=position, column=0, sticky=W)
        position += 1
        f_exams = Label(self, text="Your formative exams:", font=("MS", 16, "bold")).grid(row=position, column=0, sticky=W)
        position += 1
        formExams = []
        self.v2 = IntVar()
        position += 1
        for k in formativeExams:
            formExams.append((formativeExams[k][0], k))
       
        for k,v in formExams:
            b2 = Radiobutton(self, text=k,variable=self.v2, value=v)
            b2.grid(row=position, column=0, sticky=W)
            position += 1
        position += 1
        take2 = Button(self, text="Take", command=self.takeForm)
        take2.grid(row=position, column=0, sticky=W)
        position += 1
        r_marks = Label(self, text="Your returned marks:", font=("MS", 16, "bold")).grid(row=position, column=0, sticky=W)
        position += 1
        self.v3 = IntVar()
        retExams = [
            ("Exam1", 1),
            ("Exam2", 2),
            ("Exam3", 3),
    
        ]
        for text, val in retExams:
            b2 = Radiobutton(self, text=text, variable=self.v3, value=val)
            b2.grid(row=position, column=0, sticky=W)
            
            position += 1
        
        view = Button(self, text="View")
        view.grid(row=position, column=0, sticky=W)

    def takeSum(self):
        with open("modules/passInfo.txt", "a") as passExam:
            passExam.write("exams/" + summativeExams[self.v1.get()][1])

        t1 = Toplevel()
        Take_Summative(t1)
        t1.lift()
        t1.title(summativeExams[self.v1.get()][0])
        t1.attributes("-topmost", True)
        t1.resizable(False, False)
    def takeForm(self): 
        with open("modules/passInfo.txt", "a") as passExam:
            passExam.write("exams/" + summativeExams[self.v2.get()][1])
        try:
            t2 = Toplevel()
            Take_Formative(t2)
            t2.lift()
            t2.title(formativeExams[self.v2.get()][0])
            t2.attributes("-topmost", True)
            t2.resizable(False, False)
        
        except:
            messagebox.showwarning("Invalid Action", "You already have an active exam")
        
