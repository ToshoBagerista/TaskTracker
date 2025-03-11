from datetime import datetime
import json

class Task:
	def __init__(self, id, description):
		self.id = id
		self.description = description
		self.status = "todo"
		self.createdAt = datetime.now()
		self.updatedAt = datetime.now()

	def update(self, description):
		self.updatedAt = datetime.now()
		self.description = description

	def updateStatus(self, status):
		self.status = status

	def to_json(self):
		return self

	def __dict__(self):
		return {"id": self.id, 'description': self.description, 'status': self.status, 'createdAt': self.createdAt, 'updatedAt': self.updatedAt}

	def __str__(self): return {"id": self.id, 'description': self.description, 'status': self.status, 'createdAt': str(f"{self.createdAt :%d/%m/%y %H:%M:%S}"), 'updatedAt': str(f"{self.updatedAt :%d/%m/%y %H:%M:%S}")}
