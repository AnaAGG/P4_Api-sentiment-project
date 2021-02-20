from pymongo import MongoClient

client = MongoClient()
db = client.QuoteAPI

def insert_data(coll, obj, database = db): #con esto inserto datos en una coleccion que existe, y si no existe Mongo es muy listo y la crea
    insert = db[coll].insert_one(obj)
    return insert

def read_data(query, coll, database = db, project = None): 
    all_info = database[coll].find(query)
    return list(all_info)

def update_data(collection, query, update,database = db):
    setting = {"$set":update}
    response = db[collection].update_one(query,setting)
    return response

def delete_data (coll, query, database = db):
    deletion = database[coll].remove(query)
    return deletion

def create_coll(coll, obj,client=client):
    res = db[coll].insert_one(obj)
    return res