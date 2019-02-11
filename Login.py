from tkinter import *
import tkinter.messagebox as tkm
import passwords
import hashlib

class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createLabel()
        self.usernameBox()
        self.passwordBox()
        self.submitButton()
        
    def createLabel(self):
        lblIntro = Label(self, text="Login", font=("MS", 8, "bold"))
        lblIntro.grid(row=0, column=0, sticky=NE)

    def usernameBox(self):
        self.username = Entry(self)
        self.username.grid(row=2, column=0, columnspan=2, sticky=W)

    def passwordBox(self):
        self.passwordentry = Entry(self, show="*")
        self.passwordentry.grid(row=4, column=0, columnspan=2, sticky=W, pady=10)

    def submitButton(self):
        submit = Button(self, text="Submit", command=self.validateLogin, font=("MS", 8, "bold"))
        submit.grid(row=5, column=0, sticky=W, pady=10)

    def validateLogin(self):
        if self.username.get().strip() in passwords.users:
            key = hashlib.sha1(self.passwordentry.get().encode('utf-8')).hexdigest()
            if key == passwords.users[self.username.get().strip()]:
                tkm.showinfo("Login Successful", "Login Successful")
            else:
                tkm.showinfo("Password Incorrect", "Password Incorrect")
        else:
            tkm.showinfo("No such user", "No such user")
    

#Main
root = Tk()
root.title("Login")
app = Login(root)
root.mainloop()
