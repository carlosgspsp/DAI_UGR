#./app/app.py

from ast import Num
from bson.json_util import dumps
from pymongo import MongoClient
from flask import request, jsonify
from bson import ObjectId

from flask import Flask, Response
from flask import render_template

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles



# Practica 2.1
@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find() # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_de/<alimento>')
def mongo2(alimento):
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find({"name": str(alimento)}) # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_con/<alimento>')
def mongo3(alimento):
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find({'ingredients.name': alimento})  # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')


@app.route('/recetas_de/<int:num>/ingredientes')
def mongo4(num):
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find({'ingredients': {"$size": num}})  # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')







# Practica 2.2
@app.route('/', methods=['GET', 'POST'])
def api_5():
    return render_template('interfaz.html')


# para devolver una lista (GET), o añadir (POST)
@app.route('/api/recipes', methods=['GET', 'POST'])
def api_1():
    if request.method == 'GET':
        
        if "con" in request.args.keys():
            buscados = db.recipes.find({"ingredients.name": request.args.get('con')})
        else:
            buscados = db.recipes.find().sort('name')     

        lista = []
        for recipe in buscados:
            recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
            lista.append(recipe)
        return jsonify(lista)

    if request.method == 'POST':
        nueva_receta = {
            "name": request.json['name'],
            "ingredients": request.json['ingredients'],
            "instructions": request.json['instructions']
        }
        db.recipes.insert_one(nueva_receta)
        return dumps(nueva_receta)



@app.route('/api/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    #Metodo usada para devolver una receta dado el ID
    if request.method == 'GET':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            return jsonify(buscado)
        else:
            return jsonify({'error':'Receta no encontrada'}), 404
    #Metodo usado para editar una receta dado el ID
    if request.method == 'PUT':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            db.recipes.update_one(buscado, {"$set":{
                                                'name':request.json['name'],
                                                'ingredients':request.json['ingredients'], 
                                                'instructions': request.json['instructions']}})
            buscado_modificado = db.recipes.find_one({'_id':ObjectId(id)})
            return dumps(buscado_modificado)
        else:
            return jsonify({'error':'Receta no encontrada'}), 404
    #Metodo usado para borrar una receta dado el ID
    if request.method == 'DELETE':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            db.recipes.delete_one(buscado)
            return jsonify("Receta borrado")
        else:
            return jsonify({'error':'Receta no encontrada'}), 404 

@app.errorhandler(404)
def pagina_no_encontrada(error):

    return	'Pagina no encontrada'