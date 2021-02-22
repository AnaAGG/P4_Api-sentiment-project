from pymongo import MongoClient

client = MongoClient()
db = client.QuoteAPI

def insert_data(obj,coll, database = db):
    '''
     Insert new objects into an existing collection.

    Receives:
        coll (string): the name of the collection where we are going to insert the new data
        obj : the documents that we are going to include in each object
        database (database): the database that contains our collections

    Returns:
        The inserted element
    '''
    insert = db[coll].insert_one(obj)
    return insert

def read_data(query, project, coll, database = db): 
    '''
    Read objects in a collection

    Receives:
        - query: to determine the objects we want to search
        - project: to specify the inclusion of fields, the suppression of the _id field or the addition of new fields
        - coll (string): the collection in which we want to perform the search
        - database (database): the database that contains our collections

    Returns:
         The elements of our collection that we are looking for
    '''
    all_info = list(database[coll].find(query, project))
    return all_info

def update_data(collection, query, update,database = db):
    setting = {"$set":update}
    response = db[collection].update_one(query,setting)
    return response

def delete_data (coll, query, database = db):
    '''
    Delete objects in a collection

    Receives:

        - coll (string) the collection in which we want to perform the elimination
        - query (mongo format) to determine the objects we want to delete
        - database (database) the database that contains our collections

    Returns:
        The elements of our collection that we are eliminating
    '''
    deletion = database[coll].remove(query)
    return deletion

def push_coll(collection, query, update,database = db):
    setting = {"$push":update}
    res = db[collection].update_one(query,setting)
    return res

def update_general():
    '''
    Perform an aggregation query for each of our API collections 
    (philosophy, biology and literature) and join them

    Returns:
        New collection called Quote_Author
    '''
    mix_coll = db.Biology.aggregate( [
                        { '$unionWith': "Philosophy"},
                        { '$unionWith': "Literature"},   
                        { '$project': { '_id': 1, "Quote":1, "Author":1, "Category":1, "Gender":1}},
                        { '$out' : "Quote_Author" } ])
    return mix_coll

