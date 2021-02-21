from mongoConnections import insert_data, read_data, update_data, delete_data
from check import check_author, check_parameters
from bson import ObjectId



def list_authors_lit():
    res = read_data({}, {"Author":1, "_id":0}, "Literature" )
    return res

def insert_quote_lit(obj, coll): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    query = {"Quote":obj['Quote']}    
    if check_author(query, "Literature"):
        return "The quote you are trying to insert is in our database"
    if not check_parameters(obj, ["Quote", "Author"]):
         return "Bad request, Quote and Author are mandatory parameters"
    else:
        response = insert_data("Literature", obj)
    return response.inserted_id

def delete_literaty(obj): # donde las key del diccionario seran los documentos de cada objeto de nuestra coleccion
    query = {"Author":obj['Author']}  

    if not check_author(query, "Literature"):
        return "The Author you are trying to delete is not in our database"
    if not check_parameters(obj, ["Author"], ["Quote"]):
         return "Author and Quote are mandatory parameters"
    else:
        delete_data("Literature", query)
    return "Author successfully deleted"

def update_literature(obj):
    query= {"_id":ObjectId(obj["id"])}
    obj.pop("id")   
    if not check_author(query, "Literature"):
        return "The Author you are trying to delete is not in our database"
    if not check_parameters(obj, ["Author", "Quote"]):
         return {"Author and Quote are mandatory parameters"}
    else:
        update_data("Literature", query, obj)
    return "Author successfully updated"