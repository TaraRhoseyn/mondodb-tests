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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e 


def show_menu():
    print("") # leaves blank line on top
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option # the function will return the option variable that the user has selected



def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        # if there aren't any docs, it's empty
        print("")
        print("Error! No results found.")

    return doc


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality,
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")



def find_record():
    doc = get_record() # earlier function
    if doc: # return of function
        print("")
        for k,v in doc.items():
            if k != "_id": # k = key v = value
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    """
    Allows users to edit existing records. 
    Any inputs given will be the new values in the key/value pair.
    Any field left blank will return to the default value.
    """
    doc = get_record()
    if doc:
        update_doc = {}  # empty dictionary
        print("")
        for k,v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + "[" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v # setting key back to original value
        try:
            coll.update_one(doc,{"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()