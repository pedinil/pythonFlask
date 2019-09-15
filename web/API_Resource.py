from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
from pymongo import  MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNameDB
UserNum = db ["UserNum"]

UserNum.insert_one({
    'num_of_users' : 0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num =  prev_num + 1
        UserNum.update_one({} , {"$set" :{"num_of_users":new_num}})
        return str('helloworld' + str (new_num))


class Add(Resource):
    def post(self):
        postdata = request.get_json()
        x = postdata["x"]
        y = postdata["y"]
        ret = x + y
        retmap = {
            'Message' : ret,
            'Status Code' : 200

        }
        return jsonify(retmap)




#adding resouce to API
api.add_resource(Add , "/add")
api.add_resource(Visit , "/hello")

@app.route('/')
def first_route():
    return "helloworld"




if __name__ == "__main__":
    app.run(host='0.0.0.0')
