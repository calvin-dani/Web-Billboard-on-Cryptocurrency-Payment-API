from flask import Flask, request
import requests
import os
import configparser
from db import add_message_transaction
from payload_utils import parse_transaction_payload, return_status
from pymongo import MongoClient

#binding Flask application  
app1 = Flask(__name__)

#Fetching values from .ini files
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


#Open to blockonomics as a webhook endpoint
@app1.route("/store_transaction", methods=["GET"])
def transaction_handler():
    uuid = request.args.get('uuid')
    status = request.args.get('status')
    #Check if payment is successfull
    if return_status(status):
        #Fetch the details of the transaction
        endpoint, headers = set_endpoint_metadata(uuid)
        payload = requests.get(endpoint, headers=headers).json()
        #Parsing response
        data = parse_transaction_payload(payload)
        with app1.app_context():
            #Add the transaction detalils to mongodb
            add_message_transaction(data)
    return "Got the callback",200

#Returns URL to fetch transaction details
def set_endpoint_metadata(uuid):
    return os.getenv('GET_TRANSACTION_URL') + uuid, {
        "Authorization": "Bearer " + os.getenv('BEARER_TOKEN')
    }


if __name__ == '__main__':
    # run app in debug mode on port 5003
    app1.config['DEBUG'] = False
    app1.config['MONGO_URI'] = os.getenv('DB_URI')

    app1.run(debug=False, port=os.getenv('PORT'))
