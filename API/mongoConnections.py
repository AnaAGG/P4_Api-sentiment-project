from pymongo import MongoClient

client = MongoClient()
db = client.QuoteAPI

def insert_data(coll, obj, database = db):
    '''
     #con esto inserto datos en una coleccion 
     # que existe, y si no existe Mongo es muy listo y la crea
    '''
    insert = db[coll].insert_one(obj)
    return insert

def read_data(query, project, coll, database = db): 
    all_info = list(database[coll].find(query, project))
    return all_info

def update_data(collection, query, update,database = db):
    setting = {"$set":update}
    response = db[collection].update_one(query,setting)
    return response

def delete_data (coll, query, database = db):
    deletion = database[coll].remove(query)
    return deletion

def create_coll(coll, obj,client=client): #esta esta pendiente de usar
    res = db[coll].insert_one(obj)
    return res

def update_general():
    mix_coll = db.Biology.aggregate( [
                        { '$unionWith': "Philosophy"},
                        { '$unionWith': "Literature"},   
                        { '$project': { '_id': 1, "Quote":1, "Author":1, "Category":1}},
                        { '$out' : "Quote_Author" } ])
    return mix_coll

def get_authors(database = db):
    query = {}
    project = {"Author":1, "_id":0}
    authors = (list(db.Quote_Author.find( query, project)))
    return authors

def get_quotes(database = db):
    query = {}
    project = {"Quote":1, "_id":0}
    quote = (list(db.Quote_Author.find( query, project)))
    return quote