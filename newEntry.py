import coingeckoCalls
from datetime import datetime
import json
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://stumpf80369:Hockey@cluster0.6fy47.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["cryptoWalletCounter"]
collection = db["dataDB"]

currentDateAndTime = datetime.now()

#coin list check
customerListDict = []
geckoListCheck = coingeckoCalls.coinsList()
dictionaryListCheck = json.loads(geckoListCheck)


def coinChecker(customerInput):
    for dictionary in dictionaryListCheck:
        if dictionary['id'] == str(customerInput):
            print("Coin found")
            return customerInput

    customerInput = input("Please enter a valid coin: ")
    coinChecker(customerInput)


def amountChecker(customerInput):
    try:
        customerInput = float(customerInput)
        return float(customerInput)
    except ValueError:
        customerInput = input("Please enter a valid amount: ")
        return amountChecker(customerInput)


def amountBuilder(customerCoin, customerAmount):
    # coin look up for other information
    geckoListLook = coingeckoCalls.coinRaw(customerCoin)
    dictionaryListLook = json.loads(geckoListLook)
    coinValue = dictionaryListLook[customerCoin]['usd']
    customerAmount = float(float(customerAmount) * float(coinValue))
    return float(coinValue), float(customerAmount)


def newEntry():
    customerName = input("Enter Name: ")

    continueEntry = True
    while (continueEntry == True):
        # customer input prompts
        customerCoin = input("Enter Coin: ")
        customerCoin = coinChecker(customerCoin.lower())

        customerAmount = input("Enter Amount: ")
        customerAmount = amountChecker(customerAmount)

        # building total amount from coingecko
        coinValue, totalAmount = amountBuilder(customerCoin=customerCoin, customerAmount=customerAmount)

        # adding values to dictionary and appending to list
        post = {"customerName": customerName, "customerCoin": customerCoin, "coinValue": coinValue, "customerAmount": customerAmount,
                "totalAmount": totalAmount, "date&time": currentDateAndTime}
        collection.insert_one(post)

        # continue adding coins
        continueEntry = input("Continue? (y/n): ")
        if continueEntry == ("y" or "n"):
            if continueEntry == 'y':
                continueEntry = True
            else:
                continueEntry = False