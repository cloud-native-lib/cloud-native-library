import db
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/listbook')
def hello_world():
    return jsonify(db.all_titles())