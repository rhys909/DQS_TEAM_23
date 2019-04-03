from tkinter import *
import tkinter.messagebox as tkm
from modules.Take_Summative import *
from modules.Take_Formative import *
from exams.exams import summativeExams
from exams.exams import formativeExams

class Student_UI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        with open("modules/passInfo.txt", "r") as readInfo:
            self.username = readInfo.readlines()[0].rstrip("\n")
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
        for form in formativeExams:
            formExams.append((formativeExams[form][0], form))
        for text, val in formExams:
            b2 = Radiobutton(self, text=text,variable=self.v2, value=val)
            b2.grid(row=position, column=0, sticky=W)
            position += 1
        position += 1
        take2 = Button(self, text="Take", command=self.takeForm)
        take2.grid(row=position, column=0, sticky=W)
        position += 1
        r_marks = Label(self, text="Your returned marks:", font=("MS", 16, "bold")).grid(row=position, column=0, sticky=W)
        position += 1
        self.v3 = StringVar()
        with open("exams/stored_results.csv") as stored_results:
            results = list(csv.reader(stored_results))
        for j in results:
            b3 = Radiobutton(self, text=j[0], variable=self.v3, value=j[1])
            b3.grid(row=position, column=0, sticky=W)
            position += 1
        view = Button(self, text="View", command=self.Returned)
        view.grid(row=position, column=0, sticky=W)

    def takeSum(self):
        with open("modules/passInfo.txt", "a") as passExam:
            passExam.write("exams/" + summativeExams[self.v1.get()][1])
        with open("exams/list_of_exams.csv") as check:
            read = list(csv.reader(check))
            for row in read:
                if summativeExams[self.v1.get()][1] == row[1]:
                    if self.username in row[2]:
                        tkm.showwarning("Invalid Action", "You have already taken this exam")
                    else:
                        t1 = Toplevel()
                        Take_Summative(t1)
                        t1.lift()
                        t1.title(summativeExams[self.v1.get()][0])
                        t1.attributes("-topmost", True)
                        t1.resizable(False, False)
    def takeForm(self):
        with open("modules/passInfo.txt", "a") as passExam:
            passExam.write("exams/" + formativeExams[self.v2.get()][1])
        
        try:
            t2 = Toplevel()
            Take_Formative(t2)
            t2.lift()
            t2.title(formativeExams[self.v2.get()][0])
            t2.attributes("-topmost", True)
            t2.resizable(False, False)
        
        except:
            messagebox.showwarning("Invalid Action", "You already have an active exam")
        
    def Returned(self):
        sa=[]
        student_answer = []
        button_dir = self.v3.get()
        count = 0
        correct_answer_student = []
        wrong_answer_student = []
        with open("exams/stored_results.csv") as check:
            read = list(csv.reader(check))
            for k in read:
                yt = []
                yt.append(k[3])
                yt.append(k[1])
                student_answer.append(yt)
        with open(button_dir) as right_answers_file:
            r1 = list(csv.reader(right_answers_file))
            right_answers = r1[10]
            for g in student_answer:
                if button_dir == g[1]:
                    answers_student = g[0].split("'")
                    for i in range(len(answers_student)):
                        if answers_student[i] != right_answers[i]:
                            wrong_answer_student.append(i+1)
                        else:
                            correct_answer_student.append(i+1)
                            count +=1
                    print(wrong_answer_student)
                    print(right_answers)
                    for v in wrong_answer_student:
                        tkinter.messagebox.showinfo("Short feedback"," Question: " + str(v) + " Right answer: " + str(right_answers[v-1]))
                    tkinter.messagebox.showinfo("Short feedback","You got " + str(len(correct_answer_student)) + " out of " + str(len(right_answers)))
