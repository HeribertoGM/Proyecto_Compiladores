import pprint

programID = None
globalVariables = []
functionDictionary = []

functionsTemp = []
variablesTemp = []
typeTemp = []

# llamada para guardar las variables globales y borrar el acumulado de temporales
def addGlobalVariables():
	global globalVariables
	globalVariables = variablesTemp.copy()
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
		obj = {"functionID":ID, "functionType":Type, "functionVariables":[]}
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

def printVars():
	print("##############################################")
	print("programID: ", programID)
	print("##############################################")
	print("globalVariables: ", len(globalVariables))
	print("globalVariables: ")
	pprint.pprint(globalVariables)
	print("##############################################")
	print("functionDictionary: ", len(functionDictionary))
	print("functionDictionary: ")
	pprint.pprint(functionDictionary)
	print("##############################################")

def semanticCompat(varA, varB, operator):
	varA = type(varA)
	varB = type(varB)

	return {
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
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

            }[varA, varB],
		'&&': {
            (int, int): 'error',
			(float, float): 'error',
			(str, str): 'error',
			
            (int, float): 'error',
			(int, str): 'error',

			(float, int): 'error',
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',

			#bool?

            }[varA, varB],
		'||': {
            (int, int): 'error',
			(float, float): 'error',
			(str, str): 'error',
			
            (int, float): 'error',
			(int, str): 'error',

			(float, int): 'error',
			(float, str): 'error',

			(str, int): 'error',
			(str, float): 'error',

			#bool?

            }[varA, varB],
    }[operator]