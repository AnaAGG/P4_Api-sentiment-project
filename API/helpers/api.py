from flask import Flask, request
from bson import json_util
from pymongo import MongoClient
from biology import insert_biology, list_authors_bio, get_info_bio, delete_biology
from mongoConnections import read_data, delete_data
from literature import insert_literaty, list_authors_lit, delete_literaty
from bson import ObjectId

app = Flask("quoteapi")


@app.route('/') #ESTA FUNCIONA
def home():
    return "Welcome! This site is a prototype API for famous quotes" #Se mostrará este mensaje cuando arrancas la API


@app.route("/Quotes/<Collection>") #return every quote in a given collection TENDRIA QUE REVISARLA
def quote(Collection): #ESTA FUNCIONA
    proj={"Quote":1}
    read  = read_data({}, f"{Collection}", project=proj)
    return json_util.dumps(read)

@app.route("/Biology")#devuelve todos los autores de Biologia FUNCIONA
def biologist():
    return json_util.dumps(list_authors_bio())


@app.route("/Literature")#devuelve todos los autores de Literatura FUNCIONA
def literaty():
    return json_util.dumps(list_authors_lit())



##DELETE
@app.route("/biology/delete") #FUNCIONA, elimina un determinardo id
def biology_delete():
    args = dict(request.args)
    id = delete_literaty(args, "Literature")
    json_util.dumps({"_id":id})
    return "The author's quote has been removed from the dayos database"


@app.route("/literature/delete") #FUNCIONA, elimina un determinardo id
def literature_delete():
    args = dict(request.args)
    id = delete_literaty(args, "Literature")
    json_util.dumps({"_id":id})
    return "The author's quote has been removed from the dayos database"

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