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
		isDataInserted = False
		responseMessage = ''
		try:
			db = self.client[self.db]
			coll = db[self.coll]
			if (data != {}):
				collectionkey = data.get("collection")
				for k, v in data.items():
					v.keys()
					for i in v.keys():
						insertData = collectionkey.get(i)
						if (len(insertData) != 0):
							self.validateSaveObject(data)
							if (self.funcResult == True):
								coll.insert_one(insertData)
								logging.debug("Data Inserted")
								isDataInserted = True
								responseMessage = "Data Inserted Successfully"
							else:
								responseMessage = "Provide valid values to insert"	
						else:
							responseMessage = "Provide all valid values to insert"
			else: 
				responseMessage = "Provide valid data to insert"			
		except:
			logging.exception("Unable to insert the Data")
		return isDataInserted, responseMessage
			
	def getObject(self, query):
		logging.info("Finding data")
		isDataFiltered = False
		responseMessage = ''
		findData = {}
		try:
			db = self.client[self.db]
			coll = db[self.coll]
			if (query != {}):
				collectionkey = query.get("collection")
				for k, v in query.items():
					v.keys()
					for i in v.keys():
						findKeyData = collectionkey.get(i)
						if (len(findKeyData) != 0):
							for j in findKeyData.keys():
								findValues = findKeyData.get(j)
								if (findValues != ''):
									findData = coll.find_one(findKeyData)
									logging.debug("Data Returned")
									isDataFiltered = True
									responseMessage = "Data filtered successfully"
								else:
									responseMessage = "Provide valid values to filter"
						else:
							responseMessage = "Provide all valid values to filter"		
			else:
				responseMessage = "Provide valid data to filter"		
		except:
			logging.exception("Unable to get the data")					
		return findData, isDataFiltered, responseMessage	

	def updateObject(self, updationId, updation):
		logging.info("Updating data")
		isDataUpdated = False
		responseMessage = ''
		try:
			db = self.client[self.db]	
			coll = db[self.coll]
			collectionkey = updationId.get("collection")
			if (updationId != {}):
				if (updation != {}):
					for k, v in updationId.items():
						v.keys()
						for i in v.keys():
							updationIdData = collectionkey.get(i)
							if (len(updationIdData) != 0):
								for j in updation.keys():
									updationData = updation.get(j)
									if (len(updationData) != 0): 
										for k in updationIdData.keys():
											updationIdValues = updationIdData.get(k)
											if (updationIdValues != ''):
												for l in updationData.keys():
													updationValues = updationData.get(l)
													if (updationValues != ''):
														coll.update_one(updationIdData, updation)
														logging.debug("Data Updated")
														isDataUpdated = True 
														responseMessage = "Data Updated Successfully"
													else:
														responseMessage = "Provide valid updation values to update"	
											else:
												responseMessage = "Provide valid updationId values to update"
									else:
										responseMessage = "Provide all valid updation to update"				
							else: 
								responseMessage = "Provide all valid updationId to update"
				else:
					responseMessage = "Provide valid updation to update"			
			else:
				responseMessage = "Provide valid updationId to update"			
		except:
			logging.exception("Unable to update the Data")
		return isDataUpdated, responseMessage

	def deleteObject(self, deletion):
		logging.info("Deleting data")
		isDataDeleted = False
		responseMessage = ''
		try:
			db = self.client[self.db]	
			coll = db[self.coll]
			collectionkey = deletion.get("collection")
			if (deletion != {}):
				for k, v in deletion.items():
					v.keys()
					for i in v.keys():
						deleteData = collectionkey.get(i)
						if (len(deleteData) != 0):
							for j in deleteData.keys():
								deleteValues = deleteData.get(j)
								if (deleteValues != ''):
									coll.delete_one(deleteData)
									logging.debug("Data Deleted")
									isDataDeleted = True
									responseMessage = "Data Deleted Successfully"
								else:
									responseMessage = "Provide valid values to delete"
						else:
							responseMessage = "Provide all valid values to delete"	
			else:
				responseMessage = "Provide valid data to delete"					
		except:
			logging.exception("Unable to delete the Data")	
		return isDataDeleted, responseMessage

	def validateSaveObject(self, data):
		db = self.client[self.db]
		coll = db[self.coll]
		collectionkey = data.get("collection")
		resultList = []
		for k, v in data.items():
			v.keys()
			for i in v.keys():
				insertData = collectionkey.get(i)
				for j in insertData.keys():
					insertValues = insertData.get(j)
					if (insertValues != ''):
						self.result = True
					else:
						self.result = False
					resultList.append(self.result)
					if False not in resultList:
						self.funcResult = True
					else:
						self.funcResult = False		
+