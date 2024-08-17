import coingeckoCalls
from datetime import datetime
import json
import pyMongoDB as db

currentDateAndTime = datetime.now()

# coin list check
customerListDict = []
geckoListCheck = coingeckoCalls.coinsList()
dictionaryListCheck = json.loads(geckoListCheck)


def newEntry():
    customerName = input("Enter Name: ")

    continueEntry = True
    while (continueEntry == True):
        # customer coin input prompts
        print("\n" + "Enter Coin eg: bitcoin, ethereum, litecoin")
        customerCoin = input("Enter Coin Here: ")
        customerCoin = coinChecker(customerCoin.lower())

        # customer amount input prompts
        print("\n" + "Enter Amount of Coin eg: 3.5673235")
        customerAmount = input("Enter Amount Here: ")
        customerAmount = amountChecker(customerAmount)

        # building total amount from coingecko
        coinValue, totalAmount = amountBuilder(customerCoin=customerCoin, customerAmount=customerAmount)

        # adding values to dictionary and appending to list
        post = {"customerName": customerName, "customerCoin": customerCoin, "coinValue": coinValue,
                "customerAmount": customerAmount, "totalAmount": totalAmount,
                "date&time": currentDateAndTime}
        db.collection.insert_one(post)

        # continue adding coins
        continueEntry = input("Continue? (y/n): ")
        if continueEntry == ("y" or "n"):
            if continueEntry == 'y':
                continueEntry = True
            else:
                continueEntry = False


def coinChecker(customerInput):
    for dictionary in dictionaryListCheck:
        if dictionary['id'] == str(customerInput):
            print("Coin found")
            return customerInput

    print("Enter Coin eg: bitcoin, ethereum, litecoin")
    customerInput = input("Please enter a valid coin here: ")
    coinChecker(customerInput)


def amountChecker(customerInput):
    # try making float if not ask for correct input
    try:
        customerInput = float(customerInput)
        return float(customerInput)
    except ValueError:
        print("\n" + "Enter Amount of Coin eg: 3.5673235")
        customerInput = input("Please enter a valid amount of Coin here: ")
        return amountChecker(customerInput)


def amountBuilder(customerCoin, customerAmount):
    # coin look up for other information
    geckoListLook = coingeckoCalls.coinRaw(customerCoin)
    dictionaryListLook = json.loads(geckoListLook)

    # look at usd value and build total
    coinValue = dictionaryListLook[customerCoin]['usd']
    customerAmount = float(float(customerAmount) * float(coinValue))
    return float(coinValue), float(customerAmount)
