from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask.json import JSONEncoder
from bson import json_util, ObjectId
from datetime import datetime


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = PyMongo(current_app).db
        db.Donation_msg.create_index("value")
    return db

# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

#Querying the max valued message
def get_comment_largest_value():
    result = db.Donation_msg.find().sort("value",-1).limit(1)[0]
    return json_util.dumps(result) if result else {"message":""}

class MongoJsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)
