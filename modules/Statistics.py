from tkinter import *
import csv
from exams.exams import *

class Statistics(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        #opens the csv file thats written in Lectuer_UI
        with open("modules/passInfo.txt", "r") as viewExam:
            self.exam = viewExam.readlines()
            self.exam = self.exam[1]
        self.grid()
        self.init_window()

#initializes a window
    def init_window(self):
        #title of the window
        self.master.title("Statistics")
        #formats the font, size etc.
        self.txtDisplay = Text(self, height=30,width=200)
        self.txtDisplay.tag_configure('boldfont', font =('MS', 8, 'bold'))
        self.txtDisplay.tag_configure('normfont', font =('MS', 8))
        #simple tabs to space the results
        tabResults = ""
        tabResults += ("\t" + "\t" + "\t" + "\t" + "\t")
        #all the text that actually displays
        #loads the data from the csvfile
        with open(self.exam) as csvfile:
            reader = csv.reader(csvfile)
            reader = list(reader)
        with open("exams/list_of_exams.csv") as file:
            exams = list(csv.reader(file))
            for i in range(len(exams)):
                if exams[i][1] == str(self.exam.rsplit('/',1)[-1]):
                    people = exams[i][2]
                    amount_of_people = people.split("`")
                else:
                    pass
            
            self.txtDisplay.insert(END, "How many people answered the test" + tabResults + str(len(amount_of_people)-1) + "\n", 'boldfont')

            self.txtDisplay.insert(END, "Questions" + tabResults + "Answers" + "\n" , 'boldfont')

            questions = reader[0][1].split('`')
            self.txtDisplay.insert(END, reader[0][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[1][1].split('`')
            self.txtDisplay.insert(END, reader[1][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[2][1].split('`')
            self.txtDisplay.insert(END, reader[2][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[3][1].split('`')
            self.txtDisplay.insert(END, reader[3][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[4][1].split('`')
            self.txtDisplay.insert(END, reader[4][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[5][1].split('`')
            self.txtDisplay.insert(END, reader[5][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[6][1].split('`')
            self.txtDisplay.insert(END, reader[6][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[7][1].split('`')
            self.txtDisplay.insert(END, reader[7][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[8][1].split('`')
            self.txtDisplay.insert(END, reader[8][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")

            questions = reader[9][1].split('`')
            self.txtDisplay.insert(END, reader[9][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "%" + tabResults + "%d" % 21 + "% \t" + "\n \n","normfont")
            
            self.txtDisplay['state'] = DISABLED
            self.txtDisplay.pack() 

