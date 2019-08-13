from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


#__name__ gives each file a unique name 
app = Flask(__name__)
app.secret_key = 'Jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth
items = [] # dictionary

class Item(Resource):
    #200 ok
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    #201 created 
    def post(self, name):
        #force means your api doesn't need the application/json header
        #it will assume that the data is json and will try to format it to json as possible
        #
        #silent means on case of error, do not show errors and only return null
        # data = request.get_json(force=True)
        # data = request.get_json(silent=True)
        
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return { 'message' : "An item with name '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {
            'name': name,
            'price': data['price']
            }
        items.append(item)
        return items, 201 #originally item not items

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message' : 'Item deleted'}

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = { 'name': name, 'price': data['price']}
            items.append(item)
        else:
            items.update(item)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

    


api.add_resource(Item, '/item/<string:name>') # so we create a whole class that contain the whole crud operations except the get many? and then assign it to that add_resource function/middleware???
api.add_resource(ItemList, '/items/')

app.run(port=5000, debug=True)

