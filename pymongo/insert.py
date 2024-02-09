from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client.mydb
print(type(client))
print(type(db))
#Creating a collection
coll = db.example
print(type(db))
print(type(coll))
#Inserting document into a collection
doc1 = {"name": "Ram", "age": "26", "city": "Hyderabad"}
coll.insert_one(doc1)
print(coll.find_one())