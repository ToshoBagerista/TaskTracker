from datetime import datetime

class Task:
	def __init__(self, id, description, **kwargs):
		self.id = id
		self.description = description
		if kwargs.get("status") is not None: self.status = kwargs.get("status")
		else: self.status = "todo"
		if kwargs.get("createdAt") is not None: self.createdAt = datetime.strptime(kwargs["createdAt"], "%d/%m/%y %H:%M:%S")
		else: self.createdAt = datetime.now()
		if kwargs.get("updatedAt") is not None: self.updatedAt = datetime.strptime(kwargs["updatedAt"], "%d/%m/%y %H:%M:%S")
		else: self.updatedAt = datetime.now()

	def update(self, description):
		self.updatedAt = datetime.now()
		self.description = description

	def updateStatus(self, status):
		self.updatedAt = datetime.now()
		self.status = status

	def __str__(self): return {"id": self.id, 'description': self.description, 'status': self.status, 'createdAt': str(f"{self.createdAt :%d/%m/%y %H:%M:%S}"), 'updatedAt': str(f"{self.updatedAt :%d/%m/%y %H:%M:%S}")}
