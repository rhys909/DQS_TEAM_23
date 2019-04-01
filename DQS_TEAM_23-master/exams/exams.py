import csv
summativeExams = {}
formativeExams = {}
with open("exams/list_of_exams.csv") as file:
    exams = list(csv.reader(file))
for i in range(len(exams)):
    summativeExams[i+1] = (exams[i][0], exams[i][1], exams[i][2])
with open("exams/list_of_formative.csv") as file:
	form = list(csv.reader(file))
for i in range(len(form)):
    formativeExams[i+1] = (exams[i][0], exams[i][1], exams[i][2])

    

#Exams are stored in this format
#<exam id> : (Exam Name, csv file name, list of users that have done the exam)
