import csv
from tkinter import *
from exams.exams import summativeExams
from exams.exams import formativeExams
modifyExam={}
answers={}
fileName=''


class modify (Frame):
    def __init__(self, master=None):
        with open("modules/passInfo.txt", "r") as activeexam:
            self.exam = activeexam.readlines()
            fileName = self.exam
        with open(fileName[1], 'r') as csvFile:
            csvReader=csv.reader(csvFile)
            counter=1
            for line in csvReader:
                if counter==11:
                    c=1
                    for field in line:
                        answers[c]=field
                        c+=1
                    break
                choices=line[1].split('`')
                modifyExam[counter]=[line[0],choices]
                counter+=1
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        with open("modules/passInfo.txt", "r") as activeexam:
            self.exam = activeexam.readlines()
            fileName = self.exam
        pos=0
        ans1=StringVar()
        ans2=StringVar()
        ans3=StringVar()
        ans4=StringVar()
        ans5=StringVar()
        ans6=StringVar()
        ans7=StringVar()
        ans8=StringVar()
        ans9=StringVar()
        ans10=StringVar()
        
        m1=StringVar()
        m11=StringVar()
        m12=StringVar()
        m13=StringVar()
        m14=StringVar()
        m2=StringVar()
        m21=StringVar()
        m22=StringVar()
        m23=StringVar()
        m24=StringVar()
        m3=StringVar()
        m31=StringVar()
        m32=StringVar()
        m33=StringVar()
        m34=StringVar()
        m4=StringVar()
        m41=StringVar()
        m42=StringVar()
        m43=StringVar()
        m44=StringVar()
        m5=StringVar()
        m51=StringVar()
        m52=StringVar()
        m53=StringVar()
        m54=StringVar()
        m6=StringVar()
        m61=StringVar()
        m62=StringVar()
        m63=StringVar()
        m64=StringVar()
        m7=StringVar()
        m71=StringVar()
        m72=StringVar()
        m73=StringVar()
        m74=StringVar()
        m8=StringVar()
        m81=StringVar()
        m82=StringVar()
        m83=StringVar()
        m84=StringVar()
        m9=StringVar()
        m91=StringVar()
        m92=StringVar()
        m93=StringVar()
        m94=StringVar()
        m10=StringVar()
        m101=StringVar()
        m102=StringVar()
        m103=StringVar()
        m104=StringVar()
        
        self.master.title("Modify")
        self.pack(fill=BOTH, expand=1)

        #question 1
        q1=Label(self, text=modifyExam[1][0], font=("MS", 14, "bold")).grid(row=pos, column=0, sticky=W)
        self.q1e=Entry(self, textvariable=m1).grid(row=pos, column=1, sticky=W)
        pos+=1

        q11=Label(self, text=modifyExam[1][1][0], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q11e=Entry(self, textvariable=m11).grid(row=pos, column=1, sticky=W)
        pos+=1
        q12=Label(self, text=modifyExam[1][1][1], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q12e=Entry(self, textvariable=m12).grid(row=pos, column=1, sticky=W)
        pos+=1
        q13=Label(self, text=modifyExam[1][1][2], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q13e=Entry(self, textvariable=m13).grid(row=pos, column=1, sticky=W)
        pos+=1
        q14=Label(self, text=modifyExam[1][1][3], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q14e=Entry(self, textvariable=m14).grid(row=pos, column=1, sticky=W)
        pos+=1
        

        an1=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.an1e=Entry(self, textvariable=ans1).grid(row=pos, column=1, sticky=W)
        pos+=1

        
        #question 2
        q2=Label(self, text=modifyExam[2][0], font=("MS", 14, "bold")).grid(row=pos, column=0, sticky=W)
        self.q2e=Entry(self, textvariable=m2).grid(row=pos, column=1, sticky=W)
        pos+=1

        q21=Label(self, text=modifyExam[2][1][0], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q21e=Entry(self, textvariable=m21).grid(row=pos, column=1, sticky=W)
        pos+=1
        q22=Label(self, text=modifyExam[2][1][1], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q22e=Entry(self, textvariable=m22).grid(row=pos, column=1, sticky=W)
        pos+=1
        q23=Label(self, text=modifyExam[2][1][2], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q23e=Entry(self, textvariable=m23).grid(row=pos, column=1, sticky=W)
        pos+=1
        q24=Label(self, text=modifyExam[2][1][3], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q24e=Entry(self, textvariable=m24).grid(row=pos, column=1, sticky=W)
        pos+=1

        an2=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.an2e=Entry(self, textvariable=ans2).grid(row=pos, column=1, sticky=W)
        pos+=1

        #question 3
        q3=Label(self, text=modifyExam[3][0], font=("MS", 14, "bold")).grid(row=pos, column=0, sticky=W)
        self.q3e=Entry(self, textvariable=m3).grid(row=pos, column=1, sticky=W)
        pos+=1

        q31=Label(self, text=modifyExam[3][1][0], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q31e=Entry(self, textvariable=m31).grid(row=pos, column=1, sticky=W)
        pos+=1
        q32=Label(self, text=modifyExam[3][1][1], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q32e=Entry(self, textvariable=m32).grid(row=pos, column=1, sticky=W)
        pos+=1
        q33=Label(self, text=modifyExam[3][1][2], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q33e=Entry(self, textvariable=m33).grid(row=pos, column=1, sticky=W)
        pos+=1
        q34=Label(self, text=modifyExam[3][1][3], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q34e=Entry(self, textvariable=m34).grid(row=pos, column=1, sticky=W)
        pos+=1

        an3=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.an3e=Entry(self, textvariable=ans3).grid(row=pos, column=1, sticky=W)
        pos+=1

        #question 4
        q4=Label(self, text=modifyExam[4][0], font=("MS", 14, "bold")).grid(row=pos, column=0, sticky=W)
        self.q4e=Entry(self, textvariable=m4).grid(row=pos, column=1, sticky=W)
        pos+=1

        q41=Label(self, text=modifyExam[4][1][0], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q41e=Entry(self, textvariable=m41).grid(row=pos, column=1, sticky=W)
        pos+=1
        q42=Label(self, text=modifyExam[4][1][1], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q42e=Entry(self, textvariable=m42).grid(row=pos, column=1, sticky=W)
        pos+=1
        q43=Label(self, text=modifyExam[4][1][2], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q43e=Entry(self, textvariable=m43).grid(row=pos, column=1, sticky=W)
        pos+=1
        q44=Label(self, text=modifyExam[4][1][3], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q44e=Entry(self, textvariable=m44).grid(row=pos, column=1, sticky=W)
        pos+=1

        an4=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.an4e=Entry(self, textvariable=ans4).grid(row=pos, column=1, sticky=W)
        pos+=1

        #question 5
        q5=Label(self, text=modifyExam[5][0], font=("MS", 14, "bold")).grid(row=pos, column=0, sticky=W)
        self.q5e=Entry(self, textvariable=m5).grid(row=pos, column=1, sticky=W)
        pos+=1

        q51=Label(self, text=modifyExam[5][1][0], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q51e=Entry(self, textvariable=m51).grid(row=pos, column=1, sticky=W)
        pos+=1
        q52=Label(self, text=modifyExam[5][1][1], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q52e=Entry(self, textvariable=m52).grid(row=pos, column=1, sticky=W)
        pos+=1
        q53=Label(self, text=modifyExam[5][1][2], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q53e=Entry(self, textvariable=m53).grid(row=pos, column=1, sticky=W)
        pos+=1
        q54=Label(self, text=modifyExam[5][1][3], font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.q54e=Entry(self, textvariable=m54).grid(row=pos, column=1, sticky=W)
        pos+=1

        an5=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=0, sticky=W)
        self.an5e=Entry(self, textvariable=ans5).grid(row=pos, column=1, sticky=W)
        pos+=1

        pos =0
        #question 6
        q6=Label(self, text=modifyExam[6][0], font=("MS", 14, "bold")).grid(row=pos, column=3, sticky=W)
        self.q6e=Entry(self, textvariable=m6).grid(row=pos, column=4, sticky=W)
        pos+=1

        q61=Label(self, text=modifyExam[6][1][0], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q61e=Entry(self, textvariable=m61).grid(row=pos, column=4, sticky=W)
        pos+=1
        q62=Label(self, text=modifyExam[6][1][1], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q62e=Entry(self, textvariable=m62).grid(row=pos, column=4, sticky=W)
        pos+=1
        q63=Label(self, text=modifyExam[6][1][2], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q63e=Entry(self, textvariable=m63).grid(row=pos, column=4, sticky=W)
        pos+=1
        q64=Label(self, text=modifyExam[6][1][3], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q64e=Entry(self, textvariable=m64).grid(row=pos, column=4, sticky=W)
        pos+=1

        an6=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.an6e=Entry(self, textvariable=ans6).grid(row=pos, column=4, sticky=W)
        pos+=1

        #question 7
        q7=Label(self, text=modifyExam[7][0], font=("MS", 14, "bold")).grid(row=pos, column=3, sticky=W)
        self.q7e=Entry(self, textvariable=m7).grid(row=pos, column=4, sticky=W)
        pos+=1


        q71=Label(self, text=modifyExam[7][1][0], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q71e=Entry(self, textvariable=m71).grid(row=pos, column=4, sticky=W)
        pos+=1
        q72=Label(self, text=modifyExam[7][1][1], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q72e=Entry(self, textvariable=m72).grid(row=pos, column=4, sticky=W)
        pos+=1
        q73=Label(self, text=modifyExam[7][1][2], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q73e=Entry(self, textvariable=m73).grid(row=pos, column=4, sticky=W)
        pos+=1
        q74=Label(self, text=modifyExam[7][1][3], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q74e=Entry(self, textvariable=m74).grid(row=pos, column=4, sticky=W)
        pos+=1

        an7=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.an7e=Entry(self, textvariable=ans7).grid(row=pos, column=4, sticky=W)
        pos+=1

        #question 8
        q8=Label(self, text=modifyExam[8][0], font=("MS", 14, "bold")).grid(row=pos, column=3, sticky=W)
        self.q8e=Entry(self, textvariable=m8).grid(row=pos, column=4, sticky=W)
        pos+=1

        q81=Label(self, text=modifyExam[8][1][0], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q81e=Entry(self, textvariable=m81).grid(row=pos, column=4, sticky=W)
        pos+=1
        q82=Label(self, text=modifyExam[8][1][1], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q82e=Entry(self, textvariable=m82).grid(row=pos, column=4, sticky=W)
        pos+=1
        q83=Label(self, text=modifyExam[8][1][2], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q83e=Entry(self, textvariable=m83).grid(row=pos, column=4, sticky=W)
        pos+=1
        q84=Label(self, text=modifyExam[8][1][3], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q84e=Entry(self, textvariable=m84).grid(row=pos, column=4, sticky=W)
        pos+=1

        an8=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.an8e=Entry(self, textvariable=ans8).grid(row=pos, column=4, sticky=W)
        pos+=1

        #question 9
        q9=Label(self, text=modifyExam[9][0], font=("MS", 14, "bold")).grid(row=pos, column=3, sticky=W)
        self.q9e=Entry(self, textvariable=m9).grid(row=pos, column=4, sticky=W)
        pos+=1

        q91=Label(self, text=modifyExam[9][1][0], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q91e=Entry(self, textvariable=m91).grid(row=pos, column=4, sticky=W)
        pos+=1
        q92=Label(self, text=modifyExam[9][1][1], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q92e=Entry(self, textvariable=m92).grid(row=pos, column=4, sticky=W)
        pos+=1
        q93=Label(self, text=modifyExam[9][1][2], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q93e=Entry(self, textvariable=m93).grid(row=pos, column=4, sticky=W)
        pos+=1
        q94=Label(self, text=modifyExam[9][1][3], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q94e=Entry(self, textvariable=m94).grid(row=pos, column=4, sticky=W)
        pos+=1
        
        an9=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.an9e=Entry(self, textvariable=ans9).grid(row=pos, column=4, sticky=W)
        pos+=1

        
        #question 10
        q10=Label(self, text=modifyExam[10][0], font=("MS", 14, "bold")).grid(row=pos, column=3, sticky=W)
        self.q10e=Entry(self, textvariable=m10).grid(row=pos, column=4, sticky=W)
        pos+=1
        
        q101=Label(self, text=modifyExam[10][1][0], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q101e=Entry(self, textvariable=m101).grid(row=pos, column=4, sticky=W)
        pos+=1
        q102=Label(self, text=modifyExam[10][1][1], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q102e=Entry(self, textvariable=m102).grid(row=pos, column=4, sticky=W)
        pos+=1
        q103=Label(self, text=modifyExam[10][1][2], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q103e=Entry(self, textvariable=m103).grid(row=pos, column=4, sticky=W)
        pos+=1
        q104=Label(self, text=modifyExam[10][1][3], font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.q104e=Entry(self, textvariable=m104).grid(row=pos, column=4, sticky=W)
        pos+=1

        an10=Label(self, text='Type the correct answer (1-4)', font=("MS", 10)).grid(row=pos, column=3, sticky=W)
        self.an10e=Entry(self, textvariable=ans10).grid(row=pos, column=4, sticky=W)
        pos+=1






        
        def save():

            if ans1.get() != "":
                answers[1]=ans1.get()
            if ans2.get() != "":
                answers[2]=ans2.get()
            if ans3.get() != "":
                answers[3]=ans3.get()
            if ans4.get() != "":
                answers[4]=ans4.get()
            if ans5.get() != "":
                answers[5]=ans5.get()
            if ans6.get() != "":
                answers[6]=ans6.get()
            if ans7.get() != "":
                answers[7]=ans7.get()
            if ans8.get() != "":
                answers[8]=ans8.get()
            if ans9.get() != "":
                answers[9]=ans9.get()
            if ans10.get() != "":
                answers[10]=ans10.get()
                        

            
            if m1.get() != "":
                modifyExam[1][0]=m1.get()
                
            if m11.get() != "":
                modifyExam[1][1][0]=m11.get()
            if m12.get() != "":
                modifyExam[1][1][1]=m12.get()
            if m13.get() != "":
                modifyExam[1][1][2]=m13.get()
            if m14.get() != "":
                modifyExam[1][1][3]=m14.get()


            
            if m2.get() != "":
                modifyExam[2][0]=m2.get()

            if m21.get() != "":
                modifyExam[2][1][0]=m21.get()
            if m22.get() != "":
                modifyExam[2][1][1]=m22.get()
            if m23.get() != "":
                modifyExam[2][1][2]=m23.get()
            if m24.get() != "":
                modifyExam[2][1][3]=m24.get()



            if m3.get() != "":
                modifyExam[3][0]=m3.get()

            if m31.get() != "":
                modifyExam[3][1][0]=m31.get()
            if m32.get() != "":
                modifyExam[3][1][1]=m32.get()
            if m33.get() != "":
                modifyExam[3][1][2]=m33.get()
            if m34.get() != "":
                modifyExam[3][1][3]=m34.get()


                
            if m4.get() != "":
                modifyExam[4][0]=m4.get()

            if m41.get() != "":
                modifyExam[4][1][0]=m41.get()
            if m42.get() != "":
                modifyExam[4][1][1]=m42.get()
            if m43.get() != "":
                modifyExam[4][1][2]=m43.get()
            if m44.get() != "":
                modifyExam[4][1][3]=m44.get()


                
            if m5.get() != "":
                modifyExam[5][0]=m5.get()

            if m51.get() != "":
                modifyExam[5][1][0]=m51.get()
            if m52.get() != "":
                modifyExam[5][1][1]=m52.get()
            if m53.get() != "":
                modifyExam[5][1][2]=m53.get()
            if m54.get() != "":
                modifyExam[5][1][3]=m54.get()


                
            if m6.get() != "":
                modifyExam[6][0]=m6.get()

            if m61.get() != "":
                modifyExam[6][1][0]=m61.get()
            if m62.get() != "":
                modifyExam[6][1][1]=m6.get()
            if m63.get() != "":
                modifyExam[6][1][2]=m63.get()
            if m63.get() != "":
                modifyExam[6][1][3]=m63.get()


                
            if m7.get() != "":
                modifyExam[7][0]=m7.get()

            if m71.get() != "":
                modifyExam[7][1][0]=m71.get()
            if m72.get() != "":
                modifyExam[7][1][1]=m72.get()
            if m73.get() != "":
                modifyExam[7][1][2]=m73.get()
            if m74.get() != "":
                modifyExam[7][1][3]=m74.get()


                
            if m8.get() != "":
                modifyExam[8][0]=m8.get()

            if m81.get() != "":
                modifyExam[8][1][0]=m81.get()
            if m82.get() != "":
                modifyExam[8][1][1]=m82.get()
            if m83.get() != "":
                modifyExam[8][1][2]=m83.get()
            if m84.get() != "":
                modifyExam[8][1][3]=m84.get()


                
            if m9.get() != "":
                modifyExam[9][0]=m9.get()

            if m91.get() != "":
                modifyExam[9][1][0]=m91.get()
            if m92.get() != "":
                modifyExam[9][1][1]=m92.get()
            if m93.get() != "":
                modifyExam[9][1][2]=m93.get()
            if m94.get() != "":
                modifyExam[9][1][3]=m94.get()


                
            if m10.get() != "":
                modifyExam[10][0]=m10.get()

            if m101.get() != "":
                modifyExam[10][1][0]=m101.get()
            if m102.get() != "":
                modifyExam[10][1][1]=m102.get()
            if m103.get() != "":
                modifyExam[10][1][2]=m103.get()
            if m104.get() != "":
                modifyExam[10][1][3]=m104.get()

            with open(fileName[1],'w',newline='') as f:
                thewriter= csv.writer(f)
                for i in range (1,len(modifyExam)+1):
                    secondField= modifyExam[i][1][0]+'`'+modifyExam[i][1][1]+'`'+modifyExam[i][1][2]+'`'+modifyExam[i][1][3]
                    thewriter.writerow([modifyExam[i][0],secondField])
                    
                thewriter.writerow([answers[1],answers[2],answers[3],answers[4],answers[5]
                                   ,answers[6],answers[7],answers[8],answers[9],answers[10]])

                
            
        p = Button(self, text="save", command=save, font=("MS", 8, "bold"))
        p.grid(row=pos, column=0, sticky=W, pady=10)

        



        
'''root = Tk()
app = modify(root)
root.mainloop()
root.quit()'''

