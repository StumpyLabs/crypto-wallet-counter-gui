import pyMongoDB as db


# list of user in DB
def nameListBuilder():
    nameList = []
    result = db.collection.find()
    for i in result:
        if i["customerName"] not in nameList:
            nameList.append(i["customerName"])
    print("Name List: " + str(nameList))
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
def nameCoinListBuilder(customerName):
    coinList = []
    result = db.collection.find({"customerName": customerName})
    for i in result:
        if i["customerCoin"] not in coinList:
            coinList.append(i["customerCoin"])
    print(customerName + "'s coin list: " + str(coinList))
    return coinList


def runNames(name):
    nameList = nameListBuilder()
    stringBuilder = ""
    for i in nameList:
        if i == name:
            accountTotal = 0
            coinList = nameCoinListBuilder(i)
            for coin in coinList:
                coinTotal = searchCoinNameDB(i, coin)
                accountTotal += coinTotal
                stringBuilder += (coin + ": " + str(coinTotal) + "\n")
            stringBuilder += ("Account Total: " + str(accountTotal))


def searchNameDB(customerName):
    result = db.collection.find({"customerName": customerName})
    total = 0
    for i in result:
        total += i["totalAmount"]
    return total


def searchCoinDB(customerCoin):
    result = db.collection.find({"customerCoin": customerCoin})
    total = 0
    for i in result:
        total += i["totalAmount"]
    return total


def searchCoinNameDB(customerName, customerCoin):
    result = db.collection.find({"customerName": customerName, "customerCoin": customerCoin})
    total = 0
    for i in result:
        total += i["totalAmount"]
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
