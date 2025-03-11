import os.path, json
from Task import Task

global data
isActive = True
ID = 1
tasks = {}

def Add(desc):
	global ID
	tasks[ID] = Task(ID, desc)
	ID += 1

def Load():
	global tasks
	tasks = json.load(data)
	print(tasks)

def Delete(id):
	del tasks[id]

def Update(id, description):
	tasks[id].update(description)

def listtasks(tag):
	if tag == "all":
		for task in tasks.values(): print(f"{task.description} - {task.status}")
		return
	for task in tasks.values():
		if task.status == tag: print(f"{task.description} - {task.status}")
		return

def mark(id, status):
	tasks[id].status = status

def menu():
	global isActive
	inp = input("Enter your command: ")
	if inp.__contains__("\""): com = list(inp[:inp.index("\"")].split(" "))
	else: com = list(inp.split(" "))
	if com[0] == "task-cli":
		match(com[1]):
			case "add":
				Add(inp[inp.index("\"")+1:len(inp)-1])
				# print(tasks[1].description)
			case "delete":
				Delete(int(com[2]))
				return
			case "update":
				Update(int(com[2]), inp[inp.index("\"")+1:len(inp)-1])
				return
			case "list":
				if len(com) == 2: listtasks("all")
				else:
					match(com[2]):
						case "done":
							listtasks("done")
							return
						case "todo":
							listtasks("todo")
							return
						case "in-progress":
							listtasks("in-progress")
							return
				return
			case "mark-in-progress":
				mark(int(com[2]), "in-progress")
				return
			case "mark-done":
				mark(int(com[2]), "done")
			case "exit":
				isActive = False

def main():
	global data
	if os.path.isfile("data.json"):
		# data = open("data.json", "r")
		# Load()
		data = open("data.json", "a")
	else: data = open("data.json", "w")
	while isActive:
		menu()
	json.dump({k: v.__str__() for (k, v) in tasks.items()}, data, indent=2)

if __name__ == "__main__":
	main()