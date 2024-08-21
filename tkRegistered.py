from tkinter import *
import time
import threading
from tkinter import messagebox


def runRegisteredUser(root, layout):
    # Creates Toplevel
    registeredWindow = Toplevel(root)
    registeredWindow.title(layout + "'s Wallet Counter")
    registeredWindow.geometry("2300x700")

    # Welcome Label
    header = Label(registeredWindow, text="Please enter all of your coins bought in this time frame",
                   font=("Cambria", 25, "bold"))
    header.place(y=10)
    header.pack()

    def display_info():
        # Get input from entry fields
        customer_name = entry_name.get()
        customer_email = entry_email.get()

        # Display the customer information
        messagebox.showinfo("Customer Information", f"Name: {customer_name}\nEmail: {customer_email}")

    # Labels and Entry fields
    label_name = Label(registeredWindow, text="Name:")
    label_name.pack(pady=5)
    entry_name = Entry(registeredWindow, width=40)
    entry_name.pack(pady=5)

    label_email = Label(registeredWindow, text="Email:")
    label_email.pack(pady=5)
    entry_email = Entry(registeredWindow, width=40)
    entry_email.pack(pady=5)

    # Button to trigger the display function
    submit_button = Button(registeredWindow, text="Submit", command=display_info)
    submit_button.pack(pady=20)

    close_button = Button(registeredWindow, text="Close", command=registeredWindow.destroy)
    close_button.pack(pady=10)

    root.withdraw()
