from datetime import datetime
import json
from tkinter import *
from tkinter import messagebox

import coingeckoCalls
import tkRegistered
from pyMongoDB import db

currentDateAndTime = datetime.now()


def runNewUser(root):
    newUserWindow = Toplevel(root)
    newUserWindow.title("New User's Crypto Counter")
    newUserWindow.geometry("600x500")

    # nameLabel = Label(newUserWindow, text="Enter Name (First Last)" + "\n" + "eg: John Doe", font=("Helvetica", 12))
    # nameLabel.pack(pady=10)
    # nameEntry = Entry(newUserWindow)
    # nameEntry.pack(pady=10)

    def display_info():
        # Get input from entry fields
        customer_name = entry_name.get()
        customer_email = entry_wallet.get()

        # # Display the customer information
        # messagebox.showinfo("Customer Information", f"Name: {customer_name}\nWallet: {customer_email}")

    # Labels and Entry fields
    label_name = Label(newUserWindow, text="Enter Name (First Last)" + "\n" + "eg: John Doe", font=("Helvetica", 12))
    label_name.pack(pady=5)
    entry_name = Entry(newUserWindow, width=40)
    entry_name.pack(pady=5)

    label_wallet = Label(newUserWindow, text="Enter Wallet Name" + "\n" + "eg: Main, Binance", font=("Helvetica", 12))
    label_wallet.pack(pady=5)
    entry_wallet = Entry(newUserWindow, width=40)
    entry_wallet.pack(pady=5)

    label_coin = Label(newUserWindow, text="Enter Coin" + "\n" + "eg: bitcoin, ethereum", font=("Helvetica", 12))
    label_coin.pack(pady=5)
    entry_coin = Entry(newUserWindow, width=40)
    entry_coin.pack(pady=5)

    label_amount = Label(newUserWindow, text="Enter Amount of Coin" + "\n" + "eg: 3.5673235", font=("Helvetica", 12))
    label_amount.pack(pady=5)
    entry_amount = Entry(newUserWindow, width=40)
    entry_amount.pack(pady=5)

    def submitUser():
        if (entry_name.get() == ""):
            messagebox.showinfo("Error", "Please enter Name")
            display_info()

        if (entry_wallet.get() == ""):
            messagebox.showinfo("Error", "Please enter Wallet")
            display_info()

        if (entry_coin.get() == ""):
            messagebox.showinfo("Error", "Please enter Coin")
            display_info()

        if (entry_amount.get() == ""):
            messagebox.showinfo("Error", "Please enter Amount of Coin")
            display_info()

        # check all values are inputted
        if (entry_name.get() != "" and entry_wallet.get() != "" and entry_coin.get() != "" and entry_amount.get() != ""):
            # check that coin is a valid coin
            if coinChecker(entry_coin.get().lower()):
                if amountChecker(entry_amount.get()):
                    tkRegistered.runRegisteredUser(root, "Casey Stumpf")
                    #
                    # # Values
                    # customerName = entry_name.get()
                    # customerCoin = entry_coin.get()
                    # customerAmount = entry_amount.get()
                    #
                    # # building total amount from coingecko
                    # coinValue, totalAmount = amountBuilder(customerCoin=entry_coin.get(), customerAmount=entry_amount.get())

                    # adding values to dictionary and appending to list
                    # post = {"customerName": customerName, "customerCoin": customerCoin, "coinValue": coinValue,
                    #         "customerAmount": customerAmount, "totalAmount": totalAmount,
                    #         "date&time": currentDateAndTime}
                    # db.collection.insert_one(post)


    # coin checker
    customerListDict = []
    geckoListCheck = coingeckoCalls.coinsList()
    dictionaryListCheck = json.loads(geckoListCheck)

    def coinChecker(customerInput):
        coinCheck = False
        for dictionary in dictionaryListCheck:
            if dictionary['id'] == str(customerInput):
                coinCheck = True

        if not coinCheck:
            messagebox.showinfo("Error", "Coin entered is not valid")
            display_info()
        return coinCheck

    # amount checker
    def amountChecker(customerInput):
        amountCheck = False
        # try making float if not ask for correct input
        try:
            customerInput = float(customerInput)
            amountCheck = True
        except ValueError:
            messagebox.showinfo("Error", "\n" + "Enter Valid Amount of Coin" + "\n" + "eg: 3.5673235")
            display_info()

    # amount builder
    def amountBuilder(customerCoin, customerAmount):
        # coin look up for other information
        geckoListLook = coingeckoCalls.coinRaw(customerCoin)
        dictionaryListLook = json.loads(geckoListLook)

        # look at usd value and build total
        coinValue = dictionaryListLook[customerCoin]['usd']
        customerAmount = float(float(customerAmount) * float(coinValue))
        return float(coinValue), float(customerAmount)



    # Button to trigger the display function
    submit_button = Button(newUserWindow, text="Submit", command=submitUser)
    submit_button.pack(pady=10)

    close_button = Button(newUserWindow, text="Close", command=newUserWindow.destroy)
    close_button.pack(pady=10)

    root.withdraw()
