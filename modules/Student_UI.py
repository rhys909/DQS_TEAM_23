from tkinter import *

class Student_UI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("Student")
        s_exams = Label(self, text="Your summative exams:", font=("MS", 16, "bold")).grid(row=0, column=0, sticky=W)
        sumExams = [
            ("Exam1", 1),
            ("Exam2", 2),
            ("Exam3", 3),
            ("Exam4", 4),
            ("Exam5", 5),
        ]
        self.v1 = IntVar()
        position = 1
        
        for text, val in sumExams:
            b1 = Radiobutton(self, text=text, variable=self.v1, value=val)
            b1.grid(row=position, column=0, sticky=W)
            position += 1
            
        take1 = Button(self, text="Take")
        take1.grid(row=position, column=0, sticky=W)

        position += 1
        
        f_exams = Label(self, text="Your formative exams:", font=("MS", 16, "bold")).grid(row=position, column=0, sticky=W)
        
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
            
        take2 = Button(self, text="Take")
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
