import unittest, logging
from pymongoclass import MongoConnector
import socket
from bson import ObjectId

class PyMongoTestCase(unittest.TestCase):
	def setup(self):
		logging.basicConfig(level = logging.DEBUG)
		socket.getaddrinfo('localhost', 8080)

	def testSaveData(self):
		data = {"collection":
			{"Employee" : 
			{"id" : "06",
			"name" : "Rakshana",
			"service" : "Packager",
			"address" : "Mettupalayam",
			"dob" : "30-12-1991",
			"salary" : "46000"}}}	
		insertData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataInserted, responseMessage = insertData.saveObject(data)	
		self.assertTrue(isDataInserted)
		self.assertEquals(responseMessage, "Data Inserted Successfully")

	def testValidateSaveData(self):
		data = {"collection":
			{"Employee" : 
			{"id" : "06",
			"name" : "Rakshana",
			"service" : "Packager",
			"address" : "Mettupalayam",
			"dob" : "30-12-1991",
			"salary" : "46000"}}}		
		insertData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		insertData.saveObject(data)

	def testFindData(self):
		query = {"collection" : { "Employee" : {"id" : "06"}}}
		filterData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		findData, isDataFiltered, responseMessage = filterData.getObject(query)
		keysList = []
		for i in findData.keys():
			valuesList = findData.get(i)
			keysList.append(valuesList)
		self.assertEquals(keysList, [ObjectId('60b76a8fa2ab61954c257be0'), '06', 'Rakshana', 'Packager', 'Mettupalayam', '26-04-1992', '46000'])
		self.assertTrue(isDataFiltered)
		self.assertEquals(responseMessage, "Data filtered successfully")

	def testUpdateData(self):
		updationId = {"collection" : {"Employee" : {"id" : "06"}}}
		updation = {"$set" : {"dob" : "26-04-1992"}}
		updateData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataUpdated, responseMessage = updateData.updateObject(updationId, updation)
		self.assertTrue(isDataUpdated)
		self.assertEquals(responseMessage, "Data Updated Successfully")

	def testDeleteData(self):
		deletion = {"collection" : {"Employee" : {"id" : "03"}}}
		deleteData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataDeleted, responseMessage = deleteData.deleteObject(deletion)
		self.assertTrue(isDataDeleted)
		self.assertEquals(responseMessage, "Data Deleted Successfully")
	
	def testSaveDataWithoutData(self):
		data = {}
		insertData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataInserted, responseMessage = insertData.saveObject(data)	
		self.assertFalse(isDataInserted)
		self.assertEquals(responseMessage, "Provide valid data to insert")		

	def testSaveDataWithoutValues(self):
		data = {"collection": {"Employee" : {}}}
		insertData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataInserted, responseMessage = insertData.saveObject(data)	
		self.assertFalse(isDataInserted)
		self.assertEquals(responseMessage, "Provide all valid values to insert")
	
	def testSaveDataWithoutKeyValue(self):
		data = {"collection":
			{"Employee" : 
			{"id" : "",
			"name" : "Rakshana",
			"service" : "Packager",
			"address" : "Mettupalayam",
			"dob" : "30-12-1991",
			"salary" : "46000"}}}
		insertData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataInserted, responseMessage = insertData.saveObject(data)	
		self.assertFalse(isDataInserted)
		self.assertEquals(responseMessage, "Provide valid values to insert")

	def testFindDataWithoutData(self):
		query = {}
		filterData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		findData, isDataFiltered, responseMessage = filterData.getObject(query)
		keysList = []
		for i in findData.keys():
			valuesList = findData.get(i)
			keysList.append(valuesList)
		self.assertEquals(keysList, [])
		self.assertFalse(isDataFiltered)
		self.assertEquals(responseMessage, "Provide valid data to filter")

	def testFindDataWithoutValues(self):
		query = {"collection" : { "Employee" : {}}}
		filterData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		findData, isDataFiltered, responseMessage = filterData.getObject(query)
		keysList = []
		for i in findData.keys():
			valuesList = findData.get(i)
			keysList.append(valuesList)
		self.assertEquals(keysList, [])
		self.assertFalse(isDataFiltered)
		self.assertEquals(responseMessage, "Provide all valid values to filter")

	def testFindDataWithoutKeyValue(self):
		query = {"collection" : { "Employee" : {"id" : ""}}}
		filterData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		findData, isDataFiltered, responseMessage = filterData.getObject(query)
		keysList = []
		for i in findData.keys():
			valuesList = findData.get(i)
			keysList.append(valuesList)
		self.assertEquals(keysList, [])
		self.assertFalse(isDataFiltered)
		self.assertEquals(responseMessage, "Provide valid values to filter")		

	def testUpdateDataWithoutUpdationId(self):
		updationId = {}
		updation = {"$set" : {"dob" : "26-04-1992"}}
		updateData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataUpdated, responseMessage = updateData.updateObject(updationId, updation)
		self.assertFalse(isDataUpdated)
		self.assertEquals(responseMessage, "Provide valid updationId to update")

	def testUpdateDataWithoutUpdation(self):
		updationId = {"collection" : {"Employee" : {"id" : "06"}}}
		updation = {}
		updateData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataUpdated, responseMessage = updateData.updateObject(updationId, updation)
		self.assertFalse(isDataUpdated)
		self.assertEquals(responseMessage, "Provide valid updation to update")

	def testUpdateDataWithoutUpdationIdValues(self):
		updationId = {"collection" : {"Employee" : {}}}
		updation = {"$set" : {"dob" : "26-04-1992"}}
		updateData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataUpdated, responseMessage = updateData.updateObject(updationId, updation)
		self.assertFalse(isDataUpdated)
		self.assertEquals(responseMessage, "Provide all valid updationId to update")

	def testUpdateDataWithoutUpdationValues(self):
		updationId = {"collection" : {"Employee" : {"id" : "06"}}}	
		updation = {"$set" : {}}
		updateData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataUpdated, responseMessage = updateData.updateObject(updationId, updation)
		self.assertFalse(isDataUpdated)
		self.assertEquals(responseMessage, "Provide all valid updation to update")

	def testUpdateDataWithoutUpdationIdKeyValue(self):
		updationId = {"collection" : {"Employee" : {"id" : ""}}}
		updation = {"$set" : {"dob" : "26-04-1992"}}
		updateData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataUpdated, responseMessage = updateData.updateObject(updationId, updation)
		self.assertFalse(isDataUpdated)
		self.assertEquals(responseMessage, "Provide valid updationId values to update")

	def testUpdateDataWithoutUpdationKeyValue(self):
		updationId = {"collection" : {"Employee" : {"id" : "06"}}}
		updation = {"$set" : {"dob" : ""}}
		updateData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataUpdated, responseMessage = updateData.updateObject(updationId, updation)
		self.assertFalse(isDataUpdated)
		self.assertEquals(responseMessage, "Provide valid updation values to update")	

	def testDeleteDataWithoutData(self):
		deletion = {}
		deleteData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataDeleted, responseMessage = deleteData.deleteObject(deletion)
		self.assertFalse(isDataDeleted)
		self.assertEquals(responseMessage, "Provide valid data to delete")

	def testDeleteDataWithoutValues(self):
		deletion = {"collection" : {"Employee" : {}}}
		deleteData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataDeleted, responseMessage = deleteData.deleteObject(deletion)
		self.assertFalse(isDataDeleted)
		self.assertEquals(responseMessage, "Provide all valid values to delete")			
	
	def testDeleteDataWithoutKeyValue(self):
		deletion = {"collection" : {"Employee" : {"id" : ""}}}
		deleteData = MongoConnector("localhost", 27017, "Employee", "EmployeeDetails")
		isDataDeleted, responseMessage = deleteData.deleteObject(deletion)
		self.assertFalse(isDataDeleted)
		self.assertEquals(responseMessage, "Provide valid values to delete")