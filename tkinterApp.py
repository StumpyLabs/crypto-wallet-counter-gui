from tkinter import *


def startApp(root):
    welcomeScreen(root)



    root.mainloop()


def welcomeScreen(root):
    root.title("StumpyLabs Crypto Wallet Counter")
    root.geometry("1200x700")
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
    label.pack(padx=(0, 10), pady=(10, 0))

    # Select Person Button
    selectedPerson = StringVar(root)
    selectedPerson.set("--Select Owner--")
    layoutMenu = OptionMenu(root, selectedPerson, "--Select a layout--", "QWERTY", "Dvorak", "Colemak", "Workman")
    layoutMenu.pack()
    layoutMenu.config(font=("Cambria", 15, "bold"))

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 10), pady=(10, 0))

    # Select History or New Entry
    selectedPerson = StringVar(root)
    selectedPerson.set("--History or New Entry--")
    layoutMenu = OptionMenu(root, selectedPerson, "--Select a layout--", "QWERTY", "Dvorak", "Colemak", "Workman")
    layoutMenu.pack()
    layoutMenu.config(font=("Cambria", 15, "bold"))

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 5), pady=(5, 0))

# def personSelector(person):
#
#
#
