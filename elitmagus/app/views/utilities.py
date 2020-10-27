import pymongo

#to establish connection with mongodb
def connectMongo():
    return pymongo.MongoClient("mongodb://localhost:27017/")