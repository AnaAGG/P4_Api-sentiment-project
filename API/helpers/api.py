from flask import Flask, request, jsonify
from bson import json_util
from pymongo import MongoClient
from biology import  list_authors_bio, delete_biology, insert_quote_bio
from mongoConnections import read_data, delete_data, get_authors, get_quotes, update_general
from literature import insert_quote_lit, list_authors_lit, delete_literaty, update_literature
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


##DELETE objeos en una colleccion
@app.route("/Biology/delete") #FUNCIONA, elimina un determinardo autor
def biology_delete():
    args = dict(request.args)
    json_util.dumps(delete_biology(args))
    update_general()
    return "Nice!!! the author has been deleted"

@app.route("/Literature/delete") #FUNCIONA, elimina un determinardo autor
def literature_delete():
    args = dict(request.args)
    json_util.dumps(delete_literaty(args))
    update_general()
    return "Nice!!! the author has been deleted"

#INSERT insertar objetos nuevos en una colleccion
@app.route("/Biology/new") #FUNCIONA
def biology_new():
    args = dict(request.args)
    json_util.dumps(insert_quote_bio(args, "Biology"))
    update_general()
    return "Nice!!! the author has been included"
@app.route("/Literature/new") #FUNCIONA
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