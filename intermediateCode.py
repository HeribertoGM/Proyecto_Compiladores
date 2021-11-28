from VirtualMemory import *

####################################################
################# IntermediateCode #################
####################################################
# Archivo que contiene todas las variables globales y 
# funciones auxiliares utilizadas para la generacion 
# de codigo intermedio

# variables globales
vm = []

pOperands = []
pTypes = []
pOper = []
quads = [["GOTO", "", "", None]]
pJumps = []
pDim = []

currFunc = None
lastFunc = []
paramCounter = 0

#QuadsID
pOperandsID = []
quadsID = [["GOTO", "", "", None]]
nTemps = 1

# funcion que imprime todos los cuadruplos guardados en la variable quads
# obtiene: null
# retorna: null
def printQuads():
	global quads
	print("______________________________________________")
	print("Quads:")
	for i in range(len(quads)):
		print(i, quads[i])
	
	# QuadsID
	global quadsID
	print("______________________________________________")
	print("QuadsID:")
	for i in range(len(quadsID)):
		print(i, quadsID[i])

# funcion que crea una nueva instancia de la 
# memoria virtual y la agrega al stack de memorias
# obtiene: null
# retorna: null
def createEra():
	global vm
	vm.append(VirtualMemory())

# funcion que elimina la ultima instancia 
# de memoria virtual del stack de memorias
# obtiene: null
# retorna: null
def destroyEra():
	global vm
	last = vm.pop()
	del last

# llamada a createEra para la creacion de memoria virtual general
createEra()