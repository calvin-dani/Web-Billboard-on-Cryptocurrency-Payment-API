from flask import Flask,request,jsonify
import requests
import os
import configparser
from db_analytics import get_comment_largest_value
from pymongo import MongoClient
from flask_apscheduler import APScheduler
from flask_cors import CORS, cross_origin
from flask_caching import Cache

app2 = Flask(__name__)
cache = Cache(app2)
app2.config['CORS_HEADERS'] = "Content-Type"
ALLOWED_ORIGINS = ['localhost', '127.0.0.1']

cors = CORS(app2, resources={"/*": {"origins": ALLOWED_ORIGINS}})

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))
result = None

#Get max valued message
@app2.route("/get_message",methods=["GET"])
@cross_origin()
def get_message_max_value():
    with app2.app_context():
        result = get_comment_largest_value()
        if result:
            return result,200
        else:
            return result,500

if __name__ == '__main__':
    # run app in debug mode on port 5005
    app2.config['DEBUG'] = True
    app2.config['MONGO_URI'] = config['PROD']['DB_URI']

    app2.run(debug=False, port=config['PROD']['PORT'])
