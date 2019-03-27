from tkinter import *
import tkinter.messagebox as tkm
import accounts.accounts as accounts
import hashlib
from modules.Lecturer_UI import *
from modules.Student_UI import *


class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        with open("modules/passInfo.txt", "w") as clearFile:
            clearFile.write("")
        self.createWidgets()
        
    def createWidgets(self):
        lblIntro = Label(self, text="Login", font=("MS", 8, "bold"))
        lblIntro.grid(row=0, column=0, sticky=NE)

        self.username = Entry(self)
        self.username.grid(row=2, column=0, columnspan=2, sticky=W)

        self.passwordentry = Entry(self, show="*")
        self.passwordentry.grid(row=4, column=0, columnspan=2, sticky=W, pady=10)

        submit = Button(self, text="Submit", command=self.validateLogin, font=("MS", 8, "bold"))
        submit.grid(row=5, column=0, sticky=W, pady=10)

    def validateLogin(self):
        self.user = self.username.get().strip()
        pwd = self.passwordentry.get()
        if self.user in accounts.users:
            key = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
            if key == accounts.users[self.user][0]:
                if accounts.users[self.user][1] == "Student":
                    self.openStudentUI()
                else:
                    self.openLecturerUI()
            else:
                tkm.showinfo("Password Incorrect", "Password Incorrect")
        else:
            tkm.showinfo("No such user", "No such user")

    def openStudentUI(self):
        t1 = Toplevel(root)
        Student_UI(t1)
        with open("modules/passInfo.txt", "a") as passInfo:
            passInfo.write(self.user + "\n")
        t1.geometry("600x500")
        root.withdraw()
        t1.lift()
        t1.attributes("-topmost", True)
        t1.resizable(False, False)

    def openLecturerUI(self):
        t1 = Toplevel(root)
        Lecturer_UI(t1)
        with open("modules/passInfo.txt", "a") as passInfo:
            passInfo.write(self.user + "\n")
        t1.geometry("450x350")
        root.withdraw()
        t1.lift()
        t1.attributes("-topmost", True)
        t1.resizable(False, False)

        

    
            
#Main
root = Tk()
root.title("Login")
app = Login(root)
root.mainloop()
