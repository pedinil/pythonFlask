from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def first_route():
    return "test"


@app.route('/add', methods=["POST"])
def add_two():
    dataGet = request.get_json()
    x = dataGet["x"]
    y = dataGet["y"]
    z = x + y
    retJSON = {
        "z": z
    }
    return jsonify(retJSON), 200


@app.route('/jsonrequest')
def json_route():
    test = {
        'name': 'pedram',
        'ag': 20
    }
    return jsonify(test)


if __name__ == "__main__":
    app.run(host='0.0.0.0')