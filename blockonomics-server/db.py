import bson

from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

import os

from flask import Flask, render_template
from flask.json import JSONEncoder
from flask_cors import CORS
##from flask_bcrypt import Bcrypt
##from flask_jwt_extended import JWTManager

from bson import json_util, ObjectId
from datetime import datetime, timedelta


def get_db():
    """
    Configuration method to return db instance
    """
    
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = PyMongo(current_app).db

    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def add_comment(data):
    """
    Inserts a comment into the comments collection, with the following fields:
    - "name"
    - "email"
    - "movie_id"
    - "text"
    Name and email must be retrieved from the "user" object.
    """
    comment_doc = {
        'uuid': data["uuid"],
        'name': data["name"],
        "sender_add": data["address"],
        'sender_email': data["emailid"],
        'message': data["Message"],
        'value': data["paid_satoshi"],
        'timestamp': data["timestamp"],
    }
    return db.Donation_msg.insert_one(comment_doc)


def get_comment_largest_value():
    result = db.Donation_msg.find().sort({"value": -1,"timestamp":1}).limit(1)[0]
    return result

class MongoJsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, 'build/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, 'build')

    app = Flask(
        __name__,
        static_folder=STATIC_FOLDER,
        template_folder=TEMPLATE_FOLDER,
    )
    CORS(app)
    app.json_encoder = MongoJsonEncoder

    return app