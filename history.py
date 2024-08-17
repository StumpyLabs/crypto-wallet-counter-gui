import pyMongoDB as db


# list of user in DB
def nameListBuilder():
    nameList = []
    result = db.collection.find()
    for i in result:
        if i["customerName"] not in nameList:
            nameList.append(i["customerName"])
    print(nameList)


def searchDB():
    result = db.collection.find({"customerName": "casey", "customerCoin": "bitcoin"})
    total = 0
    for i in result:
        total += i["totalAmount"]
    print(total)


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
