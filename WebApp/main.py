from flask import Flask
from markupsafe import escape
import pymongo
from pymongo import MongoClient
import json
from bson.json_util import dumps

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World:-D'

@app.route("/<name>")
def hello(name):
	return f"Hello, {escape(name)}!"

@app.route('/mongoDB')
def mongoRead():
	client = MongoClient()
	collection = client.can_data.edge_device
	findResults = collection.find()
	print("hello")
	print(type(findResults))
	result = ""
	for doc in findResults:
		element = dumps(doc)
		print(type(element))
		result += element
		result += "<br>"
		print(element)
	return result

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000)

