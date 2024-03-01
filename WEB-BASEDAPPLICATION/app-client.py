from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# GET REST API #
@app.route('/getuser/<idmemo>', methods=["GET"])
def get_user(idmemo):
    api_url = "http://localhost:5000/getuser/v1/"+idmemo
    response = requests.get(api_url)
    return jsonify(response.json()), response.status_code

@app.route('/postuser', methods=["GET"])
def post_user():
    data = {"firstname": "Vorameth", "lastname": "Patummasut", "enail": "s6507012662071@email.kmutnb.ac.th"}
    api_url = "http://localhost:5000/postuser"
    response = requests.post(api_url, json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5005", debug=True)