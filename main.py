from tkinter import *
import tkinter.messagebox as tkm
import accounts
import hashlib
from Student_UI import *

class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
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
        user = self.username.get().strip()
        pwd = self.passwordentry.get()
        if user in accounts.users:
            key = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
            if key == accounts.users[user][0]:
                if accounts.users[user][1] == "Student":
                    self.openStudentUI()
                else:
                    tkm.showinfo("Login Successful", "Login Successful. You are a lecturer")
            else:
                tkm.showinfo("Password Incorrect", "Password Incorrect")
        else:
            tkm.showinfo("No such user", "No such user")

    def openStudentUI(self):
        t1 = Toplevel(root)
        Student_UI(t1)
        t1.geometry("600x500")
        root.withdraw()
        t1.lift()
        t1.attributes("-topmost", True)
        

    
            
#Main
root = Tk()
root.title("Login")
app = Login(root)
root.mainloop()
