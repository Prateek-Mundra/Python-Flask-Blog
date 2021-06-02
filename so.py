from flask import Flask
from flask.json import jsonify
from flask.templating import render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def get_data():
    url = "http://api.tvmaze.com/search/shows?q=girls"
    # data = requests.get(url)
    data=json.load(requests.get(url))
    return data

if __name__ == "__main__":
    app.run(debug = True, port = 3030)
