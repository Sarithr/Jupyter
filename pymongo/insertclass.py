from pymongo import MongoClient
import json

class EmployeeDetails:
	def __init__(self, host, port, db, coll):
		self.host = host
		self.port = port
		self.db = db
		self.coll = coll
		self.client = MongoClient(host = self.host, port = self.port)

	def saveEmployeeDetails(self):
		db = self.client[self.db]
		coll = self.db[self.coll]
		insertData = {"id" : "03", "name" : "Aparna", "service" : "Manager", "address" : "Ooty", "dob" : "16-08-1994", "salary" : "75000"}
		#{"id" : "04", "name" : "Gayathri", "service" : "Packager", "address" : "Thanjavur", "dob" : "09-03-1991", "salary" : "35000"}]
		self.coll.insert_one(insertData)
		print("Data Inserted")
		print(self.coll.find_one())

detailsObject = EmployeeDetails("localhost", 27017, "Employee", "EmployeeDetails")
detailsObject.saveEmployeeDetails()

