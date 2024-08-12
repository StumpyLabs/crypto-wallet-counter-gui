from datetime import date, time
from tkinter import *

import coingeckoCalls
import tkinterApp as ta

from datetime import datetime

import json

currentDateAndTime = datetime.now()

customerListDict = []
geckoList = coingeckoCalls.coinsList()

dictionaryList = json.loads(geckoList)


def main():
    # root = Tk()
    # ta.startApp(root)

    print(newEntry())


def coinChecker(customerInput):
    for dictionary in dictionaryList:
        if dictionary['id'] == str(customerInput):
            print("Coin found")
            return customerInput

    customerInput = input("Please enter a valid coin: ")
    coinChecker(customerInput)


def amountChecker(customerInput):
    try:
        # Try to convert the input to a float
        customerInput = float(customerInput)
        return customerInput
    except ValueError:
        # If conversion fails, prompt the user for a valid amount
        print(type(customerInput))
        customerInput = input("Please enter a valid amount: ")
        customerInput = float(customerInput)
        print(type(customerInput))
        amountChecker(customerInput)


def newEntry():
    customerName = input("Enter Name: ")

    continueEntry = True
    while (continueEntry == True):
        # customer input prompts
        customerCoin = input("Enter Coin: ")
        customerCoin = coinChecker(customerCoin)

        customerAmount = input("Enter Amount: ")
        amountChecker(customerAmount)

        # building total amount from coingecko
        totalAmount = customerAmount

        # adding values to dictionary and appending to list
        newEntryDict = {"customerName": customerName, "customerCoin": customerCoin, "customerAmount": customerAmount,
                        "totalAmount": totalAmount, "date&time": currentDateAndTime}
        customerListDict.append(newEntryDict)

        # continue adding coins
        continueEntry = input("Continue? (y/n): ")
        if continueEntry == ("y" or "n"):
            if continueEntry == 'y':
                continueEntry = True
            else:
                continueEntry = False

    return customerListDict


if __name__ == '__main__':
    main()
