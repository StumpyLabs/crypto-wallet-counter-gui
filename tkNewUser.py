from tkinter import *
import time
import threading
from tkinter import messagebox


def runNewUser(root):
    newUserWindow = Toplevel(root)
    newUserWindow.title("New User's Crypto Counter")
    newUserWindow.geometry("600x300")

    # nameLabel = Label(newUserWindow, text="Enter Name (First Last)" + "\n" + "eg: John Doe", font=("Helvetica", 12))
    # nameLabel.pack(pady=10)
    # nameEntry = Entry(newUserWindow)
    # nameEntry.pack(pady=10)

    def display_info():
        # Get input from entry fields
        customer_name = entry_name.get()
        customer_email = entry_email.get()

        # Display the customer information
        messagebox.showinfo("Customer Information", f"Name: {customer_name}\nWallet: {customer_email}")

    # Labels and Entry fields
    label_name = Label(newUserWindow, text="Enter Name (First Last)" + "\n" + "eg: John Doe", font=("Helvetica", 12))
    label_name.pack(pady=5)
    entry_name = Entry(newUserWindow, width=40)
    entry_name.pack(pady=5)

    label_email = Label(newUserWindow, text="Enter Wallet Name" + "\n" + "eg: Main, Binance", font=("Helvetica", 12))
    label_email.pack(pady=5)
    entry_email = Entry(newUserWindow, width=40)
    entry_email.pack(pady=5)





    # Button to trigger the display function
    submit_button = Button(newUserWindow, text="Submit", command=display_info)
    submit_button.pack(pady=10)

    close_button = Button(newUserWindow, text="Close", command=newUserWindow.destroy)
    close_button.pack(pady=10)

    root.withdraw()
