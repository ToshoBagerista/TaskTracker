from datetime import datetime

class Task:
	def __init__(self, description, status):
		self.description = description
		self.status = status
		self.createdAt = datetime.now()
		self.updatedAt = datetime.now()

	def update(self, description):
		self.updatedAt = datetime.now()
		self.description = description

	def updateStatus(self, status):
		self.status = status