import tkinter

def new_window():
    window = tkinter.TopLevel(root)

root = tkinter.tkinter()
Create_Test = tkinter.Button(root, text = "Create Test" , command = new_window)
Create_Test.pack()

root.mainloop()
