import pymongo
from pymongo import MongoClient
import dns
import datetime

print(pymongo.version)

client = pymongo.MongoClient("mongodb+srv://AdiLaptop:asdAhagYHNUOzVmk@visanariesdb-942zb.mongodb.net/VisanariesDB?retryWrites=true&w=majority")
db = client.main

people = db.people

# personDocument = {
#   "name": { "first": "TEST_FIRST_2", "last": "TEST_LAST_2" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }

# people.insert_one(personDocument)

# print(people.find_one({ "name.last": "TEST_LAST" }))
