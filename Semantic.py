import pprint
from VirtualMachine import VirtualMachine

programID = None
globalVariables = []
functionDictionary = []

functionsTemp = []
variablesTemp = []
typeTemp = []

vm = VirtualMachine()

# llamada para guardar las variables globales y borrar el acumulado de temporales
def addGlobalVariables():
	global globalVariables
	globalVariables = variablesTemp.copy()
	for variable in globalVariables:
		variable["mem_direction"] = vm.assignVirtualDirection('global', variable['variableType'])
	variablesTemp.clear()

# llamada para guardar variables locales en la tabla de variables de la ultima funcion agregada
# y borrar el acumulado de temporales
def addLocalVariables():
    global functionsTemp
    functionsTemp[-1]["functionVariables"] = variablesTemp.copy()
    variablesTemp.clear()

# cuando fromProgram es falso se agrega una funcion con 
# las variables acumuladas como locales al diccionario de funciones.
# cuando es verdadero, se envian las variables que quedan como acumuladas a el arreglo global
def addMethod(ID, Type, fromProgram):
	global programID, functionDictionary
	if(fromProgram):
		# global
		programID = ID
		functionDictionary = functionsTemp.copy()
	else:
		# funcion
		obj = {"functionID": ID, "functionType": Type, "functionVariables": []}
		functionsTemp.append(obj.copy())
	

# agrega tipo a las variables acumuladas en el arreglo temporal "typeTemp"
# y lo pone en arreglo de variables acumuladas "variablesTemp"
def addVariableTemp(variableType):
	global variablesTemp
	global typeTemp

	for i in typeTemp:
		variablesTemp.append({"variableID":i[0], "variableType":variableType, "variableDimentions": i[1]})

	typeTemp.clear()

# agrega id con dimensiones a arreglo acumulador temporal "typeTemp"
def addTypeTemp(variableID, dimensiones):
	global typeTemp
	typeTemp.append([variableID, dimensiones])

def createSemanticCube():
	global semanticCube
	semanticCube = {
		'+': {
			(int, int): int,
			(float, float): float,
			(str, str): str,

			(int, float): float,
			(int, str): 'error',

			(float, int): float,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',

			},
		'-': {
			(int, int): int,
			(float, float): float,
			(str, str): 'error',

			(int, float): float,
			(int, str): 'error',

			(float, int): float,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',

		},
		'*': {
			(int, int): int,
			(float, float): float,
			(str, str): 'error',

			(int, float): float,
			(int, str): 'error',

			(float, int): float,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'/': {
			(int, int): int,
			(float, float): float,
			(str, str): 'error',

			(int, float): float,
			(int, str): 'error',

			(float, int): float,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'%': {
			(int, int): int,
			(float, float): float,
			(str, str): 'error',

			(int, float): float,
			(int, str): 'error',

			(float, int): float,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'>': {
			(int, int): bool,
			(float, float): bool,
			(str, str): 'error',

			(int, float): bool,
			(int, str): 'error',

			(float, int): bool,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'<': {
			(int, int): bool,
			(float, float): bool,
			(str, str): 'error',

			(int, float): bool,
			(int, str): 'error',

			(float, int): bool,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'>=': {
			(int, int): bool,
			(float, float): bool,
			(str, str): 'error',

			(int, float): bool,
			(int, str): 'error',

			(float, int): bool,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'<=': {
			(int, int): bool,
			(float, float): bool,
			(str, str): 'error',

			(int, float): bool,
			(int, str): 'error',

			(float, int): bool,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'==': {
			(int, int): bool,
			(float, float): bool,
			(str, str): bool,

			(int, float): bool,
			(int, str): 'error',

			(float, int): bool,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',

		},
		'!=': {
			(int, int): bool,
			(float, float): bool,
			(str, str): bool,

			(int, float): bool,
			(int, str): 'error',

			(float, int): bool,
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',
		},
		'&&': {
			(int, int): 'error',
			(float, float): 'error',
			(str, str): 'error',
			(bool, bool): bool,

			(int, float): 'error',
			(int, str): 'error',
			(int, bool): 'error',

			(float, int): 'error',
			(float, str): 'error',
			(float, bool): 'error',

			(str, int): 'error',
			(str, float): 'error',
			(str, bool): 'error',
		},
		'||': {
			(int, int): 'error',
			(float, float): 'error',
			(str, str): 'error',
			(bool, bool): bool,

			(int, float): 'error',
			(int, str): 'error',
			(int, bool): 'error',

			(float, int): 'error',
			(float, str): 'error',
			(float, bool): 'error',

			(str, int): 'error',
			(str, float): 'error',
			(str, bool): 'error',
		},
	}

def deleteSemanticCube():
	global semanticCube
	del semanticCube

def printVars():
	print("______________________________________________")
	print("programID: ", programID)
	print("______________________________________________")
	print("globalVariables: ", len(globalVariables))
	print("globalVariables: ")
	pprint.pprint(globalVariables)
	print("______________________________________________")
	print("functionDictionary: ", len(functionDictionary))
	print("functionDictionary: ")
	pprint.pprint(functionDictionary)
	print("______________________________________________")

def printQuads():
	global quads
	print("______________________________________________")
	print("Quads:", quads)

pOperands = []
pTypes = []
pOper = []
quads = []
createSemanticCube()