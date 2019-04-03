import csv
summativeExams = {}
formativeExams = {}
allExams = {}

with open("exams/list_of_exams.csv") as file:
    exams = list(csv.reader(file))
for i in range(len(exams)):
    if exams[i][3] == "Summative":
        summativeExams[i+1] = (exams[i][0], exams[i][1], exams[i][3], exams[i][4])
        allExams[i+1] = (exams[i][0], exams[i][1], exams[i][3], exams[i][3])
    else:
        formativeExams[i+1] = (exams[i][0], exams[i][1], exams[i][3], exams[i][4])
        allExams[i+1] = (exams[i][0], exams[i][1], exams[i][3], exams[i][4])


    

#Exams are stored in this format
#<exam id> : (Exam Name, csv file name, list of users that have done the exam)
