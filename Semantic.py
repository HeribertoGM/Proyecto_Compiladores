import pprint
import sys
from intermediateCode import *

############################################
################# Semantic #################
############################################
# Archivo que contiene funciones auxiliares para 
# la creacion de las estructuras de datos 
# utilizados para fase de semantica

# variables globales
programID = None
globalVariables = []
functionDictionary = []

currScope = None

functionsTemp = []
variablesTemp = []
typeTemp = []

# funcion que  guarda las variables globales 
# y borrar el acumulado de temporales
# obtiene: null
# retorna: null
def addGlobalVariables():
	global globalVariables, variablesTemp, vm

	for var in variablesTemp:
		globalVariables.append(var)

	for variable in globalVariables:
		if variable["variableDimentions"] == None:
			variable["mem_direction"] = vm[-1].assignVirtualDirection('global', variable['variableType'])
		else:
			variable["mem_direction"] = vm[-1].assignMemoryArray('global', variable['variableType'], variable["arrSize"])

	variablesTemp.clear()

# funcion que llamada para guardar variables locales en 
# la tabla de variables de la ultima funcion agregada
# y borrar el acumulado de temporales
# obtiene: null
# retorna: null
def addLocalVariables():
	global functionsTemp, variablesTemp, vm
	# print(vm)
	functionsTemp[-1]["functionVariables"] = variablesTemp.copy()
	# Agregar assignVirtualDirection locales

	for variable in functionsTemp[-1]["functionVariables"]:
		if variable["variableDimentions"] == None:
			variable["mem_direction"] = vm[-1].assignVirtualDirection('local', variable['variableType'])
		else:
			variable["mem_direction"] = vm[-1].assignMemoryArray('local', variable['variableType'], variable["arrSize"])
	
	variablesTemp.clear()

# funcion que cuando fromProgram es falso se agrega una funcion con 
# las variables acumuladas como locales al diccionario de funciones.
# cuando es verdadero, se envian las variables que quedan como acumuladas a el arreglo global
# obtiene: id de funcion
# obtiene: tipo de retorno de la funcion
# obtiene: scope
# retorna: null
def addMethod(ID, Type, fromProgram):
	global programID, functionDictionary, quads
	if(fromProgram):
		# global
		programID = ID
		for func in functionsTemp:
			functionDictionary.append(func)
	else:
		# funcion
		obj = {"functionID": ID, "functionType": Type, "functionVariables": [], "parameterTable": [], "signature": [], "functionStart": len(quads)}
		functionsTemp.append(obj.copy())
	
def addVariableTempCheckRedef(vType):
	global variablesTemp, typeTemp
	
	elemIDsTT = list(map(lambda x: x[0], typeTemp))
	elemIDsVT = list(map(lambda x: x["variableID"], variablesTemp))
	
	elemID = elemIDsTT+elemIDsVT
	for i in elemID:
		if elemID.count(i) > 1:
			print("Semantic Error: redeclaration of variable - ", i)
			sys.exit()

	addVariableTemp(vType)

# funcion que agrega tipo a las variables 
# acumuladas en el arreglo temporal "typeTemp"
# y lo pone en arreglo de variables acumuladas "variablesTemp"
# obtiene: tipo de variable
# retorna: null
def addVariableTemp(variableType):
	global variablesTemp
	global typeTemp

	for i in typeTemp:
		dimLL = []
		r = 1
		if i[1] != None:
			li = 0
			for ls in i[1]:
				ls -= 1
				dimLL.append({"li": li, "ls": ls, "R": None})
				r = (ls - li + 1) * r

			m = [r, 0, 0, 0]
			dim = 1
			offset = 0
			for node in dimLL:
				m[dim] = m[dim - 1] / (node["ls"] - node["li"] + 1)
				node["R"] = m[dim]
				offset = offset + node["li"] * m[dim]
				dim += 1

			dimLL[-1]["R"] = -offset
			# pprint.pprint(dimLL)
		else:
			dimLL = None
			r = None

		variablesTemp.append({"variableID":i[0], "variableType":variableType, "variableDimentions": i[1], "variableDimLL" : dimLL, "arrSize": r})

	typeTemp.clear()

# funcion que agrega id con dimensiones a 
# arreglo acumulador temporal "typeTemp"
# obtiene: id de la variable
# obtiene: dimensiones/ null si no es dimensionada
# retorna: null
def addTypeTemp(variableID, dimensiones):
	global typeTemp
	typeTemp.append([variableID, dimensiones])

