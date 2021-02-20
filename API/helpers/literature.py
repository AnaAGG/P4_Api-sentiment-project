from mongoConnections import insert_data, read_data, update_data, delete_data
from check import check_author
from bson import ObjectId



def list_authors_lit():
    res = read_data({}, "Literature", project={"_id":0})
    response = {c["Author"]:str(c["_id"]) for c in res}
    return response

def insert_literaty(obj, coll): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    query = {"Author":obj['Author']}    
    if check_author(query, "Literature"):
        return "Sorry, the author already exists"
    else:
        response = insert_data("Literature", obj)
    return response.inserted_id

def delete_literaty(obj, coll): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    query = {"Author":obj['Author']}    
    if not check_author(query, "Literature"):
        return "The Author you are trying to delete is not in our database"
    else:
        response = delete_data("Literature", obj)
    return response.inserted_id