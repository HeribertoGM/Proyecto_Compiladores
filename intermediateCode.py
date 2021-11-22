from VirtualMemory import *

vm = []

pOperands = []
pTypes = []
pOper = []
quads = [["GOTO", "", "", None]]
pJumps = []
pDim = []

currFunc = None
paramCounter = 0

#QuadsID
pOperandsID = []
quadsID = [["GOTO", "", "", None]]
nTemps = 1

def printQuads():
	global quads
	print("______________________________________________")
	print("Quads:")
	for i in range(len(quads)):
		print(i, quads[i])
	
	#QuadsID
	global quadsID
	print("______________________________________________")
	print("QuadsID:")
	for i in range(len(quadsID)):
		print(i, quadsID[i])

def createEra():
	global vm
	vm.append(VirtualMemory())

def destroyEra():
	global vm
	last = vm.pop()
	del last

createEra()