# funcion que procesa los parametros de las 
# funciones y las coloca en signature y parameterTable
# obtiene: id de la variable
# obtiene: tipo de la variable
# retorna: null
def addParameter(paramType, paramID):
	global functionsTemp
	functionsTemp[-1]["signature"].append(paramType)
	functionsTemp[-1]["parameterTable"].append(paramID)

# funcion que inicializa el cubo semantico
# obtiene: id de la variable
# obtiene: dimensiones/ null si no es dimensionada
# retorna: null
def createSemanticCube():
	global semanticCube
	semanticCube = {
		'+': {
			("int", "int"): 'int',
			("float", "float"): 'float',
			("str", "str"): 'str',
			("bool", "bool"): 'error',

			("int", "float"): 'float',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'float',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'-': {
			("int", "int"): 'int',
			("float", "float"): 'float',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'float',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'float',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'*': {
			("int", "int"): 'int',
			("float", "float"): 'float',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'float',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'float',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'/': {
			("int", "int"): 'int',
			("float", "float"): 'float',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'float',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'float',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'%': {
			("int", "int"): 'int',
			("float", "float"): 'float',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'float',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'float',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'>': {
			("int", "int"): 'bool',
			("float", "float"): 'bool',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'bool',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'bool',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'<': {
			("int", "int"): 'bool',
			("float", "float"): 'bool',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'bool',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'bool',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'>=': {
			("int", "int"): 'bool',
			("float", "float"): 'bool',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'bool',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'bool',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'<=': {
			("int", "int"): 'bool',
			("float", "float"): 'bool',
			("str", "str"): 'error',
			("bool", "bool"): 'error',

			("int", "float"): 'bool',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'bool',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'==': {
			("int", "int"): 'bool',
			("float", "float"): 'bool',
			("str", "str"): 'bool',
			("bool", "bool"): 'bool',

			("int", "float"): 'bool',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'bool',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'!=': {
			("int", "int"): 'bool',
			("float", "float"): 'bool',
			("str", "str"): 'bool',
			("bool", "bool"): 'bool',

			("int", "float"): 'bool',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'bool',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'&&': {
			("int", "int"): 'error',
			("float", "float"): 'error',
			("str", "str"): 'error',
			("bool", "bool"): 'bool',

			("int", "float"): 'error',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'error',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		},
		'||': {
			("int", "int"): 'error',
			("float", "float"): 'error',
			("str", "str"): 'error',
			("bool", "bool"): 'bool',

			("int", "float"): 'error',
			("int", "str"): 'error',
			("int", "bool"): 'error',

			("float", "int"): 'error',
			("float", "str"): 'error',
			("float", "bool"): 'error',

			("str", "int"): 'error',
			("str", "float"): 'error',
			("str", "bool"): 'error'
		}
	}

# funcion que borra el cubo semantico
# obtiene: null
# retorna: null
def deleteSemanticCube():
	global semanticCube
	del semanticCube

# funcion que imprime la tabla de variables globales, 
# la memoria virtual, el diccionario de funciones y el programID
# obtiene: null
# retorna: null
def printVars():
	global programID, globalVariables, functionDictionary, vm
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
	# print(vm[-1].localInts.loc[9001:9010])

# funcion que busca un id en la tabla de variables de 
# la funcion actual y en la tabla de variables global
# obtiene: id de la variable
# obtiene: scope
# retorna: objeto variable
def getVariable(varID, scope):
	global globalVariables, functionsTemp

	if scope: # local
		f = functionsTemp[-1]['functionVariables']
		y = list(filter(lambda x: (x['variableID'] == varID), f))
		if y == []:
			y = list(filter(lambda x: (x['variableID'] == varID), globalVariables))
		return y[0]
	else: #global
		y = list(filter(lambda x: (x['variableID'] == varID), globalVariables))
		return y[0]

# funcion que retorna una entrada del 
# directorio de funciones de acuerdo 
# a un id de funcion
# obtiene: id de la funcion
# retorna: entrada del directorio de funciones
def getFunction(funcID):
	global functionsTemp
	func = list(filter(lambda x: (x['functionID'] == funcID), functionsTemp))
	return func

createSemanticCube()