# wsgi.py
from flask import Flask
from flask import jsonify
from json import dumps
from flask import request

app = Flask(__name__)

the_products = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' }
]

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products/<id>',methods=['GET','DELETE'])
def manage_product(id):
    print(request.method)
    if (request.method=='GET'):
        for element in the_products:
            if element["id"]==int(id):
                return jsonify(element)
            else:
                return "element non trouve : "+id
    elif (request.method=='DELETE'):
        for i in range(len(the_products)):
            if the_products[i]["id"]==int(id):
                del(the_products[i])
        return "methode DELETE  : "+str(id)+" supprimé"
    else:
        return "methode inconnue"+request.method

@app.route('/api/v1/products',methods=['GET', 'POST','PATCH'])
def get_post_products():
    if (request.method=='GET'):
        return jsonify(the_products)
    elif (request.method=='POST'):
        data=request.json
        the_products.append(data)
        return "methode POST  : "+str(request.data)+" ajouté"
    elif (request.method=='PATCH'):
        data=request.json
        for element in the_products:
            if element["id"]==int(data["id"]):
                element["name"]=data["name"]
        return "methode PATCH  : "+str(request.data)+" patché"
    else:
        return "methode inconnue"+request.method

