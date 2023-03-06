from flask import Flask, request
import requests
import os
import configparser
from db import add_comment
from payload_utils import parse_transaction_payload, return_status
from pymongo import MongoClient


app1 = Flask(__name__)

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


#Open to bloconomics as a callback endpoint
@app1.route("/store_transaction", methods=["GET"])
def transaction_handler():
    uuid = request.args.get('uuid')
    status = request.args.get('status')
    #Check if payment is successfull
    if return_status(status):
        #Fetch all the details of the transaction
        endpoint, headers = set_endpoint_metadata(uuid)
        payload = requests.get(endpoint, headers=headers).json()
        data = parse_transaction_payload(payload)
        with app1.app_context():
            #Add the transaction detalils to mongodb
            add_comment(data)
    return "Got the callback",200


def set_endpoint_metadata(uuid):
    return config['PROTO']["GET_TRANSACTION_URL"] + uuid, {
        "Authorization": "Bearer " + config['PROTO']["BEARER_TOKEN"]
    }

if __name__ == '__main__':
    # run app in debug mode on port 5003
    # app = create_app()
    app1.config['DEBUG'] = True
    app1.config['MONGO_URI'] = config['PROTO']['DB_URI']
    print(config['PROTO']['DB_URI'])

    # CONNECTION_STRING = config['PROD']['DB_URI']

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    # client = MongoClient(CONNECTION_STRING)

    app1.run(debug=True, port=config['PROTO']['PORT'])
