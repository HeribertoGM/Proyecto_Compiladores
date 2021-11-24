import os.path
import sys
import pprint
from VirtualMemory import *

vm = []
quads = []
functionDictionary = []
globalVariables = []

# funcion que formatea los datos del archivo de codigo intermedio y los coloca en el entorno global
# obtiene: data del archivo de codigo intermedio
# retorna: variables globales inicializadas
def setup(data):
	global globalVariables, functionDictionary, quads, vm

	jsons = data.split("¿?¿?¿?")
	globalVariables = json.loads(jsons[0])
	functionDictionary = json.loads(jsons[1])
	quads = json.loads(jsons[2])

	vm.append(VirtualMemory())

# funcion que inicializa los espacios de memoria 
# de la memoria virtual a partir de las variables 
# globales inicializadas
# obtiene: variables globales inicializadas
# retorna: memoria virtual inicializada
def initializeVM():
	pass

# funcion que imprime en pantalla todas las estructuras globales
# obtiene: null
# retorna: null
def printAll():
	global globalVariables, functionDictionary, quads

	print("===========================================================")
	pprint.pprint(globalVariables)
	print("===========================================================")
	pprint.pprint(functionDictionary)
	print("===========================================================")
	pprint.pprint(quads)
	print("===========================================================")

# funcion que hace la administracion de variables, 
# obtiene valor, escribe y determina tratamiento de variables
# obtiene: dirreccion de variable / tuplas de punteros / tuplas de constantes
# retorna: valor dentro de la direccion de memoria / null
def adminVariable():
	pass

#funcion que se encarga de ejecutar una instruccion singular
# obtiene: quadruplo con instruccion
# retorna: null
def execute(instruction):
	pass

# funcion que funciona como instruction pointer, 
# hace saltos en el programa y maneja el flujo
# obtiene: variables globales inicializadas
# retorna: null
def run():
	global globalVariables, functionDictionary, quads
	ip = 0

	while quads[ip][0] != 'END':
		print(str(ip) + " - " + str(quads[ip]))
		if quads[ip][0] == '+':
			execute(quads[ip])
		elif quads[ip][0] == '-':
			execute(quads[ip])
		elif quads[ip][0] == '*':
			execute(quads[ip])
		elif quads[ip][0] == '/':
			execute(quads[ip])
		elif quads[ip][0] == '%':
			execute(quads[ip])
		elif quads[ip][0] == '||':
			execute(quads[ip])
		elif quads[ip][0] == '&&':
			execute(quads[ip])
		elif quads[ip][0] == '<':
			execute(quads[ip])
		elif quads[ip][0] == '>':
			execute(quads[ip])
		elif quads[ip][0] == '<=':
			execute(quads[ip])
		elif quads[ip][0] == '>=':
			execute(quads[ip])
		elif quads[ip][0] == '==':
			execute(quads[ip])
		elif quads[ip][0] == '!=':
			execute(quads[ip])
		elif quads[ip][0] == 'READ':
			execute(quads[ip])
		elif quads[ip][0] == 'WRITE':
			execute(quads[ip])
		elif quads[ip][0] == 'GOTO':
			ip = 14
			continue
		elif quads[ip][0] == 'GOTOF':
			pass
		elif quads[ip][0] == 'VERIFY':
			pass
		elif quads[ip][0] == 'ENDFUNC':
			pass
		elif quads[ip][0] == 'RETURN':
			pass
		elif quads[ip][0] == 'GOSUB':
			pass
		elif quads[ip][0] == 'PARAM':
			pass
		else:
			print("ERR - Instruction not identified - "+str(quads[ip]))
			sys.exit()

		ip += 1
	
	print(str(ip) + " - " + str(quads[ip]))
	print("Completado sin errores")

data = None
try:
	s = "testG.txt"#str(input(">> "))"fibonacci_r2.txt"#
	path = os.path.join("output", s)
	with open(path, "r") as f:
		data = f.read()
except EOFError:
    print("Error reading code.")


setup(data)
# printAll()
run()