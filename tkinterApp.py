from tkinter import *


def startApp(root):
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
    selection = Label(root, text="Here you can add all of your cryptos you own and find total value!", font=("Cambria", 15, "bold"))
    selection.place(y=30)
    selection.pack()

    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 10), pady=(10, 0))

    # Select Button
    selectedLayout = StringVar(root)
    selectedLayout.set("--Select a layout--")
    layoutMenu = OptionMenu(root, selectedLayout, "--Select a layout--", "QWERTY", "Dvorak", "Colemak", "Workman")
    layoutMenu.pack()
    layoutMenu.config(font=("Cambria", 15, "bold"))








    # Padding
    label = Label(root, text="")
    label.pack(padx=(0, 5), pady=(5, 0))

    root.mainloop()
