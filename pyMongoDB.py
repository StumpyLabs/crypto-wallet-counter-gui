import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://stumpf80369:Hockey@cluster0.6fy47.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["cryptoWalletCounter"]
collection = db["dataDB"]

# post = {"_id": "casey_1", "score": 19}
#  collection.insert_one(post)