from mongo import insert_data, read_data, update_data, delete_data
from check import check_author, check_parameters
from bson import ObjectId

def list_authors_bio():
    res = read_data({}, {"Author":1, "_id":0}, "Biology" )
    return res

def insert_quote_bio(obj, coll): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    query = {"Quote":obj['Quote']}    
    if check_author(query, "Biology"):
        return "The quote you are trying to insert is in our database"
    if not check_parameters(obj, ["Quote", "Author"]):
         return "Bad request, Quote and Author are mandatory parameters"
    else:
        response = insert_data("Biology", obj)
    return response.inserted_id

def delete_biology(obj): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    query = {"Author":obj['Author']}    
    if not check_author(query, "Biology"):
        return f"The Author you are trying to delete is not in our database"
    if not check_parameters(obj, ["Author", "Quote"]):
        return "Bad request, Author are mandatory parameters"
    else:
        delete_data("Biology", obj)
    return "Author successfully deleted"