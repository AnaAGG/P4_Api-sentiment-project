from mongo import insert_data, read_data, update_data, delete_data
from check import check_author, check_parameters
from bson import ObjectId


def complete_list():
    res = read_data({}, {"Author":1, "Quote":1, "Category":1, "_id":0}, "Quote_Author" )
    return res