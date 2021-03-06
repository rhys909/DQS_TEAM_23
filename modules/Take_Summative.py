from tkinter import *
import tkinter.messagebox as tkm
import csv
from exams.exams import summativeExams


class Take_Summative(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        with open("modules/passInfo.txt", "r") as activeexam:
            self.exam = activeexam.readlines()
            self.user = self.exam[0].rstrip("\n")
            self.exam = self.exam[1]
        self.grid()
        self.init_window(self.exam)

    def init_window(self, exam):
        with open(self.exam) as csvfile:
            reader = csv.reader(csvfile)
            reader = list(reader)
            
            self.varQ1 = IntVar(None, 1)
            lblQ1 = Label(self, text=reader[0][0], font=('MS', 12, "bold"))
            lblQ1.grid(row=0, sticky=W)
            questions = reader[0][1].split('`')
            pos=1
            for question in questions:
                rbQ1 = Radiobutton(self, text=question, variable=self.varQ1, value=(questions.index(question)+1))
                rbQ1.grid(row=pos, column=0, sticky=W)
                pos += 1
            pos += 1

            self.varQ2 = IntVar(None, 1)
            lblQ2 = Label(self, text=reader[1][0], font=('MS', 12, "bold"))
            lblQ2.grid(row=pos, sticky=W)
            pos += 1
            questions = reader[1][1].split('`')
            for question in questions:
                rbQ2 = Radiobutton(self, text=question, variable=self.varQ2, value=(questions.index(question)+1))
                rbQ2.grid(row=pos, column=0, sticky=W)
                pos += 1
            pos += 1

            self.varQ3 = IntVar(None, 1)
            lblQ3 = Label(self, text=reader[2][0], font=('MS', 12, "bold"))
            lblQ3.grid(row=pos, sticky=W)
            pos += 1
            questions = reader[2][1].split('`')
            for question in questions:
                rbQ4 = Radiobutton(self, text=question, variable=self.varQ3, value=(questions.index(question)+1))
                rbQ4.grid(row=pos, column=0, sticky=W)
                pos += 1
            pos += 1

            self.varQ4 = IntVar(None, 1)
            lblQ4 = Label(self, text=reader[3][0], font=('MS', 12, "bold"))
            lblQ4.grid(row=pos, sticky=W)
            pos += 1
            questions = reader[3][1].split('`')
            for question in questions:
                rbQ4 = Radiobutton(self, text=question, variable=self.varQ4, value=(questions.index(question)+1))
                rbQ4.grid(row=pos, column=0, sticky=W)
                pos += 1
            pos += 1

            self.varQ5 = IntVar(None, 1)
            lblQ5 = Label(self, text=reader[4][0], font=('MS', 12, "bold"))
            lblQ5.grid(row=pos, sticky=W)
            pos += 1
            questions = reader[4][1].split('`')
            for question in questions:
                rbQ5 = Radiobutton(self, text=question, variable=self.varQ5, value=(questions.index(question)+1))
                rbQ5.grid(row=pos, column=0, sticky=W)
                pos += 1
            pos += 1

            pos = 0
            self.varQ6 = IntVar(None, 1)
            lblQ6 = Label(self, text=reader[5][0], font=('MS', 12, "bold"))
            lblQ6.grid(row=pos, column=4, sticky=W)
            pos += 1
            questions = reader[5][1].split('`')
            for question in questions:
                rbQ6 = Radiobutton(self, text=question, variable=self.varQ6, value=(questions.index(question)+1))
                rbQ6.grid(row=pos, column=4, sticky=W)
                pos += 1
            pos += 1

            self.varQ7 = IntVar(None, 1)
            lblQ7 = Label(self, text=reader[6][0], font=('MS', 12, "bold"))
            lblQ7.grid(row=pos, column=4, sticky=W)
            pos += 1
            questions = reader[6][1].split('`')
            for question in questions:
                rbQ7 = Radiobutton(self, text=question, variable=self.varQ7, value=(questions.index(question)+1))
                rbQ7.grid(row=pos, column=4, sticky=W)
                pos += 1
            pos += 1

            self.varQ8 = IntVar(None, 1)
            lblQ8 = Label(self, text=reader[7][0], font=('MS', 12, "bold"))
            lblQ8.grid(row=pos, column=4, sticky=W)
            pos += 1
            questions = reader[7][1].split('`')
            for question in questions:
                rbQ8 = Radiobutton(self, text=question, variable=self.varQ8, value=(questions.index(question)+1))
                rbQ8.grid(row=pos, column=4, sticky=W)
                pos += 1
            pos += 1

            self.varQ9 = IntVar(None, 1)
            lblQ9 = Label(self, text=reader[8][0], font=('MS', 12, "bold"))
            lblQ9.grid(row=pos, column=4, sticky=W)
            pos += 1
            questions = reader[8][1].split('`')
            for question in questions:
                rbQ9 = Radiobutton(self, text=question, variable=self.varQ9, value=(questions.index(question)+1))
                rbQ9.grid(row=pos, column=4, sticky=W)
                pos += 1
            pos += 1

            self.varQ10 = IntVar(None, 1)
            lblQ10 = Label(self, text=reader[9][0], font=('MS', 12, "bold"))
            lblQ10.grid(row=pos, column=4, sticky=W)
            pos += 1
            questions = reader[9][1].split('`')
            for question in questions:
                rbQ10 = Radiobutton(self, text=question, variable=self.varQ10, value=(questions.index(question)+1))
                rbQ10.grid(row=pos, column=4, sticky=W)
                pos += 1
            pos += 1

            butSubmit = Button(self, text="Submit", font=("MS", 8, "bold"), command=self.storeAnswers)
            butSubmit.grid(row=pos, column=0, sticky=W)

    def storeAnswers(self):
            user_answered = str(self.varQ1.get()) + " " + str(self.varQ2.get()) + " " + str(self.varQ3.get()) + " " + str(self.varQ4.get()) + " " + str(self.varQ5.get()) + " " + str(self.varQ6.get()) + " " + str(self.varQ7.get()) + " " + str(self.varQ8.get()) + " " + str(self.varQ9.get()) + " " + str(self.varQ10.get())
            user_answered = user_answered.split(" ")
            with open(self.exam) as csvfile:
                reader = csv.reader(csvfile)
                print(user_answered)
                answers = list(reader)[10]
                marks = 10
                for i in range(len(answers)-1):
                    if user_answered[i] != answers[i]:
                        marks -= 1
                tkm.showinfo("Exam submitted", f"You scored {marks}/10")
            tempList = []
            with open("exams/list_of_exams.csv") as file:
                read = list(csv.reader(file))
                for row in read:
                    tempList.append(row)
                for item in tempList:
                    if ("exams/" + item[1]) == self.exam:
                        item[2] = item[2] + "`" + self.user
                
            with open("exams/list_of_exams.csv", "w") as file:
                for item in tempList:
                    for i in item:
                        if i != item[-1]:
                            file.write(i + ",")
                        else:
                            file.write(i + "\n")
                 ###################
            result_string = "`".join(user_answered)
            #splitting bart's user output for debugging
            start = "exams/"
            end = ".csv"
            #defining the beginning and end for the search for exam name
            examname = str(self.exam)
            #take in the directory
            examname = examname[examname.find(start)+len(start):examname.rfind(end)]
            #search for the string between string start and string end and assign
            result_file = open("exams/stored_results.csv", 'a', newline='')
            #use append for writing to do newline formatting
            result_write = []
            #declare empty list to append
            result_write.insert(0,examname)
            #the searched value
            result_write.insert(1,self.exam)
            #the directory
            result_write.insert(2,self.user)
            #user taking the test
            result_write.insert(3,result_string)
            #Add "Open" to end
            result_write.insert(4,"Open")
            #the split list for reassembling in statistics
            with result_file:
                writer = csv.writer(result_file, delimiter=",")
                #assign writer
                writer.writerow(result_write)
                #output
            ###################       
                    

