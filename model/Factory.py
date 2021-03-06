from DateHelper import DateHelper
from StringHelper import StringHelper

class Factory:
	def __init__(self):
		pass

	def getDateHelper(self):
		return self._getService(DateHelper(), [])

	def getExampleService(self):
		return self._getService(ExampleService(), [])
		
	def getStringHelper(self):
		return self._getService(StringHelper(), [])
		

	def _getService(self, service, stuff):
		for item in stuff:
			service.inject(item[0], item[1])

		return service

	def _getDAO(self, dao):
		dao.inject("dateHelper", self.getDateHelper())
		return dao
