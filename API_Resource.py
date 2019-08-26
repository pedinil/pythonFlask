from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


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

@app.route('/')
def first_route():
    return "helloworld"




if __name__ == "__main__":
    app.run()
