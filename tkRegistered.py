from tkinter import *
import time
import threading
from tkinter import messagebox

import history


def runRegisteredUser(root, layout):
    # Creates Toplevel
    registeredWindow = Toplevel(root)
    registeredWindow.title(layout + "'s Wallet Counter")
    registeredWindow.geometry("1500x2200")

    # Welcome Label
    header = Label(registeredWindow, text="Below is current coin History",
                   font=("Cambria", 18, "bold"))
    header.place(y=10)
    header.pack()

    coinFrameHistory = Frame(registeredWindow)
    coinFrameHistory.pack()
    historyString = str(history.runNames(layout))
    print(historyString)
    historyLabel = Label(registeredWindow, text=historyString)
    historyLabel.pack()
    # Buttons on bottom Frame Build built from bottom 3
    buttons = Frame(registeredWindow)
    buttons.pack(side=BOTTOM, pady=10)
    close_button = Button(buttons, text="Submit", command=registeredWindow.destroy)
    close_button.pack(side=LEFT)
    close_button = Button(buttons, text="Close", command=registeredWindow.destroy)
    close_button.pack(padx=15)

    # Entry's on bottom; built from bottom up 2
    coinFrameEntry = Entry(registeredWindow)
    coinFrameEntry.pack(side=BOTTOM, pady=10)

    # Entry's on bottom; built from bottom up 1
    coinFrameLabel = Frame(registeredWindow)
    coinFrameLabel.pack(side=BOTTOM, pady=10)

    # Coin Label Entry
    coinLabel = Label(coinFrameLabel, text="Enter Coin" + "\n" + "eg: bitcoin, ethereum", font=("Helvetica", 12))
    coinLabel.pack(side=LEFT, padx=10)
    coinEntry = Entry(coinFrameEntry, width=22)
    coinEntry.pack(side=LEFT)

    # Amount Label Entry
    amountLabel = Label(coinFrameLabel, text="Enter Amount of Coin" + "\n" + "eg: 3.5673235", font=("Helvetica", 12))
    amountLabel.pack(side=RIGHT)
    amountEntry = Entry(coinFrameEntry, width=22)
    amountEntry.pack(side=RIGHT)


    root.withdraw()


