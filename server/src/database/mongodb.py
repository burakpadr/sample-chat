import pymongo
import json
from bson.json_util import dumps
from src.etc.settings import Settings
from src.etc.project import Project


class MongoDB:

    __DATABASE = pymongo.MongoClient(Settings.MONGODB_URI)[Project.NAME]

    def __init__(self, collectionName):
        self.__collection = MongoDB.__DATABASE[collectionName]

    def create(self, data):
        self.__collection.insert_one(data)
    
    def read(self, data=None):
        return list(json.loads(dumps(self.__collection.find(data))))

    def update(self, queryData, updateData):
        data = {"$set": updateData}
        
        return self.__collection.update_many(queryData, data)
    
    def delete(self, data):
        return self.__collection.delete_many(data)