import pprint.pprint

programID = None
globalVariables = []
functionDictionary = []

functionsTemp = []
variablesTemp = []
typeTemp = []

# cuando fromProgram es falso se agrega una funcion con 
# las variables acumuladas como locales al diccionario de funciones.
# cuando es verdadero, se envian las variables que quedan como acumuladas a el arreglo global
def addMethod(ID, Type, fromProgram):
	global programID, functionDictionary, globalVariables
	if(fromProgram):
		# global
		programID = ID
		functionDictionary = functionsTemp.copy()
		globalVariables = variablesTemp.copy()
	else:
		# funcion
		obj = {"functionID":ID, "functionType":Type, "functionVariables":variablesTemp.copy()}
		functionsTemp.append(obj.copy())
	
	#variablesTemp.clear()

# agrega tipo a las variables acumuladas en el arreglo temporal "typeTemp"
# y lo pone en arreglo de variables acumuladas "variablesTemp"
def addVariableTemp(variableType):
	global typeTemp

	for i in typeTemp:
		variablesTemp.append({"variableID":i[0], "variableType":variableType, "variableDimentions": i[1]})

	typeTemp.clear()

# agrega id con dimensiones a arreglo acumulador temporal "typeTemp"
def addTypeTemp(variableID, dimensiones):
	global typeTemp
	typeTemp.append([variableID, dimensiones])

def printVars():
	print("##############################################")
	print("programID: ", programID)
	print("##############################################")
	print("globalVariables: ", len(globalVariables))
	print("globalVariables: ")
	pprint(globalVariables)
	print("##############################################")
	print("functionDictionary: ", len(functionDictionary))
	print("functionDictionary: ")
	pprint(functionDictionary)
	print("##############################################")