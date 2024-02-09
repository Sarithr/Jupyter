from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['Employee']
print("Database created........")
print("List of databases after creating new one")
print(client.list_database_names())
collection = db['EmployeeDetails']
print("Collection created......")