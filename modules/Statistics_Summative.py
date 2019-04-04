from tkinter import *
import csv
from exams.exams import *
class Statistics_Summative(Frame):

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
            print(self.exam)
        with open("exams/list_of_exams.csv") as file:
            exams = list(csv.reader(file))
            for i in range(len(exams)):
                if exams[i][1] == str(self.exam.rsplit('/',1)[-1]):
                    people = exams[i][2]
                    amount_of_people = people.split("`")
                else:
                    pass
        result_dictionary = {}
        #declare main dictionary outside of loop
        with open("exams/stored_results.csv", 'r') as rfile:
            #open the resultsfile
            read_res = csv.reader(rfile)
            #read in
            listed_inputs = [row for row in read_res if row]
            #reads in the inputted lines to a list in a list and ignores newline if present
            for i in range(len(listed_inputs)):
                exam_key = listed_inputs[i][0]
                #creates the top level key
                result_dictionary[exam_key] = {}
                #creates an empty dictionary in the top level key
            for j in range(len(listed_inputs)):
                intermed_dict = {}
                #declare dictionary to use inside the loop
                exam_inputted = listed_inputs[j][0]
                #find the top level key to append to
                internal_list = []
                #internal placeholder list to append to for the value for the second dictionary
                listedres = listed_inputs[j][3].split("`")
                listedres.pop(0)
                listedres = [int(i) for i in listedres]
                # #splits the results string back in to a list
                internal_list.append(listed_inputs[j][2])
                # #appends who took the test first
                internal_list.append(listedres)
                # #then appends the results they inputted
                intermed_dict[internal_list[0]] = internal_list[1]
                # #assigns the key and value to be inputted in to the external dictionary
                result_dictionary[exam_inputted].update(intermed_dict)
                # #updates the dictionary
            print(result_dictionary)
        outerlist = []
        for key in result_dictionary:
        	if key in str(self.exam):
        		print(key)
        		for key, value in result_dictionary[key].items():
        			innerlist = []
        			innerlist.insert(0,key)
        			innerlist.insert(1,value)
        			outerlist.append(innerlist)
        	else:
        		print("passed")
        		pass
        print(outerlist)
        userlist = []
        for i in range(len(outerlist)):
        	userlist.append(outerlist[i][0])
        print(userlist)



        A1lst = [0, 0, 0, 0]
        A2lst = [0, 0, 0, 0]
        A3lst = [0, 0, 0, 0]
        A4lst = [0, 0, 0, 0]
        A5lst = [0, 0, 0, 0]
        A6lst = [0, 0, 0, 0]
        A7lst = [0, 0, 0, 0]
        A8lst = [0, 0, 0, 0]
        A9lst = [0, 0, 0, 0]
        A10lst = [0, 0, 0, 0]
        with open("exams/stored_results.csv") as file2:
            storedResults = list(csv.reader(file2))
            for i in range(len(storedResults)):
                if storedResults[i][1] == self.exam:
                    listresults = storedResults[i][3].split("`")
                    listresults.pop(0)
                    listresults = [int(i) for i in listresults]
                    A1 = listresults[0]
                    A2 = listresults[1]
                    A3 = listresults[2]
                    A4 = listresults[3]
                    A5 = listresults[4]
                    A6 = listresults[5]
                    A7 = listresults[6]
                    A8 = listresults[7]
                    A9 = listresults[8]
                    A10 = listresults[9]
                    A1lst[A1-1] += 1
                    A2lst[A2-1] += 1
                    A3lst[A3-1] += 1
                    A4lst[A4-1] += 1
                    A5lst[A5-1] += 1
                    A6lst[A6-1] += 1
                    A7lst[A7-1] += 1
                    A8lst[A8-1] += 1
                    A9lst[A9-1] += 1
                    A10lst[A10-1] += 1
                else:
                    pass
            for item in userlist:
            	button = Button(self, text=item)
            	button.pack( side = LEFT)


            

            self.txtDisplay.insert(END, "How many people answered the test" + tabResults + str(len(amount_of_people)-1) + "\n", 'boldfont')

            self.txtDisplay.insert(END, "Questions" + tabResults + "Answers" + "\n" , 'boldfont')


            questions = reader[0][1].split('`')
            self.txtDisplay.insert(END, reader[0][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A1lst[0]) + tabResults + str(A1lst[1]) + tabResults + str(A1lst[2]) + tabResults + str(A1lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A1lst[0] / sum(A1lst) * 100) + "%" + tabResults + str(A1lst[1] / sum(A1lst) * 100) + "%" + tabResults + str(A1lst[2] / sum(A1lst) * 100) + "%" + tabResults + str(A1lst[3] / sum(A1lst) * 100) + "%" + "\n","normfont")

            questions = reader[1][1].split('`')
            self.txtDisplay.insert(END, reader[1][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A2lst[0]) + tabResults + str(A2lst[1]) + tabResults + str(A2lst[2]) + tabResults + str(A2lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A2lst[0] / sum(A2lst) * 100) + "%" + tabResults + str(A2lst[1] / sum(A2lst) * 100) + "%" + tabResults + str(A2lst[2] / sum(A2lst) * 100) + "%" + tabResults + str(A2lst[3] / sum(A2lst) * 100) + "%" + "\n","normfont")

            questions = reader[2][1].split('`')
            self.txtDisplay.insert(END, reader[2][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A3lst[0]) + tabResults + str(A3lst[1]) + tabResults + str(A3lst[2]) + tabResults + str(A3lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A3lst[0] / sum(A3lst) * 100) + "%" + tabResults + str(A3lst[1] / sum(A3lst) * 100) + "%" + tabResults + str(A3lst[2] / sum(A3lst) * 100) + "%" + tabResults + str(A3lst[3] / sum(A3lst) * 100) + "%" + "\n","normfont")

            questions = reader[3][1].split('`')
            self.txtDisplay.insert(END, reader[3][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A4lst[0]) + tabResults + str(A4lst[1]) + tabResults + str(A4lst[2]) + tabResults + str(A4lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A4lst[0] / sum(A4lst) * 100) + "%" + tabResults + str(A4lst[1] / sum(A4lst) * 100) + "%" + tabResults + str(A4lst[2] / sum(A4lst) * 100) + "%" + tabResults + str(A4lst[3] / sum(A4lst) * 100) + "%" + "\n","normfont")

            questions = reader[4][1].split('`')
            self.txtDisplay.insert(END, reader[4][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A5lst[0]) + tabResults + str(A5lst[1]) + tabResults + str(A5lst[2]) + tabResults + str(A5lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A5lst[0] / sum(A5lst) * 100) + "%" + tabResults + str(A5lst[1] / sum(A5lst) * 100) + "%" + tabResults + str(A5lst[2] / sum(A5lst) * 100) + "%" + tabResults + str(A5lst[3] / sum(A5lst) * 100) + "%" + "\n","normfont")

            questions = reader[5][1].split('`')
            self.txtDisplay.insert(END, reader[5][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A6lst[0]) + tabResults + str(A6lst[1]) + tabResults + str(A6lst[2]) + tabResults + str(A6lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A6lst[0] / sum(A6lst) * 100) + "%" + tabResults + str(A6lst[1] / sum(A6lst) * 100) + "%" + tabResults + str(A6lst[2] / sum(A6lst) * 100) + "%" + tabResults + str(A6lst[3] / sum(A6lst) * 100) + "%" + "\n","normfont")

            questions = reader[6][1].split('`')
            self.txtDisplay.insert(END, reader[6][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A7lst[0]) + tabResults + str(A7lst[1]) + tabResults + str(A7lst[2]) + tabResults + str(A7lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A7lst[0] / sum(A7lst) * 100) + "%" + tabResults + str(A7lst[1] / sum(A7lst) * 100) + "%" + tabResults + str(A7lst[2] / sum(A7lst) * 100) + "%" + tabResults + str(A7lst[3] / sum(A7lst) * 100) + "%" + "\n","normfont")

            questions = reader[7][1].split('`')
            self.txtDisplay.insert(END, reader[7][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A8lst[0]) + tabResults + str(A8lst[1]) + tabResults + str(A8lst[2]) + tabResults + str(A8lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A8lst[0] / sum(A8lst) * 100) + "%" + tabResults + str(A8lst[1] / sum(A8lst) * 100) + "%" + tabResults + str(A8lst[2] / sum(A8lst) * 100) + "%" + tabResults + str(A8lst[3] / sum(A8lst) * 100) + "%" + "\n","normfont")

            questions = reader[8][1].split('`')
            self.txtDisplay.insert(END, reader[8][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A9lst[0]) + tabResults + str(A9lst[1]) + tabResults + str(A9lst[2]) + tabResults + str(A9lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A9lst[0] / sum(A9lst) * 100) + "%" + tabResults + str(A9lst[1] / sum(A9lst) * 100) + "%" + tabResults + str(A9lst[2] / sum(A9lst) * 100) + "%" + tabResults + str(A9lst[3] / sum(A9lst) * 100) + "%" + "\n","normfont")

            questions = reader[9][1].split('`')
            self.txtDisplay.insert(END, reader[9][0] + tabResults + questions[0] + tabResults + questions[1] + tabResults + questions[2] + tabResults + questions[3] + "\n", "normfont")
            self.txtDisplay.insert(END, "Answers" + tabResults + str(A10lst[0]) + tabResults + str(A10lst[1]) + tabResults + str(A10lst[2]) + tabResults + str(A10lst[3]) + "\n","normfont")
            self.txtDisplay.insert(END, "Percentage answered" + tabResults + str(A10lst[0] / sum(A10lst) * 100) + "%" + tabResults + str(A10lst[1] / sum(A10lst) * 100) + "%" + tabResults + str(A10lst[2] / sum(A10lst) * 100) + "%" + tabResults + str(A10lst[3] / sum(A10lst) * 100) + "%" + "\n","normfont")

            self.txtDisplay['state'] = DISABLED
            self.txtDisplay.pack()