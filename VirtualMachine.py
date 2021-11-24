import os.path
import pprint
from VirtualMemory import *

vm = []
quads = []
functionDictionary = []
globalVariables = []

def setup(data):
	global globalVariables, functionDictionary, quads, vm

	jsons = data.split("¿?¿?¿?")
	globalVariables = json.loads(jsons[0])
	functionDictionary = json.loads(jsons[1])
	quads = json.loads(jsons[2])

	jsonVM = json.loads(jsons[3])
	vm.append(VirtualMemory())
	vm[-1].restoreVM(jsonVM)

def run():
	pass

def printAll():
	global globalVariables, functionDictionary, quads, vm

	pprint.pprint(globalVariables)
	pprint.pprint(functionDictionary)
	pprint.pprint(quads)
	print(vm[-1].cteInts)

data = None
try:
	s = str(input(">> "))#"testS.txt""fibonacci_r2.txt"#
	path = os.path.join("output", s)
	with open(path, "r") as f:
		data = f.read()
except EOFError:
    print("Error reading code.")


setup(data)
printAll()
run()