import os
import os.path
import sys
import pprint
import json

from numpy import right_shift
from Parser import parseProgram
from VirtualMemory import *

##################################################
################# VirtualMachine #################
##################################################
# Archivo que contiene la logica de la maquina virtual, 
# utiliza el archivo de salida del compilador para la ejecucion de codigo

vm = []
quads = []
functionDictionary = []
globalVariables = []
params = []

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

# funcion que hace el movimiento de variables 
# de un contexto de memoria virtual pasiva a activa
# obtiene: direccion que guarda el valor a pasar a la funcion
# obtine: direccion local que tiene el parametro dentro de la funcion
# retorna: direccion inicializada con el valor de la dirPasiva
def passParam(dirPasiva, dirActiva):
	val = None
	if type(dirPasiva) == int:
		val = vm[-2].getValueWithIndex(dirPasiva)
	else:
		if dirPasiva[0] == 'pointer':
			if type(dirPasiva[0][1]) == int:
				vm[-2].getValueWithIndex(vm[-2].getValueWithIndex(dirPasiva[1]))
			else: # cte
				vm[-2].setValueWithIndex(dirPasiva[1][1], dirPasiva[1][2])
			val = vm[-2].getValueWithIndex(dirPasiva[1][1])
		else: # cte
			vm[-2].setValueWithIndex(dirPasiva[1], dirPasiva[2])
			val = vm[-2].getValueWithIndex(dirPasiva[1])

	# print("param: ", val)
	adminVariable(False, dirActiva, val)

# funcion que hace el movimiento de variables 
# de un contexto de memoria virtual activa a pasiva
# obtine: direccion local que tiene el parametro dentro de la funcion
# obtiene: direccion que guarda el valor a pasar a la funcion
# retorna: direccion actualizada con el valor de la dirActiva
def passReturn(dirActiva, dirPasiva):
	val = adminVariable(True, dirActiva, None)
	vm[-2].setValueWithIndex(dirPasiva, val)

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
def adminVariable(getSet, var, val):
	# print(type(var))
	if type(var) == int:
		if getSet:
			return vm[-1].getValueWithIndex(var)
		else:
			vm[-1].setValueWithIndex(var, val)
	elif type(var) == list and var[0] == "pointer":
		if type(var[1]) == int:
			if getSet:
				return vm[-1].getValueWithIndex(vm[-1].getValueWithIndex(var[1]))
			else:
				vm[-1].setValueWithIndex(vm[-1].getValueWithIndex(var[1]), val)
		else:
			return adminVariable(True, var[1], None)
	elif type(var) == list and var[0] == "cte":
		vm[-1].setValueWithIndex(var[1], var[2])
		if getSet:
			return vm[-1].getValueWithIndex(var[1])
		else:
			print("Unable Operation - write cte")
	else: #str
		print("adminVariable - str")

#funcion que se encarga de ejecutar una instruccion singular
# obtiene: quadruplo con instruccion
# retorna: null
def execute(instruction):
	global globalVariables, functionDictionary, quads, vm
	if instruction[0] == '+':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand + rOperand)
	elif instruction[0] == '-':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand - rOperand)
	elif instruction[0] == '*':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand * rOperand)
	elif instruction[0] == '/':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand / rOperand)
	elif instruction[0] == '%':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand % rOperand)
	elif instruction[0] == '||':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand or rOperand)
	elif instruction[0] == '&&':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand and rOperand)
	elif instruction[0] == '<':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand < rOperand)
	elif instruction[0] == '>':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand > rOperand)
	elif instruction[0] == '<=':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand <= rOperand)
	elif instruction[0] == '>=':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand >= rOperand)
	elif instruction[0] == '==':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand == rOperand)
	elif instruction[0] == '!=':
		lOperand = adminVariable(True, instruction[1], None)
		rOperand = adminVariable(True, instruction[2], None)
		adminVariable(False, instruction[3], lOperand != rOperand)
	elif instruction[0] == 'READ':
		s = str(input(">>"))
		if not s.isalpha():
			try:
				s = int(s)
			except ValueError:
				s = float(s)
		adminVariable(False, instruction[3], s)
	elif instruction[0] == 'WRITE':
		result = adminVariable(True, instruction[3], None)
		print(result)
	elif instruction[0] == '=':
		lOperand = adminVariable(True, instruction[1], None)
		adminVariable(False, instruction[3], lOperand)
	else:
		print("ERR - Instruction not identified - "+str(instruction))
		sys.exit()


# funcion que funciona como instruction pointer, 
# hace saltos en el programa y maneja el flujo
# obtiene: variables globales inicializadas
# retorna: null
def run():
	global globalVariables, functionDictionary, quads, vm
	ip = 0
	returnFromFunc = []

	while quads[ip][0] != 'END':
		# print(str(ip) + " - " + str(quads[ip]))
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
		elif quads[ip][0] == '=':
			execute(quads[ip])
		elif quads[ip][0] == 'GOTO':
			ip = quads[ip][3]
			continue
		elif quads[ip][0] == 'GOTOF':
			lOperand = adminVariable(True, quads[ip][1], None)
			if not lOperand:
				ip = quads[ip][3]
				continue
		elif quads[ip][0] == 'VERIFY':
			val = adminVariable(True, quads[ip][1], None)
			limI = adminVariable(True, quads[ip][2], None)
			limS = adminVariable(True, quads[ip][3], None)
			if not (val >= limI and val <= limS):
				print(f'ERR - Val not in range {limI}-{limS} - '+str(quads[ip]))
				sys.exit()
		elif quads[ip][0] == 'ENDFUNC':
			ip = returnFromFunc.pop()
			vm.pop()
			continue
		elif quads[ip][0] == 'RETURN':
			passReturn(quads[ip][1], quads[ip][3])
			pass
		elif quads[ip][0] == 'GOSUB':
			returnFromFunc.append(ip + 1)
			ip = quads[ip][3]
			continue
		elif quads[ip][0] == 'PARAM':
			params.append((quads[ip][1], quads[ip][3]))
			# passParam(quads[ip][1], quads[ip][3])
		elif quads[ip][0] == 'ERA':
			vm.append(VirtualMemory())
			for i in range(0, len(params)):
				dPasiva, dActiva = params.pop()
				passParam(dPasiva, dActiva)
		else:
			print("ERR - Instruction not identified - "+str(quads[ip]))
			sys.exit()


		ip += 1
	print("Completado sin errores")

# ==================== Main ====================

data = None
try:
	s = str(input(">> "))#"fibonacci_r2.txt""fibonacci_r2.txt"#
	# path = os.path.join("tests", s)
	# with open(path, "r") as f:
	# 	program = f.read()
	parseProgram(s)

	path = os.path.join("output", s)
	with open(path, "r") as f:
		data = f.read()
except EOFError:
    print("Error reading code.")

setup(data)
# printAll()
run()