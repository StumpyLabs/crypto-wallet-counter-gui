from tkinter import *


def errorWindow(root):
    newWindow = Tk()
    newWindow.title("No User Selected - Error")
    newWindow.geometry("1000x300")
    newWindow.resizable(width=False, height=False)

    header = Label(newWindow, text="Please select user name or select -New User- to get started", font=("Cambria", 15, "bold"))
    header.place(y=10)
    header.pack()