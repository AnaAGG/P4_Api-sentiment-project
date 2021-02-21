from flask import Flask, request, jsonify
from bson import json_util
from pymongo import MongoClient
from biology import insert_biology, list_authors_bio, delete_biology
from mongoConnections import read_data, delete_data, get_authors, get_quotes
from literature import insert_literaty, list_authors_lit, delete_literaty
from bson import ObjectId

app = Flask("quoteapi")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/') #ESTA FUNCIONA
def home():
    return "Welcome! This site is a prototype API for famous quotes" #Se mostrará este mensaje cuando arrancas la API

@app.route("/Authors")
def all_names():
    aut = get_authors()
    return jsonify(aut)

@app.route("/Quotes")
def all_quotes():
    aut = get_quotes()
    return jsonify(aut)

@app.route("/Quotes/<Collection>") #return every quote in a given collection TENDRIA QUE REVISARLA
def quote(Collection): #ESTA FUNCIONA
    read  = read_data({}, {"_id":0, "Subcategory": 0, "Author": 0, "Section": 0, "Book": 0}, f"{Collection}")
    return jsonify(read)

@app.route("/Biology")#devuelve todos los autores de Biologia FUNCIONA
def biologist():
    return jsonify(list_authors_bio())


@app.route("/Literature")#devuelve todos los autores de Literatura FUNCIONA
def literaty():
    return jsonify(list_authors_lit())


##DELETE
@app.route("/biology/delete") #FUNCIONA, elimina un determinardo id
def biology_delete():
    args = dict(request.args)
    return json_util.dumps(delete_biology(args))


@app.route("/literature/delete") #FUNCIONA, elimina un determinardo id
def literature_delete():
    args = dict(request.args)
    return json_util.dumps(delete_literaty(args))

#INSERT
@app.route("/Quotes/Biology/new") #FUNCIONA
def biology_new():
    args = dict(request.args)
    id = insert_biology(args, "Biology")
    json_util.dumps({"_id":id})
    return "Nice!!! There is a new quote in the Biology collection"
@app.route("/Quotes/Literature/new") #FUNCIONA
def literaty_new():
    args = dict(request.args)
    id = insert_literaty(args, "Literature")
    json_util.dumps({"_id":id})
    return "Nice!!! There is a new quote in the Literature collection"
   
app.run(debug=True)