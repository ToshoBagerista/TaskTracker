import os, json

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
	global data, ID, tasks
	try:
		loadtasks = json.load(data)
		for task in loadtasks.values():
			tasks[ID] = Task(ID, task['description'], status=task['status'], createdAt=task['createdAt'], updatedAt=task['updatedAt'])
			ID += 1
	except ValueError:
		pass
	data.close()
	os.remove("data.json")

def Delete(id):
	try: del tasks[id]
	except KeyError: print("Task not found!")

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
	try:
		inp = input("Enter your command: ")
		if inp.__contains__("\""): com = list(inp[:inp.index("\"")].split(" "))
		else: com = list(inp.split(" "))
		if com[0] == "task-cli":
			match(com[1]):
				case "add":
					Add(inp[inp.index("\"")+1:len(inp)-1])
					return
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
					return
				case "exit":
					isActive = False
					return
	except ValueError: print("Invalid input! Try again!")
	except IndexError: print("Something went wrong! Try again!")
	except KeyError: print("Something went wrong! Try again!")
	finally: return

def main():
	global data
	try:
		if os.path.isfile("data.json"):
			data = open("data.json", "r")
			Load()
		data = open("data.json", "w")
	except BaseException:
		if os.path.isfile("data.json"):
			data.close()
			os.remove("data.json")
			data = open("data.json", "w")
		else: data.open("data.json", "w")
	while isActive:
		menu()
	try: json.dump({int(k): v.__str__() for (k, v) in tasks.items()}, data, indent=2)
	except BaseException: print("You did something wrong! You are an idiot!")

if __name__ == "__main__":
	main()