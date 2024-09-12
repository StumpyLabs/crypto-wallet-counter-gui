import tkinter
from tkinter import *

import history
import tkError
import tkNewUser
import tkRegistered


def startApp(root):
    root.title("StumpyLabs Crypto Wallet Counter")
    root.geometry("1000x500")
    root.resizable(width=False, height=False)

    # Padding from top
    label = Label(root, text="")
    label.pack(padx=(0, 50), pady=(50, 0))

    # Welcome Label
    header = Label(root, text="StumpyLabs Crypto Wallet Counter", font=("Cambria", 25, "bold"))
    header.place(y=10)
    header.pack()

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 10), pady=(10, 0))

    # Please Select label
    selection = Label(root, text="Here you can add all of your current crypto you own and continue to add entry's! \n"
                                 "This will give you precise history of your buys and sells of each coin and total"
                                 " wallet value.", font=("Cambria", 12, "bold"))
    selection.place(y=30)
    selection.pack()

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 20), pady=(20, 0))

    # Select Person Button
    selectedPerson = StringVar(root)
    selectedPerson.set("-Select Owner-")

    ownerMenu = OptionMenu(root, selectedPerson, *history.nameListApp())
    ownerMenu.pack()
    ownerMenu.config(font=("Cambria", 15, "bold"))

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 5), pady=(5, 0))

    # Start Button
    def startApp():
        layout = selectedPerson.get()
        if layout == "-Select Owner-":
            tkError.errorWindow(root)
        elif layout == "-New User-":
            tkNewUser.runNewUser(root)
        else:
            tkRegistered.runRegisteredUser(root, layout)

    button = Button(root, text="Start", command=startApp, height=1, width=6, font=("Cambria", 15, "bold"))
    button.pack()

    root.mainloop()
