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

new_docs = [{
    # multi docs = array of dictionaries
    "first": "terry",
    "last": "pratchett",
    "dob": "28/04/1948",
    "gender": "m",
    "hair_color": "not much",
    "occuptation": "writer",
    "nationality": "british"
}, {
    "first": "george",
    "last": "rr martin",
    "dob": "02/09/1948",
    "gender": "m",
    "hair_color": "white",
    "occupation": "writer",
    "nationality": "american"
}]

coll.insert_many(new_docs)

documents = coll.find()
# MongoDB object = cursor

for doc in documents:
    print(doc)