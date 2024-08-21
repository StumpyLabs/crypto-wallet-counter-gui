from tkinter import *
import time
import threading


def runNewUser(root):
    newUserWindow = Toplevel(root)
    newUserWindow.title("New User's Crypto Counter")
    newUserWindow.geometry("2300x800")

    label = Label(newUserWindow, text="This is the second window")
    label.pack(pady=20)

    close_button = Button(newUserWindow, text="Close", command=newUserWindow.destroy)
    close_button.pack(pady=10)

    root.withdraw()

