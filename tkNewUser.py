from tkinter import *
import time
import threading


def runNewUser(root):
    newUserWindow = Toplevel(root)
    newUserWindow.title("New User's Crypto Counter")
    newUserWindow.geometry("500x550")

    nameLabel = Label(newUserWindow, text="Enter Name (First Last)" + "\n" + "eg: John Doe", font=("Helvetica", 12))
    nameLabel.pack(pady=10)
    nameEntry = Entry(newUserWindow)
    nameEntry.pack(pady=10)

    coinLabel = Label(newUserWindow, text="Enter Coin" + "\n" + "eg: bitcoin, ethereum", font=("Helvetica", 12))
    coinLabel.pack(pady=10)
    coinEntry = Entry(newUserWindow)
    coinEntry.pack(pady=10)

    amountLabel = Label(newUserWindow, text="Enter Amount of Coin" + "\n" + "eg: 3.5673235", font=("Helvetica", 12))
    amountLabel.pack(pady=10)
    amountEntry = Entry(newUserWindow)
    amountEntry.pack(pady=10)

    close_button = Button(newUserWindow, text="Submit", command=newUserWindow.destroy)
    close_button.pack(pady=10)

    close_button = Button(newUserWindow, text="Close", command=newUserWindow.destroy)
    close_button.pack(pady=10)

    root.withdraw()
