from tkinter import *

class Create_Exam(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()
#        commented out saveTest() until its functional
#        self.saveTest()

    def init_window(self):
        self.master.title("New Test")

        lblTstName = Label(self, text=" Enter the \n test name: ", font=('MS', 12,'bold'))
        lblTstName.grid(row=1, rowspan=2, column=0, columnspan=1, sticky=W)
        lblA = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lblA.grid(row=1,rowspan=2, column=7, sticky=E)
        lblB = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lblB.grid(row=1,rowspan=2, column=8, sticky=E)
        lblC = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lblC.grid(row=1,rowspan=2, column=9, sticky=E)
        lblD = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lblD.grid(row=1,rowspan=2, column=10, sticky=E)

        lblQ1 = Label(self, text=" Question 1: ", font=('MS', 8 , 'bold'))
        lblQ1.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ2 = Label(self, text=" Question 2: ", font=('MS', 8 , 'bold'))
        lblQ2.grid(row=6, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ3 = Label(self, text=" Question 3: ", font=('MS', 8 , 'bold'))
        lblQ3.grid(row=9, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ4 = Label(self, text=" Question 4: ", font=('MS', 8 , 'bold'))
        lblQ4.grid(row=12, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ5 = Label(self, text=" Question 5: ", font=('MS', 8 , 'bold'))
        lblQ5.grid(row=15, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ6 = Label(self, text=" Question 6: ", font=('MS', 8 , 'bold'))
        lblQ6.grid(row=18, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ7 = Label(self, text=" Question 7: ", font=('MS', 8 , 'bold'))
        lblQ7.grid(row=21, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ8 = Label(self, text=" Question 8: ", font=('MS', 8 , 'bold'))
        lblQ8.grid(row=24, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ9 = Label(self, text=" Question 9: ", font=('MS', 8 , 'bold'))
        lblQ9.grid(row=27, column=0, rowspan=3, columnspan=2, sticky=W)
        lblQ10 = Label(self, text=" Question 10: ", font=('MS', 8 , 'bold'))
        lblQ10.grid(row=30, column=0, rowspan=3, columnspan=2, sticky=W)

        self.entTestName =Entry(self)
        self.entTestName.grid(row=1, column=2, columnspan= 5, rowspan=1, sticky=W)
        self.entQ1 = Entry(self)
        self.entQ1.grid(row=3, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ2 = Entry(self)
        self.entQ2.grid(row=6, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ3 = Entry(self)
        self.entQ3.grid(row=9, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ4 = Entry(self)
        self.entQ4.grid(row=12, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ5 = Entry(self)
        self.entQ5.grid(row=15, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ6 = Entry(self)
        self.entQ6.grid(row=18, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ7 = Entry(self)
        self.entQ7.grid(row=21, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ8 = Entry(self)
        self.entQ8.grid(row=24, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ9 = Entry(self)
        self.entQ9.grid(row=27, column=2, columnspan= 5, rowspan=3, sticky=W)
        self.entQ10 = Entry(self)
        self.entQ10.grid(row=30, column=2, columnspan= 5, rowspan=3, sticky=W)

        self.varQ1 = IntVar()

        R1Q1 = Radiobutton(self, variable=self.varQ1, value=1)
        R1Q1.grid(row=3, column=7)
        R2Q1 = Radiobutton(self, variable=self.varQ1, value=2)
        R2Q1.grid(row=3, column=8)
        R3Q1 = Radiobutton(self, variable=self.varQ1, value=3)
        R3Q1.grid(row=3, column=9)
        R4Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R4Q1.grid(row=3, column=10)

        self.varQ2 = IntVar()

        R1Q2 = Radiobutton(self, variable=self.varQ2, value=1)
        R1Q2.grid(row=6, column=7)
        R2Q2 = Radiobutton(self, variable=self.varQ2, value=2)
        R2Q2.grid(row=6, column=8)
        R3Q2 = Radiobutton(self, variable=self.varQ2, value=3)
        R3Q2.grid(row=6, column=9)
        R4Q2 = Radiobutton(self, variable=self.varQ2, value=4)
        R4Q2.grid(row=6, column=10)

        self.varQ3 = IntVar()

        R1Q3 = Radiobutton(self, variable=self.varQ3, value=1)
        R1Q3.grid(row=9, column=7)
        R2Q3 = Radiobutton(self, variable=self.varQ3, value=2)
        R2Q3.grid(row=9, column=8)
        R3Q3 = Radiobutton(self, variable=self.varQ3, value=3)
        R3Q3.grid(row=9, column=9)
        R4Q3 = Radiobutton(self, variable=self.varQ3, value=4)
        R4Q3.grid(row=9, column=10)

        self.varQ4 = IntVar()

        R1Q4 = Radiobutton(self, variable=self.varQ4, value=1)
        R1Q4.grid(row=12, column=7)
        R2Q4 = Radiobutton(self, variable=self.varQ4, value=2)
        R2Q4.grid(row=12, column=8)
        R3Q4 = Radiobutton(self, variable=self.varQ4, value=3)
        R3Q4.grid(row=12, column=9)
        R4Q4 = Radiobutton(self, variable=self.varQ4, value=4)
        R4Q4.grid(row=12, column=10)

        self.varQ5 = IntVar()

        R1Q5 = Radiobutton(self, variable=self.varQ5, value=1)
        R1Q5.grid(row=15, column=7)
        R2Q5 = Radiobutton(self, variable=self.varQ5, value=2)
        R2Q5.grid(row=15, column=8)
        R3Q5 = Radiobutton(self, variable=self.varQ5, value=3)
        R3Q5.grid(row=15, column=9)
        R4Q5 = Radiobutton(self, variable=self.varQ5, value=4)
        R4Q5.grid(row=15, column=10)

        self.varQ6 = IntVar()

        R1Q6 = Radiobutton(self, variable=self.varQ6, value=1)
        R1Q6.grid(row=18, column=7)
        R2Q6 = Radiobutton(self, variable=self.varQ6, value=2)
        R2Q6.grid(row=18, column=8)
        R3Q6 = Radiobutton(self, variable=self.varQ6, value=3)
        R3Q6.grid(row=18, column=9)
        R4Q6 = Radiobutton(self, variable=self.varQ6, value=4)
        R4Q6.grid(row=18, column=10)

        self.varQ7 = IntVar()

        R1Q7 = Radiobutton(self, variable=self.varQ7, value=1)
        R1Q7.grid(row=21, column=7)
        R2Q7 = Radiobutton(self, variable=self.varQ7, value=2)
        R2Q7.grid(row=21, column=8)
        R3Q7 = Radiobutton(self, variable=self.varQ7, value=3)
        R3Q7.grid(row=21, column=9)
        R4Q7 = Radiobutton(self, variable=self.varQ7, value=4)
        R4Q7.grid(row=21, column=10)

        self.varQ8 = IntVar()

        R1Q8 = Radiobutton(self, variable=self.varQ8, value=1)
        R1Q8.grid(row=24, column=7)
        R2Q8 = Radiobutton(self, variable=self.varQ8, value=2)
        R2Q8.grid(row=24, column=8)
        R3Q8 = Radiobutton(self, variable=self.varQ8, value=3)
        R3Q8.grid(row=24, column=9)
        R4Q8 = Radiobutton(self, variable=self.varQ8, value=4)
        R4Q8.grid(row=24, column=10)

        self.varQ9 = IntVar()

        R1Q9 = Radiobutton(self, variable=self.varQ9, value=1)
        R1Q9.grid(row=27, column=7)
        R2Q9 = Radiobutton(self, variable=self.varQ9, value=2)
        R2Q9.grid(row=27, column=8)
        R3Q9 = Radiobutton(self, variable=self.varQ9, value=3)
        R3Q9.grid(row=27, column=9)
        R4Q9 = Radiobutton(self, variable=self.varQ9, value=4)
        R4Q9.grid(row=27, column=10)

        self.varQ10 = IntVar()

        R1Q10 = Radiobutton(self, variable=self.varQ10, value=1)
        R1Q10.grid(row=30, column=7)
        R2Q10 = Radiobutton(self, variable=self.varQ10, value=2)
        R2Q10.grid(row=30, column=8)
        R3Q10 = Radiobutton(self, variable=self.varQ10, value=3)
        R3Q10.grid(row=30, column=9)
        R4Q10 = Radiobutton(self, variable=self.varQ10, value=4)
        R4Q10.grid(row=30, column=10)
        #above is the code for the radio buttons and I have assigned A the value of 1 B=2 C=3 D=4
        #Further development can be added to give a variety of questions however for initial implementation
        #I was just sticking with the multiple choice of 10 questions

"""
    def saveTest(self):

        saveButton= Button(self, text='Save Test', font=('MS', 8, 'bold'))
        saveButton['command'] = self.storeTest
        saveButton.grid(row=32, sticky=SE)

    def storeTest(self):
"""
