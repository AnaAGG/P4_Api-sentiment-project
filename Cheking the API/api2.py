from flask import Flask, request, jsonify
from bson import json_util
from pymongo import MongoClient
from biology import  list_authors_bio, delete_biology, insert_quote_bio
from mongo import read_data, delete_data, update_general
from literature import insert_quote_lit, list_authors_lit, delete_literaty, update_literature
from QuoteAuthors import complete_list
from bson import ObjectId

app = Flask("quoteapi")

@app.route('/') #Homepage
def home():
    return "Welcome! This site is a prototype API for famous quotes" 

@app.route("/Data") #to obtain all the information about authors, categories and phrases from our entire database
def data():
    read = complete_list()
    return jsonify(read)

@app.route("/Authors/<Collection>") #to get all the authors contained in a given collection
def all_names(Collection):
    aut = read_data({}, {"_id":0, "Subcategory": 0, "Quote": 0, "Category": 0, "Book": 0}, f"{Collection}")
    return jsonify(aut)

@app.route("/Quotes/<Collection>") #to get all the phrases contained in a given collection
def all_quotes(Collection):
    aut = read_data({}, {"_id":0, "Subcategory": 0, "Author": 0, "Category": 0, "Book": 0}, f"{Collection}")
    return jsonify(aut)


##DELETE objeos en una colleccion
@app.route("/Biology/delete") #Delete a certain author and his / her quote from the biology collection
def biology_delete():
    args = dict(request.args)
    json_util.dumps(delete_biology(args))
    update_general()
    return "Nice!!! the author has been deleted"

@app.route("/Literature/delete") # Remove a certain author and his / her citation from the literature collection
def literature_delete():
    args = dict(request.args)
    json_util.dumps(delete_literaty(args))
    update_general()
    return "Nice!!! the author has been deleted"

#INSERT insertar objetos nuevos en una colleccion
@app.route("/Biology/new") # Insert a new author and his citation from the biology collection
def biology_new():
    args = dict(request.args)
    json_util.dumps(insert_quote_bio(args, "Biology"))
    update_general()
    return "Nice!!! the author has been included"

@app.route("/Literature/new") # Insert a new author and his citation from the literature collection
def literaty_new():
    args = dict(request.args)
    json_util.dumps(insert_quote_lit(args, "Literature"))
    update_general()
    return "Nice!!! the author has been included"

app.run(debug=True)




#UPDATE
@app.route("/update/literature")
def update_lit():
   args = dict(request.args) 
   return json_util.dumps(update_literature(args))