from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if (request.method == "GET"):
        return jsonify({"default message": "Hello World!"})
    elif (request.method == "POST"):
        json_received = request.get_json()
        return jsonify({"your message": json_received}), 201

@app.route("/multiply/<int:num1>/<int:num2>", methods = ["GET"])
def multiply(num1, num2):
    return jsonify({"Product": num1 * num2})

if (__name__ == "__main__"):
    app.run(debug = True)
