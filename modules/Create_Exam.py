from tkinter import *
import tkinter.messagebox as tkm
from exams.exams import summativeExams
from exams.exams import formativeExams
import csv

class Create_Exam(Frame):

    # hello
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_window()
#        commented out saveTest() until its functional
#        self.storeTest()
    def storeTest(self):
        if self.entTestName.get() != "":
            testName = self.entTestName.get()

            TstFormSumm = self.FormOrSumm.get()
            if TstFormSumm == 0:
                TestType = "Formative"
            else:
                TestType = "Summative"

            Question1 = self.entQ1.get()
            Question2 = self.entQ2.get()
            Question3 = self.entQ3.get()
            Question4 = self.entQ4.get()
            Question5 = self.entQ5.get()
            Question6 = self.entQ6.get()
            Question7 = self.entQ7.get()
            Question8 = self.entQ8.get()
            Question9 = self.entQ9.get()
            Question10 = self.entQ10.get()

            ansQ1 = self.varQ1.get()
            ansQ2 = self.varQ2.get()
            ansQ3 = self.varQ3.get()
            ansQ4 = self.varQ4.get()
            ansQ5 = self.varQ5.get()
            ansQ6 = self.varQ6.get()
            ansQ7 = self.varQ7.get()
            ansQ8 = self.varQ8.get()
            ansQ9 = self.varQ9.get()
            ansQ10 = self.varQ10.get()

            Q1A = self.ent1A.get()
            Q1B = self.ent1B.get()
            Q1C = self.ent1C.get()
            Q1D = self.ent1D.get()

            Q2A = self.ent2A.get()
            Q2B = self.ent2B.get()
            Q2C = self.ent2C.get()
            Q2D = self.ent2D.get()

            Q3A = self.ent3A.get()
            Q3B = self.ent3B.get()
            Q3C = self.ent3C.get()
            Q3D = self.ent3D.get()

            Q4A = self.ent4A.get()
            Q4B = self.ent4B.get()
            Q4C = self.ent4C.get()
            Q4D = self.ent4D.get()

            Q5A = self.ent5A.get()
            Q5B = self.ent5B.get()
            Q5C = self.ent5C.get()
            Q5D = self.ent5D.get()

            Q6A = self.ent6A.get()
            Q6B = self.ent6B.get()
            Q6C = self.ent6C.get()
            Q6D = self.ent6D.get()

            Q7A = self.ent7A.get()
            Q7B = self.ent7B.get()
            Q7C = self.ent7C.get()
            Q7D = self.ent7D.get()

            Q8A = self.ent8A.get()
            Q8B = self.ent8B.get()
            Q8C = self.ent8C.get()
            Q8D = self.ent8D.get()

            Q9A = self.ent9A.get()
            Q9B = self.ent9B.get()
            Q9C = self.ent9C.get()
            Q9D = self.ent9D.get()

            Q10A = self.ent10A.get()
            Q10B = self.ent10B.get()
            Q10C = self.ent10C.get()
            Q10D = self.ent10D.get()

            if ansQ1 == 0:
                tkm.showwarning("Invalid Input", "Question 1 has not had an answer selected")
            elif ansQ2 == 0:
                tkm.showwarning("Invalid Input", "Question 2 has not had an answer selected")
            elif ansQ3 == 0:
                tkm.showwarning("Invalid Input", "Question 3 has not had an answer selected")
            elif ansQ4 == 0:
                tkm.showwarning("Invalid Input", "Question 4 has not had an answer selected")
            elif ansQ5 == 0:
                tkm.showwarning("Invalid Input", "Question 5 has not had an answer selected")
            elif ansQ6 == 0:
                tkm.showwarning("Invalid Input", "Question 6 has not had an answer selected")
            elif ansQ7 == 0:
                tkm.showwarning("Invalid Input", "Question 7 has not had an answer selected")
            elif ansQ8 == 0:
                tkm.showwarning("Invalid Input", "Question 8 has not had an answer selected")
            elif ansQ9 == 0:
                tkm.showwarning("Invalid Input", "Question 9 has not had an answer selected")
            elif ansQ10 == 0:
                tkm.showwarning("Invalid Input", "Question 10 has not had an answer selected")

            else:
                c = "Closed"
                answers = [ansQ1,ansQ2,ansQ3,ansQ4,ansQ5,ansQ6,ansQ7,ansQ8,ansQ9,ansQ10]
                with open("exams/list_of_exams.csv", "a") as file:
                    code = len(summativeExams)+len(formativeExams)+1
                    name = "exam"+str(code)+".csv"
                    file.write(f"{testName},{name},,{TestType},{c}\n")

                with open(("exams/"+name), 'w') as f:
                    ans = Q1A+"`"+Q1B+"`"+Q1C+"`"+Q1D
                    f.write(Question1+","+ans+"\n")
                    ans = Q2A+"`"+Q2B+"`"+Q2C+"`"+Q2D
                    f.write(Question2+","+ans+"\n")
                    ans = Q3A+"`"+Q3B+"`"+Q3C+"`"+Q3D
                    f.write(Question3+","+ans+"\n")
                    ans = Q4A+"`"+Q4B+"`"+Q4C+"`"+Q4D
                    f.write(Question4+","+ans+"\n")
                    ans = Q5A+"`"+Q5B+"`"+Q5C+"`"+Q5D
                    f.write(Question5+","+ans+"\n")
                    ans = Q6A+"`"+Q6B+"`"+Q6C+"`"+Q6D
                    f.write(Question6+","+ans+"\n")
                    ans = Q7A+"`"+Q7B+"`"+Q7C+"`"+Q7D
                    f.write(Question7+","+ans+"\n")
                    ans = Q8A+"`"+Q8B+"`"+Q8C+"`"+Q8D
                    f.write(Question8+","+ans+"\n")
                    ans = Q9A+"`"+Q9B+"`"+Q9C+"`"+Q9D
                    f.write(Question9+","+ans+"\n")
                    ans = Q10A+"`"+Q10B+"`"+Q10C+"`"+Q10D
                    f.write(Question10+","+ans+"\n")
                    for i in range(10):
                        if i != 9:
                            f.write(str(answers[i])+",")
                        else:
                            f.write(str(answers[i])+"\n")


                tkm.showinfo("Action Complete", "Exam Created")



        else:
            tkm.showwarning("Invalid Input", "You have not named your test")


    def init_window(self):
        self.master.title("New Test")

        lblTstName = Label(self, text=" Enter the \n test name: ", font=('MS', 12,'bold'))
        lblTstName.grid(row=1, rowspan=1, column=0, columnspan=1, sticky=W)
        lblFormative = Label(self, text=" Formative \n Assesment: ", font=('MS', 8, 'bold'))
        lblFormative.grid(row=2, rowspan=1, column=0, columnspan=1, sticky=W)
        lblSummative = Label(self, text=" Summative \n Assesment: ", font=('MS', 8, 'bold'))
        lblSummative.grid(row=2, rowspan=1, column=2, columnspan=1, sticky=W)
        lblA = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lblA.grid(row=1,rowspan=2, column=7, sticky=E)
        lblB = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lblB.grid(row=1,rowspan=2, column=8, sticky=E)
        lblC = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lblC.grid(row=1,rowspan=2, column=9, sticky=E)
        lblD = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lblD.grid(row=1,rowspan=2, column=10, sticky=E)

        lblA2 = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lblA2.grid(row=1,rowspan=2, column=18, sticky=E)
        lblB2 = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lblB2.grid(row=1,rowspan=2, column=19, sticky=E)
        lblC2 = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lblC2.grid(row=1,rowspan=2, column=20, sticky=E)
        lblD2 = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lblD2.grid(row=1,rowspan=2, column=21, sticky=E)

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
        lblQ6.grid(row=3, column=11, rowspan=1, columnspan=2, sticky=W)
        lbl6A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl6A.grid(row=4,rowspan=1, column=11, sticky=W)
        lbl6B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl6B.grid(row=5,rowspan=1, column=11, sticky=W)
        lbl6C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl6C.grid(row=6,rowspan=1, column=11, sticky=W)
        lbl6D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl6D.grid(row=7,rowspan=1, column=11, sticky=W)
        lblQ7 = Label(self, text=" Question 7: ", font=('MS', 8 , 'bold'))
        lblQ7.grid(row=8, column=11, rowspan=1, columnspan=2, sticky=W)
        lbl7A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl7A.grid(row=9,rowspan=1, column=11, sticky=W)
        lbl7B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl7B.grid(row=10,rowspan=1, column=11, sticky=W)
        lbl7C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl7C.grid(row=11,rowspan=1, column=11, sticky=W)
        lbl7D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl7D.grid(row=12,rowspan=1, column=11, sticky=W)
        lblQ8 = Label(self, text=" Question 8: ", font=('MS', 8 , 'bold'))
        lblQ8.grid(row=13, column=11, rowspan=1, columnspan=2, sticky=W)
        lbl8A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl8A.grid(row=14,rowspan=1, column=11, sticky=W)
        lbl8B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl8B.grid(row=15,rowspan=1, column=11, sticky=W)
        lbl8C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl8C.grid(row=16,rowspan=1, column=11, sticky=W)
        lbl8D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl8D.grid(row=17,rowspan=1, column=11, sticky=W)
        lblQ9 = Label(self, text=" Question 9: ", font=('MS', 8 , 'bold'))
        lblQ9.grid(row=18, column=11, rowspan=1, columnspan=2, sticky=W)
        lbl9A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl9A.grid(row=19,rowspan=1, column=11, sticky=W)
        lbl9B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl9B.grid(row=20,rowspan=1, column=11, sticky=W)
        lbl9C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl9C.grid(row=21,rowspan=1, column=11, sticky=W)
        lbl9D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl9D.grid(row=22,rowspan=1, column=11, sticky=W)
        lblQ10 = Label(self, text=" Question 10: ", font=('MS', 8 , 'bold'))
        lblQ10.grid(row=23, column=11, rowspan=1, columnspan=2, sticky=W)
        lbl10A = Label(self, text=" A)", font=('MS', 8, 'bold'))
        lbl10A.grid(row=24,rowspan=1, column=11, sticky=W)
        lbl10B = Label(self, text=" B)", font=('MS', 8, 'bold'))
        lbl10B.grid(row=25,rowspan=1, column=11, sticky=W)
        lbl10C = Label(self, text=" C)", font=('MS', 8, 'bold'))
        lbl10C.grid(row=26,rowspan=1, column=11, sticky=W)
        lbl10D = Label(self, text=" D)", font=('MS', 8, 'bold'))
        lbl10D.grid(row=27,rowspan=1, column=11, sticky=W)

        self.entTestName = Entry(self)
        self.entTestName.grid(row=1, column=2, columnspan= 5, rowspan=1, sticky=W)

        self.FormOrSumm = IntVar()
        FormativeRadio = Radiobutton(self, variable=self.FormOrSumm, value=0)
        FormativeRadio.grid(row=2, column=1, rowspan=1, columnspan=1, sticky=W)
        SummativeRadio = Radiobutton(self, variable=self.FormOrSumm, value=1)
        SummativeRadio.grid(row=2, column=3, rowspan=1, columnspan=1, sticky=W)

        self.entQ1 = Entry(self)
        self.entQ1.grid(row=3, column=2, columnspan= 5, rowspan=1, sticky=W)
        self.ent1A = Entry(self)
        self.ent1A.grid(row=4,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent1B = Entry(self)
        self.ent1B.grid(row=5,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent1C = Entry(self)
        self.ent1C.grid(row=6,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent1D = Entry(self)
        self.ent1D.grid(row=7,rowspan=1, column=2, columnspan=5, sticky=W)
        self.entQ2 = Entry(self)
        self.entQ2.grid(row=8, column=2, columnspan= 5, rowspan=1, sticky=W)
        self.ent2A = Entry(self)
        self.ent2A.grid(row=9,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent2B = Entry(self)
        self.ent2B.grid(row=10,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent2C = Entry(self)
        self.ent2C.grid(row=11,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent2D = Entry(self)
        self.ent2D.grid(row=12,rowspan=1, column=2, columnspan=5, sticky=W)
        self.entQ3 = Entry(self)
        self.entQ3.grid(row=13, column=2, columnspan= 5, rowspan=1, sticky=W)
        self.ent3A = Entry(self)
        self.ent3A.grid(row=14,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent3B = Entry(self)
        self.ent3B.grid(row=15,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent3C = Entry(self)
        self.ent3C.grid(row=16,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent3D = Entry(self)
        self.ent3D.grid(row=17,rowspan=1, column=2, columnspan=5, sticky=W)
        self.entQ4 = Entry(self)
        self.entQ4.grid(row=18, column=2, columnspan= 5, rowspan=1, sticky=W)
        self.ent4A = Entry(self)
        self.ent4A.grid(row=19,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent4B = Entry(self)
        self.ent4B.grid(row=20,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent4C = Entry(self)
        self.ent4C.grid(row=21,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent4D = Entry(self)
        self.ent4D.grid(row=22,rowspan=1, column=2, columnspan=5, sticky=W)
        self.entQ5 = Entry(self)
        self.entQ5.grid(row=23, column=2, columnspan= 5, rowspan=1, sticky=W)
        self.ent5A = Entry(self)
        self.ent5A.grid(row=24,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent5B = Entry(self)
        self.ent5B.grid(row=25,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent5C = Entry(self)
        self.ent5C.grid(row=26,rowspan=1, column=2, columnspan=5, sticky=W)
        self.ent5D = Entry(self)
        self.ent5D.grid(row=27,rowspan=1, column=2, columnspan=5, sticky=W)
        self.entQ6 = Entry(self)
        self.entQ6.grid(row=3, column=13, columnspan= 5, rowspan=1, sticky=W)
        self.ent6A = Entry(self)
        self.ent6A.grid(row=4,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent6B = Entry(self)
        self.ent6B.grid(row=5,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent6C = Entry(self)
        self.ent6C.grid(row=6,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent6D = Entry(self)
        self.ent6D.grid(row=7,rowspan=1, column=13, columnspan=5, sticky=W)
        self.entQ7 = Entry(self)
        self.entQ7.grid(row=8, column=13, columnspan= 5, rowspan=1, sticky=W)
        self.ent7A = Entry(self)
        self.ent7A.grid(row=9,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent7B = Entry(self)
        self.ent7B.grid(row=10,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent7C = Entry(self)
        self.ent7C.grid(row=11,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent7D = Entry(self)
        self.ent7D.grid(row=12,rowspan=1, column=13, columnspan=5, sticky=W)
        self.entQ8 = Entry(self)
        self.entQ8.grid(row=13, column=13, columnspan= 5, rowspan=1, sticky=W)
        self.ent8A = Entry(self)
        self.ent8A.grid(row=14,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent8B = Entry(self)
        self.ent8B.grid(row=15,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent8C = Entry(self)
        self.ent8C.grid(row=16,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent8D = Entry(self)
        self.ent8D.grid(row=17,rowspan=1, column=13, columnspan=5, sticky=W)
        self.entQ9 = Entry(self)
        self.entQ9.grid(row=18, column=13, columnspan= 5, rowspan=1, sticky=W)
        self.ent9A = Entry(self)
        self.ent9A.grid(row=19,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent9B = Entry(self)
        self.ent9B.grid(row=20,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent9C = Entry(self)
        self.ent9C.grid(row=21,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent9D = Entry(self)
        self.ent9D.grid(row=22,rowspan=1, column=13, columnspan=5, sticky=W)
        self.entQ10 = Entry(self)
        self.entQ10.grid(row=23, column=13, columnspan= 5, rowspan=1, sticky=W)
        self.ent10A = Entry(self)
        self.ent10A.grid(row=24,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent10B = Entry(self)
        self.ent10B.grid(row=25,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent10C = Entry(self)
        self.ent10C.grid(row=26,rowspan=1, column=13, columnspan=5, sticky=W)
        self.ent10D = Entry(self)
        self.ent10D.grid(row=27,rowspan=1, column=13, columnspan=5, sticky=W)

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
        R1Q2.grid(row=8, column=7)
        R2Q2 = Radiobutton(self, variable=self.varQ2, value=2)
        R2Q2.grid(row=8, column=8)
        R3Q2 = Radiobutton(self, variable=self.varQ2, value=3)
        R3Q2.grid(row=8, column=9)
        R4Q2 = Radiobutton(self, variable=self.varQ2, value=4)
        R4Q2.grid(row=8, column=10)

        self.varQ3 = IntVar()

        R1Q3 = Radiobutton(self, variable=self.varQ3, value=1)
        R1Q3.grid(row=13, column=7)
        R2Q3 = Radiobutton(self, variable=self.varQ3, value=2)
        R2Q3.grid(row=13, column=8)
        R3Q3 = Radiobutton(self, variable=self.varQ3, value=3)
        R3Q3.grid(row=13, column=9)
        R4Q3 = Radiobutton(self, variable=self.varQ3, value=4)
        R4Q3.grid(row=13, column=10)

        self.varQ4 = IntVar()

        R1Q4 = Radiobutton(self, variable=self.varQ4, value=1)
        R1Q4.grid(row=18, column=7)
        R2Q4 = Radiobutton(self, variable=self.varQ4, value=2)
        R2Q4.grid(row=18, column=8)
        R3Q4 = Radiobutton(self, variable=self.varQ4, value=3)
        R3Q4.grid(row=18, column=9)
        R4Q4 = Radiobutton(self, variable=self.varQ4, value=4)
        R4Q4.grid(row=18, column=10)

        self.varQ5 = IntVar()

        R1Q5 = Radiobutton(self, variable=self.varQ5, value=1)
        R1Q5.grid(row=23, column=7)
        R2Q5 = Radiobutton(self, variable=self.varQ5, value=2)
        R2Q5.grid(row=23, column=8)
        R3Q5 = Radiobutton(self, variable=self.varQ5, value=3)
        R3Q5.grid(row=23, column=9)
        R4Q5 = Radiobutton(self, variable=self.varQ5, value=4)
        R4Q5.grid(row=23, column=10)

        self.varQ6 = IntVar()

        R1Q6 = Radiobutton(self, variable=self.varQ6, value=1)
        R1Q6.grid(row=3, column=18)
        R2Q6 = Radiobutton(self, variable=self.varQ6, value=2)
        R2Q6.grid(row=3, column=19)
        R3Q6 = Radiobutton(self, variable=self.varQ6, value=3)
        R3Q6.grid(row=3, column=20)
        R4Q6 = Radiobutton(self, variable=self.varQ6, value=4)
        R4Q6.grid(row=3, column=21)

        self.varQ7 = IntVar()

        R1Q7 = Radiobutton(self, variable=self.varQ7, value=1)
        R1Q7.grid(row=8, column=18)
        R2Q7 = Radiobutton(self, variable=self.varQ7, value=2)
        R2Q7.grid(row=8, column=19)
        R3Q7 = Radiobutton(self, variable=self.varQ7, value=3)
        R3Q7.grid(row=8, column=20)
        R4Q7 = Radiobutton(self, variable=self.varQ7, value=4)
        R4Q7.grid(row=8, column=21)

        self.varQ8 = IntVar()

        R1Q8 = Radiobutton(self, variable=self.varQ8, value=1)
        R1Q8.grid(row=13, column=18)
        R2Q8 = Radiobutton(self, variable=self.varQ8, value=2)
        R2Q8.grid(row=13, column=19)
        R3Q8 = Radiobutton(self, variable=self.varQ8, value=3)
        R3Q8.grid(row=13, column=20)
        R4Q8 = Radiobutton(self, variable=self.varQ8, value=4)
        R4Q8.grid(row=13, column=21)

        self.varQ9 = IntVar()

        R1Q9 = Radiobutton(self, variable=self.varQ9, value=1)
        R1Q9.grid(row=18, column=18)
        R2Q9 = Radiobutton(self, variable=self.varQ9, value=2)
        R2Q9.grid(row=18, column=19)
        R3Q9 = Radiobutton(self, variable=self.varQ9, value=3)
        R3Q9.grid(row=18, column=20)
        R4Q9 = Radiobutton(self, variable=self.varQ9, value=4)
        R4Q9.grid(row=18, column=21)

        self.varQ10 = IntVar()

        R1Q10 = Radiobutton(self, variable=self.varQ10, value=1)
        R1Q10.grid(row=23, column=18)
        R2Q10 = Radiobutton(self, variable=self.varQ10, value=2)
        R2Q10.grid(row=23, column=19)
        R3Q10 = Radiobutton(self, variable=self.varQ10, value=3)
        R3Q10.grid(row=23, column=20)
        R4Q10 = Radiobutton(self, variable=self.varQ10, value=4)
        R4Q10.grid(row=23, column=21)
        #above is the code for the radio buttons and I have assigned A the value of 1 B=2 C=3 D=4
        #Further development can be added to give a variety of questions however for initial implementation
        #I was just sticking with the multiple choice of 10 questions
        saveButton= Button(self, text='Save Test', font=('MS', 8, 'bold'))
        saveButton['command'] = self.storeTest
        saveButton.grid(row=32, sticky=SE)
