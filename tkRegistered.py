from tkinter import *
import time
import threading
from tkinter import messagebox

import history
import tkError
import tkNewUser


def runRegisteredUser(root, layout):
    # Creates Toplevel
    registeredWindow = Toplevel(root)
    registeredWindow.title(layout + "'s Wallet Counter")
    registeredWindow.geometry("1600x1600")

    # Welcome Label
    header = Label(registeredWindow, text=layout + "'s Current Wallet('s) Amount",
                   font=("Cambria", 16, "bold"))
    header.place(y=10)
    header.pack(pady=10)

    # Wallet Selector


    # Select Person Button
    selectedWallet = StringVar(registeredWindow)
    selectedWallet.set("-Select Wallet-")

    ownerMenu = OptionMenu(registeredWindow, selectedWallet, *history.walletCoinListBuilder(layout, "Main"))
    ownerMenu.pack()
    ownerMenu.config(font=("Cambria", 15, "bold"))

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 5), pady=(5, 0))

    # Start Button
    def startApp():
        layout = selectedWallet.get()
        if layout == "-Select Wallet-":
            tkError.errorWindow(registeredWindow)
        elif layout == "-New User-":
            tkNewUser.runNewUser(registeredWindow)
        else:
            runRegisteredUser(root, layout)

    # button = Button(registeredWindow, text="Start", command=startApp, height=1, width=6, font=("Cambria", 15, "bold"))
    # button.pack()

    # coin builder for current wallet
    coinFrameHistory = Frame(registeredWindow, borderwidth=5, background="black")
    coinFrameHistory.pack(pady=25)
    historyString = str(history.runWallets(layout, "Main"))
    historyLabel = Label(coinFrameHistory, text=historyString, justify=LEFT)
    historyLabel.pack()

    # Welcome Label
    header = Label(registeredWindow, text="Add a new transaction:",
                   font=("Cambria", 12, "bold"))
    header.place()
    header.pack()

    # Entry's on bottom; built from bottom up 1
    coinFrameLabel = Frame(registeredWindow)
    coinFrameLabel.pack(      pady=10)

    # Entry's on bottom; built from bottom up 2
    coinFrameEntry = Entry(registeredWindow)
    coinFrameEntry.pack(      pady=10)

    # Buttons on bottom Frame Build built from bottom 3
    buttons = Frame(registeredWindow)
    buttons.pack(     pady=10)
    close_button = Button(buttons, text="Submit", command=registeredWindow.destroy)
    close_button.pack(side=LEFT)
    close_button = Button(buttons, text="Close", command=registeredWindow.destroy)
    close_button.pack(padx=15)

    # Coin Label Entry
    coinLabel = Label(coinFrameLabel, text="Enter Coin" + "\n" + "eg: bitcoin, ethereum", font=("Helvetica", 10))
    coinLabel.pack(side=LEFT, padx=10)
    coinEntry = Entry(coinFrameEntry, width=22)
    coinEntry.pack(side=LEFT)

    # Amount Label Entry
    amountLabel = Label(coinFrameLabel, text="Enter Amount of Coin" + "\n" + "eg: 3.5673235", font=("Helvetica", 10))
    amountLabel.pack(side=RIGHT)
    amountEntry = Entry(coinFrameEntry, width=22)
    amountEntry.pack(side=RIGHT)

    root.withdraw()
