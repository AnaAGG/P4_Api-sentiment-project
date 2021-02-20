from mongoConnections import insert_data, read_data, update_data, delete_data
from check import check_author
from bson import ObjectId

def list_authors_bio():
    res = read_data({}, "Biology", project={"_id":0})
    response = {c["Author"]:str(c["_id"]) for c in res}
    return response


def get_info_bio(obj):
    q = {"_id":ObjectId(obj["id"])}
    if not check_author(q,"Biology"):
        return "Bad Request: quote with given id does not exist"
    else:
        return read_data("Biology",q)


def insert_biology(obj, coll): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    print(obj['Author'])
    query = {"Author":obj['Author']}    
    if check_author(query, "Biology"):
        return "Sorry, the author already exists"
    else:
        response = insert_data("Biology", obj)
    return response.inserted_id

def delete_biology(obj, coll): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    query = {"Author":obj['Author']}    
    if not check_author(query, "Biology"):
        return f"The Author you are trying to delete is not in our database"
    else:
        response = delete_data("Biology", obj)
    return response.inserted_id