import os
import pymongo
if os.path.exists("env.py"):
    # this imports env.py only if we have an env.py file in our root dir
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebrities"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e 


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

coll.find({"first": "douglas"})
# MongoDB object = cursor

documents = coll.find()

for doc in documents:
    print(doc)