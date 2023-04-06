# This servers deals with querying data for insights. 
#In this case taking the message with the highest donation
# - get_message_max_value queries the mongoDb and returns the 
#       message with the highest donation 
from flask import Flask,request,jsonify
import os
import configparser
from db_analytics import get_comment_largest_value
from pymongo import MongoClient


analytics_app = Flask(__name__)

result = None
emptyResponse = {"message":"","name":""}

# Get max valued message
@analytics_app.route("/get_message",methods=["GET"])
def get_message_max_value():
    with analytics_app.app_context():
        result = get_comment_largest_value()
        if result:
            return result,200
        else:
            return emptyResponse,500

if __name__ == '__main__':
    # run app in on port 5005
    analytics_app.config['DEBUG'] = False
    analytics_app.config['MONGO_URI'] = os.getenv('DB_URI')
    analytics_app.run(debug=False, port=os.getenv('PORT'))
