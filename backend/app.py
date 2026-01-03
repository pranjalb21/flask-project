from flask import Flask, jsonify, request
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
load_dotenv()

app = Flask(__name__)

DB_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
client = MongoClient(DB_URI)
db = client.get_database(DB_NAME)
collection = db["items"]

result = [
    {
        "slno": 1,
        "name": "Item 1"
    },
    {
        "slno": 2,
        "name": "Item 2"
    },
    {
        "slno": 3,
        "name": "Item 3"
    }
]

@app.route('/api/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = dict(request.json)
    collection.insert_one(dict(data))
    return 'Todo submitted successfully'


@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = dict(request.json)

    collection.insert_one(dict(data))
    
    return 'Data submitted successfully'

@app.route('/api/view', methods=['GET'])
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']
    data = {
        'data': data
    }

    return data

@app.route('/api', methods=['GET'])
def get_result():
    return jsonify({"result": result}), 200

@app.route('/')
def home():
    return 'Hello world '

if __name__ == '__main__':
    port = int(os.getenv('BACKEND_PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)