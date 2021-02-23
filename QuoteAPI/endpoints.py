from mongo import insert_data, read_data, update_data, delete_data, update_general, push_coll
from check import check_author, check_parameters
from bson import ObjectId


def complete_list():
    res = read_data({}, {"_id":0}, "Quote_Author" )
    return res


def complete_auth():
    res = read_data({}, {"Author": 1}, "Quote_Author" )
    return res

def delete(obj,Collection):

    if not check_parameters(obj,['id']):
        return {"response":400,"message":"Bad Request: 'Quote', 'Author' and 'Gender' is an obligatory parameter"}

    query = {"_id":ObjectId(obj['id'])}
    if not check_author(query, f"{Collection}"):
        return {" Bad Request: with given id does not exist"}

    delete_data(f"{Collection}",query)
    return {"Quote successfully deleted"}


def insert(obj,Collection):

    if not check_parameters(obj,["Quote", "Author", "Gender"]):
        return {"Sorry: 'Quote', 'Author' and 'Gender' is an obligatory parameter"}

    query = {"Quote":obj['Quote']}

    if check_author(query,Collection):
        return {"Sorry: Bad Request: there is already this quote"}
    insert_data(obj, f"{Collection}")
    return {"Quote successfully inserted"}


def update(obj,Collection):

    if not check_parameters(obj,["id"]):
        return {"response":400, "message": "Bad request: 'id' is an obligatory parameter"}

    query = {"_id":ObjectId(obj['id'])}

    if not check_author(query,Collection):
        return {"response":400,"message": "Bad Request: there is already this quote"}
    obj.pop("id")
    update_data(f"{Collection}",query, update)
    return {"Quote successfully updated"}
