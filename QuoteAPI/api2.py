from flask import Flask, request, jsonify
from bson import json_util
from pymongo import MongoClient
from mongo import read_data, delete_data, update_general
from bson import ObjectId
from endpoints import delete, insert, complete_list, update, complete_auth

app = Flask("quoteapi")

@app.route('/') #Homepage
def home():
    return "Welcome! This site is a prototype API for famous quotes :)" 

@app.route("/Data") #to obtain all the information about authors, categories and phrases from our entire database
def data():
    read = complete_list()
    return jsonify(read)

@app.route("/AuthorAndQuote") #to obtain all the authors of the API
def data_aut():
    read = complete_auth()
    return json_util.dumps(read)


@app.route("/Authors/<Collection>") #to get all the authors contained in a given collection
def all_names(Collection):
    aut = read_data({}, {"Author":1, "_id": 0}, f"{Collection}")
    return json_util.dumps(aut)

@app.route("/Quotes/<Collection>") #to get all the phrases contained in a given collection
def all_quotes(Collection):
    aut = read_data({}, {"Quote":1, "_id": 0}, f"{Collection}")
    return json_util.dumps(aut)

##DELETE objeos en una colleccion
@app.route("/<collection>/delete") #Delete a certain author and his / her quote from the biology collection
def delete_prueba(collection):
    args = dict(request.args)
    x = json_util.dumps(delete(args, collection))
    update_general()
    return x

@app.route("/<collection>/new") # Insert a new author and his citation from the biology collection
def insert_new(collection):
    args = dict(request.args)
    x = json_util.dumps(insert(args, collection))
    update_general()
    return x

@app.route("/<collection>/update")
def update_lit(collection):
   args = dict(request.args) 
   x = json_util.dumps(update(args, collection))
   update_general()
   return x

app.run(debug=True)


 