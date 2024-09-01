import coingeckoCalls
import pyMongoDB as db
import json


# list of user in DB
def nameListBuilder():
    nameList = []
    result = db.collection.find()
    for i in result:
        if i["customerName"] not in nameList:
            nameList.append(i["customerName"])
    return nameList


# list of user in DB
def nameListApp():
    nameList = ["-New User-"]
    result = db.collection.find()
    for i in result:
        if i["customerName"] not in nameList:
            nameList.append(i["customerName"])
    return nameList


# list of user's coins in DB
def walletListBuilder(customerName):
    walletList = []
    result = db.collection.find({"customerName": customerName})
    for i in result:
        if i["customerWallet"] not in walletList:
            walletList.append(i["customerWallet"])
    return walletList


# list of user's coins in DB
def walletCoinListBuilder(customerName, customerWallet):
    coinList = []
    result = db.collection.find({"customerName": customerName, "customerWallet": customerWallet})
    for i in result:

        if i["customerCoin"] not in coinList:
            coinList.append(i["customerCoin"])
    return coinList


def runWallets(name, wallet):
    coinListWallet = walletCoinListBuilder(name, wallet)

    stringBuilder = ""
    for coin in coinListWallet:
        coinAmount = searchCoinNameDB(name, coin, wallet)
        coinValue = coingeckoCalls.coinRaw(coin)

        # coin amount
        stringBuilder += (coin + ": " + str(coinAmount) + "\n")
        coinTotal = searchCoinNameDB(name, coinListWallet[-1], wallet)
        coinTotal = coinValue[coin]["usd"] * coinTotal
        stringBuilder += (coinListWallet[-1] + ": Coin Amount: " + str(coinAmount) + " Coin Value: $" +
                          str(coinValue[coin]["usd"]) + " Coin Total: $" + str(coinTotal) + "\n")

        print(str(stringBuilder))
    return str(stringBuilder)


def searchNameDB(customerName):
    result = db.collection.find({"customerName": customerName})
    total = 0
    for i in result:
        total += i["totalAmount"]
    return total


def searchCoinDB(customerCoin, customerWallet):
    result = db.collection.find({"customerCoin": customerCoin, "customerWallet": customerWallet})
    total = 0
    for i in result:
        total += i["totalAmount"]
    return total


def searchCoinNameDB(customerName, customerCoin, customerWallet):
    result = db.collection.find(
        {"customerName": customerName, "customerCoin": customerCoin, "customerWallet": customerWallet})
    total = 0
    for i in result:
        total += i["customerAmount"]
    return total


# delete last input to the DB
def deleteLastInputDB():
    lastInput = db.collection.find_one(sort=[("_id", -1)])

    if lastInput:
        db.collection.delete_one({"_id": lastInput["_id"]})
        print("Last input deleted", lastInput)
    else:
        print("No input found")


def deleteManyDB():
    db.collection.delete_one()


# delete the whole DB
def clearDB():
    db.collection.delete_many({})
    print("DB cleared")
