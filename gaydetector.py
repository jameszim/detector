from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="You are gay.")
    myLabel.pack()

#Button   
myButton = Button(root, text="Gay dectector", command=myClick, fg="red")
myButton.pack()


root.mainloop()