import pymongo

#to establish connection with mongodb
def connectMongo():
    try:
        return pymongo.MongoClient("mongodb://localhost:27017/")
    except Exception as ex:
        print(ex)
        return -1