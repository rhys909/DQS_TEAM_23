from tkinter import *
import csv

class Create_Exam(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()
#        commented out saveTest() until its functional
#        self.storeTest()
    def storeTest(self):
        testName = entTestName.get()

        Question1 = entQ1.get()
        Question2 = entQ2.get()
        Question3 = entQ3.get()
        Question4 = entQ4.get()
        Question5 = entQ5.get()
        Question6 = entQ6.get()
        Question7 = entQ7.get()
        Question8 = entQ8.get()
        Question9 = entQ9.get()
        Question10 = entQ10.get()

        ansQ1 = varQ1.get()
        if  ansQ1 == 1:
            Q1A = 1
            Q1B = 0
            Q1C = 0
            Q1D = 0
        elif  ansQ1 == 2:
            Q1A = 0
            Q1B = 1
            Q1C = 0
            Q1D = 0
        elif  ansQ1 == 3:
            Q1A = 0
            Q1B = 0
            Q1C = 1
            Q1D = 0
        elif  ansQ1 == 4:
            Q1A = 0
            Q1B = 0
            Q1C = 0
            Q1D = 1
        else:
            print("Error please put an answer to the question")

        ansQ2 = varQ2.get()
        if  ansQ2 == 1:
            Q2A = 1
            Q2B = 0
            Q2C = 0
            Q2D = 0
        elif  ansQ2 == 2:
            Q2A = 0
            Q2B = 1
            Q2C = 0
            Q2D = 0
        elif  ansQ2 == 3:
            Q2A = 0
            Q2B = 0
            Q2C = 1
            Q2D = 0
        elif  ansQ2 == 4:
            Q2A = 0
            Q2B = 0
            Q2C = 0
            Q2D = 1
        else:
            print("Error please put an answer to the question")

        ansQ3 = varQ3.get()
        if  ansQ3 == 1:
            Q3A = 1
            Q3B = 0
            Q3C = 0
            Q3D = 0
        elif  ansQ3 == 2:
            Q3A = 0
            Q3B = 1
            Q3C = 0
            Q3D = 0
        elif  ansQ3 == 3:
            Q3A = 0
            Q3B = 0
            Q3C = 1
            Q3D = 0
        elif  ansQ3 == 4:
            Q3A = 0
            Q3B = 0
            Q3C = 0
            Q3D = 1
        else:
            print("Error please put an answer to the question")

        ansQ4 = varQ4.get()
        if  ansQ4 == 1:
            Q4A = 1
            Q4B = 0
            Q4C = 0
            Q4D = 0
        elif  ansQ4 == 2:
            Q4A = 0
            Q4B = 1
            Q4C = 0
            Q4D = 0
        elif  ansQ4 == 3:
            Q4A = 0
            Q4B = 0
            Q4C = 1
            Q4D = 0
        elif  ansQ4 == 4:
            Q4A = 0
            Q4B = 0
            Q4C = 0
            Q4D = 1
        else:
            print("Error please put an answer to the question")

        ansQ5 = varQ5.get()
        if  ansQ5 == 1:
            Q5A = 1
            Q5B = 0
            Q5C = 0
            Q5D = 0
        elif  ansQ5 == 2:
            Q5A = 0
            Q5B = 1
            Q5C = 0
            Q5D = 0
        elif  ansQ5 == 3:
            Q5A = 0
            Q5B = 0
            Q5C = 1
            Q5D = 0
        elif  ansQ5 == 4:
            Q5A = 0
            Q5B = 0
            Q5C = 0
            Q5D = 1
        else:
            print("Error please put an answer to the question")

        ansQ6 = varQ6.get()
        if  ansQ6 == 1:
            Q6A = 1
            Q6B = 0
            Q6C = 0
            Q6D = 0
        elif  ansQ6 == 2:
            Q6A = 0
            Q6B = 1
            Q6C = 0
            Q6D = 0
        elif  ansQ6 == 3:
            Q6A = 0
            Q6B = 0
            Q6C = 1
            Q6D = 0
        elif  ansQ6 == 4:
            Q6A = 0
            Q6B = 0
            Q6C = 0
            Q6D = 1
        else:
            print("Error please put an answer to the question")

        ansQ7 = varQ7.get()
        if  ansQ7 == 1:
            Q7A = 1
            Q7B = 0
            Q7C = 0
            Q7D = 0
        elif  ansQ7 == 2:
            Q7A = 0
            Q7B = 1
            Q7C = 0
            Q7D = 0
        elif  ansQ7 == 3:
            Q7A = 0
            Q7B = 0
            Q7C = 1
            Q7D = 0
        elif  ansQ7 == 4:
            Q7A = 0
            Q7B = 0
            Q7C = 0
            Q7D = 1
        else:
            print("Error please put an answer to the question")

        ansQ8 = varQ8.get()
        if  ansQ8 == 1:
            Q8A = 1
            Q8B = 0
            Q8C = 0
            Q8D = 0
        elif  ansQ8 == 2:
            Q8A = 0
            Q8B = 1
            Q8C = 0
            Q8D = 0
        elif  ansQ8 == 3:
            Q8A = 0
            Q8B = 0
            Q8C = 1
            Q8D = 0
        elif  ansQ8 == 4:
            Q8A = 0
            Q8B = 0
            Q8C = 0
            Q8D = 1
        else:
            print("Error please put an answer to the question")

        ansQ9 = varQ9.get()
        if  ansQ9 == 1:
            Q9A = 1
            Q9B = 0
            Q9C = 0
            Q9D = 0
        elif  ansQ9 == 2:
            Q9A = 0
            Q9B = 1
            Q9C = 0
            Q9D = 0
        elif  ansQ9 == 3:
            Q9A = 0
            Q9B = 0
            Q9C = 1
            Q9D = 0
        elif  ansQ9 == 4:
            Q9A = 0
            Q9B = 0
            Q9C = 0
            Q9D = 1
        else:
            print("Error please put an answer to the question")

        ansQ10 = varQ10.get()
        if  ansQ10 == 1:
            Q10A = 1
            Q10B = 0
            Q10C = 0
            Q10D = 0
        elif  ansQ10 == 2:
            Q10A = 0
            Q10B = 1
            Q10C = 0
            Q10D = 0
        elif  ansQ10 == 3:
            Q10A = 0
            Q10B = 0
            Q10C = 1
            Q10D = 0
        elif  ansQ10 == 4:
            Q10A = 0
            Q10B = 0
            Q10C = 0
            Q10D = 1
        else:
            print("Error please put an answer to the question")

        with open(testName, 'w', newline = '') as f:
            dqs = csv.writer(f, delimeter='`')

            dqs.writerow([Question1 , Q1A, Q1B, Q1C, Q1D])
            dqs.writerow([Question2 , Q2A, Q2B, Q2C, Q2D])
            dqs.writerow([Question3 , Q3A, Q3B, Q3C, Q3D])
            dqs.writerow([Question4 , Q4A, Q4B, Q4C, Q4D])
            dqs.writerow([Question5 , Q5A, Q5B, Q5C, Q5D])
            dqs.writerow([Question6 , Q6A, Q6B, Q6C, Q6D])
            dqs.writerow([Question7 , Q7A, Q7B, Q7C, Q7D])
            dqs.writerow([Question8 , Q8A, Q8B, Q8C, Q8D])
            dqs.writerow([Question9 , Q9A, Q9B, Q9C, Q9D])
            dqs.writerow([Question10 , Q10A, Q10B, Q10C, Q10D])


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
        lblQ1.grid(row=3, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl1A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl1A.grid(row=4,rowspan=1, column=0, sticky=W)
        lbl1B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl1B.grid(row=5,rowspan=1, column=0, sticky=W)
        lbl1C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl1C.grid(row=6,rowspan=1, column=0, sticky=W)
        lbl1D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl1D.grid(row=7,rowspan=1, column=0, sticky=W)
        lblQ2 = Label(self, text=" Question 2: ", font=('MS', 8 , 'bold'))
        lblQ2.grid(row=8, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl2A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl2A.grid(row=9,rowspan=1, column=0, sticky=W)
        lbl2B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl2B.grid(row=10,rowspan=1, column=0, sticky=W)
        lbl2C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl2C.grid(row=11,rowspan=1, column=0, sticky=W)
        lbl2D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl2D.grid(row=12,rowspan=1, column=0, sticky=W)
        lblQ3 = Label(self, text=" Question 3: ", font=('MS', 8 , 'bold'))
        lblQ3.grid(row=13, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl3A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl3A.grid(row=14,rowspan=1, column=0, sticky=W)
        lbl3B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl3B.grid(row=15,rowspan=1, column=0, sticky=W)
        lbl3C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl3C.grid(row=16,rowspan=1, column=0, sticky=W)
        lbl3D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl3D.grid(row=17,rowspan=1, column=0, sticky=W)
        lblQ4 = Label(self, text=" Question 4: ", font=('MS', 8 , 'bold'))
        lblQ4.grid(row=18, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl4A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl4A.grid(row=19,rowspan=1, column=0, sticky=W)
        lbl4B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl4B.grid(row=20,rowspan=1, column=0, sticky=W)
        lbl4C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl4C.grid(row=21,rowspan=1, column=0, sticky=W)
        lbl4D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl4D.grid(row=22,rowspan=1, column=0, sticky=W)
        lblQ5 = Label(self, text=" Question 5: ", font=('MS', 8 , 'bold'))
        lblQ5.grid(row=23, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl5A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl5A.grid(row=24,rowspan=1, column=0, sticky=W)
        lbl5B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl5B.grid(row=25,rowspan=1, column=0, sticky=W)
        lbl5C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl5C.grid(row=26,rowspan=1, column=0, sticky=W)
        lbl5D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl5D.grid(row=27,rowspan=1, column=0, sticky=W)
        lblQ6 = Label(self, text=" Question 6: ", font=('MS', 8 , 'bold'))
        lblQ6.grid(row=28, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl6A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl6A.grid(row=29,rowspan=1, column=0, sticky=W)
        lbl6B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl6B.grid(row=30,rowspan=1, column=0, sticky=W)
        lbl6C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl6C.grid(row=31,rowspan=1, column=0, sticky=W)
        lbl6D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl6D.grid(row=32,rowspan=1, column=0, sticky=W)
        lblQ7 = Label(self, text=" Question 7: ", font=('MS', 8 , 'bold'))
        lblQ7.grid(row=33, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl7A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl7A.grid(row=34,rowspan=1, column=0, sticky=W)
        lbl7B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl7B.grid(row=35,rowspan=1, column=0, sticky=W)
        lbl7C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl7C.grid(row=36,rowspan=1, column=0, sticky=W)
        lbl7D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl7D.grid(row=37,rowspan=1, column=0, sticky=W)
        lblQ8 = Label(self, text=" Question 8: ", font=('MS', 8 , 'bold'))
        lblQ8.grid(row=38, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl8A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl8A.grid(row=39,rowspan=1, column=0, sticky=W)
        lbl8B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl8B.grid(row=40,rowspan=1, column=0, sticky=W)
        lbl8C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl8C.grid(row=41,rowspan=1, column=0, sticky=W)
        lbl8D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl8D.grid(row=42,rowspan=1, column=0, sticky=W)
        lblQ9 = Label(self, text=" Question 9: ", font=('MS', 8 , 'bold'))
        lblQ9.grid(row=43, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl9A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl9A.grid(row=44,rowspan=1, column=0, sticky=W)
        lbl9B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl9B.grid(row=45,rowspan=1, column=0, sticky=W)
        lbl9C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl9C.grid(row=46,rowspan=1, column=0, sticky=W)
        lbl9D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl9D.grid(row=47,rowspan=1, column=0, sticky=W)
        lblQ10 = Label(self, text=" Question 10: ", font=('MS', 8 , 'bold'))
        lblQ10.grid(row=48, column=0, rowspan=1, columnspan=2, sticky=W)
        lbl10A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl10A.grid(row=49,rowspan=1, column=0, sticky=W)
        lbl10B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl10B.grid(row=50,rowspan=1, column=0, sticky=W)
        lbl10C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl10C.grid(row=51,rowspan=1, column=0, sticky=W)
        lbl10D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl10D.grid(row=52,rowspan=1, column=0, sticky=W)

        self.entTestName =Entry(self)
        self.entTestName.grid(row=1, column=2, columnspan= 5, rowspan=1, sticky=W)
        self.entQ1 = Entry(self)
        self.entQ1.grid(row=3, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent1A = Entry(self)
        ent1A.grid(row=4,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent1B = Entry(self)
        ent1B.grid(row=5,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent1C = Entry(self)
        ent1C.grid(row=6,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent1D = Entry(self)
        ent1D.grid(row=7,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ2 = Entry(self)
        self.entQ2.grid(row=8, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent2A = Entry(self)
        ent2A.grid(row=9,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent2B = Entry(self)
        ent2B.grid(row=10,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent2C = Entry(self)
        ent2C.grid(row=11,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent2D = Entry(self)
        ent2D.grid(row=12,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ3 = Entry(self)
        self.entQ3.grid(row=13, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent3A = Entry(self)
        ent3A.grid(row=14,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent3B = Entry(self)
        ent3B.grid(row=15,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent3C = Entry(self)
        ent3C.grid(row=16,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent3D = Entry(self)
        ent3D.grid(row=17,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ4 = Entry(self)
        self.entQ4.grid(row=18, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent4A = Entry(self)
        ent4A.grid(row=19,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent4B = Entry(self)
        ent4B.grid(row=20,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent4C = Entry(self)
        ent4C.grid(row=21,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent4D = Entry(self)
        ent4D.grid(row=22,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ5 = Entry(self)
        self.entQ5.grid(row=23, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent5A = Entry(self)
        ent5A.grid(row=24,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent5B = Entry(self)
        ent5B.grid(row=25,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent5C = Entry(self)
        ent5C.grid(row=26,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent5D = Entry(self)
        ent5D.grid(row=27,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ6 = Entry(self)
        self.entQ6.grid(row=28, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent6A = Entry(self)
        ent6A.grid(row=29,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent6B = Entry(self)
        ent6B.grid(row=30,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent6C = Entry(self)
        ent6C.grid(row=31,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent6D = Entry(self)
        ent6D.grid(row=32,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ7 = Entry(self)
        self.entQ7.grid(row=33, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent7A = Entry(self)
        ent7A.grid(row=34,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent7B = Entry(self)
        ent7B.grid(row=35,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent7C = Entry(self)
        ent7C.grid(row=36,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent7D = Entry(self)
        ent7D.grid(row=37,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ8 = Entry(self)
        self.entQ8.grid(row=38, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent8A = Entry(self)
        ent8A.grid(row=39,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent8B = Entry(self)
        ent8B.grid(row=40,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent8C = Entry(self)
        ent8C.grid(row=41,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent8D = Entry(self)
        ent8D.grid(row=42,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ9 = Entry(self)
        self.entQ9.grid(row=43, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent9A = Entry(self)
        ent9A.grid(row=44,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent9B = Entry(self)
        ent9B.grid(row=45,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent9C = Entry(self)
        ent9C.grid(row=46,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent9D = Entry(self)
        ent9D.grid(row=47,rowspan=1, column=2, cloumnspan=5, sticky=W)
        self.entQ10 = Entry(self)
        self.entQ10.grid(row=48, column=2, columnspan= 5, rowspan=1, sticky=W)
        ent10A = Entry(self)
        ent10A.grid(row=49,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent10B = Entry(self)
        ent10B.grid(row=50,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent10C = Entry(self)
        ent10C.grid(row=51,rowspan=1, column=2, cloumnspan=5, sticky=W)
        ent10D = Entry(self)
        ent10D.grid(row=52,rowspan=1, column=2, cloumnspan=5, sticky=W)

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
        saveButton= Button(self, text='Save Test', font=('MS', 8, 'bold'))
        saveButton['command'] = self.storeTest
        saveButton.grid(row=32, sticky=SE)
