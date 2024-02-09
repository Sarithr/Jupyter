from pymongo import MongoClient
import logging

logging.basicConfig(level = logging.DEBUG)

logging.info("A Python Mongo Connector")
class MongoConnector:
	def __init__(self, host, port, db, coll):
		self.host = host
		self.port = port
		self.db = db
		self.coll = coll
		self.client = MongoClient(host = self.host, port = self.port)

	def saveObject(self, data):
		logging.info("Inserting data")
		try:
			db = self.client[self.db]
			coll = db[self.coll]
			coll.insert_one(data.get("collection"))
			logging.debug("Data Inserted")
		except:
			logging.exception("Unable to insert the Data")	

	def getObject(self, query):
		logging.info("Finding data")
		try:
			db = self.client[self.db]
			coll = db[self.coll]		
			logging.debug(coll.find_one(query.get("collection")))
			logging.debug("Data Returned")
		except:
			logging.exception("Unable to get the data")	

	def updateObject(self, updationId, updation):
		logging.info("Updating data")
		try:
			db = self.client[self.db]	
			coll = db[self.coll]
			coll.update_one(updationId.get("collection"), updation)
			logging.debug("Data Updated")
		except:
			logging.exception("Unable to update the Data")
		
	def deleteObject(self, deletion):
		logging.info("Deleting data")
		try:
			db = self.client[self.db]	
			coll = db[self.coll]
			coll.delete_one(deletion.get("collection"))
			logging.debug("Data Deleted")
		except:
			logging.exception("Unable to delete the Data")	
	
data = {"collection":
	{"Employee" : 
	{"id" : "05",
	"name" : "Prathiksha",
	"service" : "Security Checker",
	"address" : "Coimbatore",
	"dob" : "08-02-1993",
	"salary" : "55000"}}}

query = {"collection" : {"Employee" : {"name" : "Keerthana"}}}	

updationId = {"collection" : {"Employee" : {"id" : "05"}}}
updation = {"$set" : {"salary" : "57000"}}

deletion = {"collection" : {"Employee" : {"id" : "03"}}}

detailsObject = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
detailsObject.saveObject(data)
detailsObject.updateObject(updationId, updation)
detailsObject.deleteObject(deletion)

