import ntpath
import sys
import ply.yacc as yacc
from Lexer import *
from Semantic import *

# Programa
def p_programa(p):
	'''
	programa : PROGRAM ID SEMICOLON declaracion_global funcion main bloque
	'''
	quads.append(("END", "", "", ""))

	#QuadsID
	quadsID.append(("END", "", "", ""))

	addMethod(p[2], None, True)
	deleteSemanticCube()
	printVars()
	printQuads()
	print("call programa")

def p_main(p):
	'''
	main : MAIN O_PARENTHESIS C_PARENTHESIS
	'''
	global currScope
	currScope = False #global
	quads[0][3] = len(quads)

	#QuadsID
	quadsID[0][3] = len(quadsID)
	print("call main")

# Bloque
def p_bloque(p):
	'''
	bloque : O_CBRACKET bloque_prime C_CBRACKET
	'''
	print("call bloque")

def p_bloque_prime(p):
	'''
	bloque_prime : estatuto bloque_prime
				 | epsilon
	'''
	print("call bloque_prime")

# Declaracion
def p_declaracion_funcion(p):
	'''
	declaracion_funcion : declaracion
	'''
	addLocalVariables()
	global currScope
	currScope = True # local
	print("call declaracion_funcion")

def p_declaracion_global(p):
	'''
	declaracion_global : declaracion
	'''
	global globalVariables
	addGlobalVariables()
	print("call declaracion_global")

def p_declaracion(p):
	'''
	declaracion : declaracion_base
				| declaracion_base declaracion
	'''
	print("call declaracion")

def p_declaracion_base(p):
	'''
	declaracion_base : LET declaracion_prime COLON declaracion_tipo SEMICOLON
	'''
	print("call declaracion_base")

def p_declaracion_prime(p):
	'''
	declaracion_prime : declaracion_variable
					  | declaracion_variable COMMA declaracion_prime
	'''
	print("call declaracion_prime")


def p_declaracion_variable(p):
	'''
	declaracion_variable : ID O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET
						 | ID O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET
						 | ID O_ABRACKET CTE_INT C_ABRACKET
						 | ID 
	'''

	if(len(p) > 2):
		dim_len = int((len(p)-2)/3)
		dims = []

		for i in range(1,dim_len+1):
			cte_index = i*3
			dims.append(p[cte_index])

		print(dims)
		addTypeTemp(p[1], dims)
	else:
		addTypeTemp(p[1], None)

	print("call declaracion_variable")

def p_declaracion_tipo(p):
	'''
	declaracion_tipo : INT
					 | FLOAT
					 | CHAR
					 | STRING
	'''
	# addVariableTemp(p[1])
	if p[1] == 'int':
		addVariableTemp(int)
	elif p[1] == 'float':
		addVariableTemp(float)
	else:
		addVariableTemp(str)
	print("call declaracion_tipo")

# Tipo
def p_tipo(p):
	'''
	tipo : INT
		 | FLOAT
		 | CHAR
		 | STRING
	'''
	print("call tipo")

# Funcion
def p_funcion(p):
	'''
	funcion : funcion_base funcion
			| epsilon
	'''
	print("call funcion")

def p_funcion_base(p):
	'''
	funcion_base : FUNCTION funcion_ident O_PARENTHESIS funcion_prime C_PARENTHESIS declaracion_funcion bloque
	'''
	print("call funcion_base")

def p_funcion_prime(p):
	'''
	funcion_prime : tipo ID
				  | tipo ID COMMA funcion_prime
	'''
	print("call funcion_prime")

def p_funcion_ident(p):
	'''
	funcion_ident : VOID ID
 				  | INT ID
				  | FLOAT ID
				  | CHAR ID
				  | STRING ID
	'''
	addMethod(p[2], p[1], False)
	print("call funcion_ident")

# Variable
def p_variable(p):
	'''
	variable : var_array
			 | ID 
	'''
	global currScope
	if p[1] != None:
		try:
			variable = getVariable(p[1], currScope)
		except Exception as e:
			print("Semantic Error[1]: undefined variable - ", p[1])
			sys.exit()

		pOperands.append(variable['mem_direction'])

		#QuadsID
		pOperandsID.append(p[1])

		pTypes.append(variable['variableType'])
	print("call variable")

def p_var_array(p):
	'''
	var_array : arr_id O_ABRACKET exp arr_close_bracket arr_open_bracket exp arr_close_bracket arr_open_bracket exp arr_close_bracket
			  | arr_id O_ABRACKET exp arr_close_bracket arr_open_bracket exp arr_close_bracket
			  | arr_id O_ABRACKET exp arr_close_bracket
	'''
	aux1 = pOperands.pop()
	k = vm[-1].cteAssign(0)
	result = vm[-1].temporalAssign(int)
	quads.append(("+", aux1, k, result))
	temp = vm[-1].temporalAssign(int)
	variable, dim = pDim.pop()
	base_dir = vm[-1].cteAssign(variable["mem_direction"])
	quads.append(("+", result, [base_dir], temp))
	pOperands.append([temp])
	pOper.pop()

	#QuadsID
	global nTemps
	aux1ID = pOperandsID.pop()
	quadsID.append(("+", aux1ID, 0, "t" + str(nTemps)))
	quadsID.append(("+", "t" + str(nTemps), [variable["mem_direction"]], "t" + str(nTemps + 1)))
	pOperandsID.append(["t" + str(nTemps + 1)])
	nTemps += 2
	print("call var_array")

def p_arr_id(p):
	'''
	arr_id : ID
	'''
	global currScope
	try:
		variable = getVariable(p[1], currScope)

		# pOperands.append(variable["mem_direction"])
		# pTypes.append(variable["variableType"])

		dim = 0
		pDim.append((variable, dim))
		pOper.append("FakeBottom")
	except Exception as e:
		print("Semantic Error[2]: undefined variable - ", p[1])
		sys.exit()
	print("call arr_id")

def p_arr_close_bracket(p):
	'''
	arr_close_bracket : C_ABRACKET
	'''
	operand = pOperands[-1]
	index = vm[-1].cteAssign(0)
	variable, dim = pDim[-1]
	ls = vm[-1].cteAssign(variable["variableDimLL"][dim]["ls"])
	quads.append(("verify", operand, index, ls))

	#QuadsID
	operandID = pOperandsID[-1]
	quadsID.append(("verify", operandID, 0, variable["variableDimLL"][dim]["ls"]))

	print("Dimension:", dim)
	if len(variable["variableDimLL"]) > dim + 1:
		aux = pOperands.pop()
		result = vm[-1].temporalAssign(int)
		r = vm[-1].cteAssign(variable["variableDimLL"][dim]["R"])
		quads.append(('*', aux, r, result))
		pOperands.append(result)

		#QuadsID
		global nTemps
		operandID = pOperandsID.pop()
		quadsID.append(('*', operandID, variable["variableDimLL"][dim]["R"], "t" + str(nTemps)))
		pOperandsID.append("t" + str(nTemps))
		nTemps += 1
	
	# if not (len(variable["variableDimLL"]) > dim + 1):
	# 	pDim.append((variable, dim))
	if dim >= 1:
		aux2 = pOperands.pop()
		aux1 = pOperands.pop()
		result = vm[-1].temporalAssign(int)
		quads.append(('+', aux1, aux2, result))
		pOperands.append(result)

		#QuadsID
		aux2ID = pOperandsID.pop()
		aux1ID = pOperandsID.pop()
		quadsID.append(('+', aux1ID, aux2ID, "t" + str(nTemps)))
		pOperandsID.append("t" + str(nTemps))
		nTemps += 1
		print("=========Más de una==========")
	print("call arr_close_bracket")

def p_arr_open_bracket(p):
	'''
	arr_open_bracket : O_ABRACKET
	'''
	variable, dim = pDim.pop()
	dim += 1
	pDim.append((variable, dim))
	print("call arr_open_bracket")

# Estatuto
def p_estatuto(p):
	'''
	estatuto : asignacion SEMICOLON
			 | llamada SEMICOLON
			 | retorno SEMICOLON
			 | lectura SEMICOLON
			 | escritura SEMICOLON
			 | decision
			 | while
			 | for
	'''
	print("call estatuto")

# Asignacion
def p_asignacion(p):
	'''
	asignacion : variable ASSIGN asignacion_expr
	'''
	print("call asignacion")

def p_asignacion_expr(p):
	'''
	asignacion_expr : expr
	'''
	global currScope
	
	lOperand = pOperands.pop()
	result = pOperands.pop()

	quads.append(("=", lOperand, " ", result))

	#QuadsID
	lOperandID = pOperandsID.pop()
	resultID = pOperandsID.pop()

	quadsID.append(("=", lOperandID, " ", resultID))
	print("call asignacion_expr")

# Llamada
def p_llamada(p):
	'''
	llamada : ID O_PARENTHESIS llamada_prime C_PARENTHESIS
	'''
	print("call llamada")

def p_llamada_prime(p):
	'''
	llamada_prime : exp
				  | exp COMMA llamada_prime
	'''
	# Agregar nueva ERA
	print("call llamada_prime")

# Retorno
def p_retorno(p):
	'''
	retorno : RETURN O_PARENTHESIS expr C_PARENTHESIS
	'''
	print("call retorno")

# Lectura
def p_lectura(p):
	'''
	lectura : READ O_PARENTHESIS lectura_prime C_PARENTHESIS
	'''
	print("call lectura")

def p_lectura_prime(p):
	'''
	lectura_prime : variable
				  | variable COMMA lectura_prime
	'''
	pTypes.pop()
	quads.append(("read", "", "", pOperands.pop()))

	#QuadsID
	quadsID.append(("read", "", "", pOperandsID.pop()))
	print("call lectura_prime")

# Escritura
def p_escritura(p):
	'''
	escritura : WRITE O_PARENTHESIS escritura_prime C_PARENTHESIS
	'''
	print("call escritura")

def p_escritura_prime(p):
	'''
	escritura_prime : expr
					| escritura_string
					| expr COMMA escritura_prime
					| escritura_string COMMA escritura_prime
	'''
	pTypes.pop()
	quads.append(("write", "", "", pOperands.pop()))

	#QuadsID
	quadsID.append(("write", "", "", pOperandsID.pop()))
	print("call escritura_prime")

def p_escritura_string(p):
	'''
	escritura_string : CTE_STRING
	'''
	index = vm[-1].cteAssign(p[1])
	pOperands.append(index)
	pTypes.append("TypeDummie")

	#QuadsID
	pOperandsID.append(p[1])
	print("call escritura_string")

# Decision
def p_decision(p):
	'''
	decision : IF O_PARENTHESIS decision_expr C_PARENTHESIS bloque else
	'''
	print("call decision")

def p_decision_expr(p):
	'''
	decision_expr : expr
	'''
	result = pOperands.pop()
	varType = pTypes.pop()
	if varType == bool:
		quads.append(["GOTOF", result, "", None])
		pJumps.append(len(quads) - 1)

		#QuadsID
		quadsID.append(["GOTOF", pOperandsID.pop(), "", None])
	else:
		print(f'Semantic error: type mismatch - ({result}:{varType}) not boolean)' )
		sys.exit()

	print("call decision_expr")

def p_else(p):
	'''
	else : else_prime bloque
		 | epsilon
	'''
	quads[pJumps.pop()][3] = len(quads)
	print("call else")

def p_else_prime(p):
	'''
	else_prime : ELSE
	'''
	quads.append(["GOTO", "", "", None])
	jump = pJumps.pop()
	pJumps.append(len(quads) - 1)
	quads[jump][3] = len(quads)

	#QuadsID
	quadsID.append(["GOTO", "", "", None])
	quadsID[jump][3] = len(quadsID)
	print("call else_prime")

# While
def p_while(p):
	'''
	while : while_prime while_expr bloque
	'''
	end = pJumps.pop()
	ret = pJumps.pop()
	quads.append(["GOTO", "", "", ret])
	quads[end][3] = len(quads)

	#QuadsID
	quadsID.append(["GOTO", "", "", ret])
	quadsID[end][3] = len(quadsID)
	print("call while")

def p_while_prime(p):
	'''
	while_prime : WHILE
	'''
	pJumps.append(len(quads))
	print("call while_prime")

def p_while_expr(p):
	'''
	while_expr : O_PARENTHESIS expr C_PARENTHESIS
	'''
	result = pOperands.pop()
	varType = pTypes.pop()
	if varType == bool:
		quads.append(["GOTOF", result, "", None])
		pJumps.append(len(quads) - 1)

		#QuadsID
		quadsID.append(["GOTOF", pOperandsID.pop(), "", None])
	else:
		print(f'Semantic error: type mismatch - ({result}:{varType}) not boolean)' )
		sys.exit()
	print("call while_expr")

# For
def p_for(p):
	'''
	for : FOR for_asignacion for_to for_exp bloque
	'''
	operand = pOperands.pop()
	index = vm[-1].cteAssign(1)
	result = vm[-1].temporalAssign(int)
	quads.append(('+', operand, index, result))
	quads.append(('=', result, "", operand))

	despues = pJumps.pop()
	antes = pJumps.pop()

	quads.append(("GOTO", "", "", antes))
	quads[despues][3] = len(quads)

	#QuadsID
	global nTemps
	operandID = pOperandsID.pop()
	quadsID.append(('+', operandID, 1, "t" + str(nTemps)))
	quadsID.append(('=', "t" + str(nTemps), "", operandID))

	quadsID.append(("GOTO", "", "", antes))
	quadsID[despues][3] = len(quadsID)
	print("call for")

def p_for_asignacion(p):
	'''
	for_asignacion : variable ASSIGN for_asignacion_expr
	'''
	print("call asignacion")

def p_for_asignacion_expr(p):
	'''
	for_asignacion_expr : expr
	'''
	global currScope
	
	lOperand = pOperands.pop()
	result = pOperands.pop()

	quads.append(("=", lOperand, " ", result))
	pOperands.append(result)

	#QuadsID
	lOperandID = pOperandsID.pop()
	resultID = pOperandsID.pop()

	quadsID.append(("=", lOperandID, " ", resultID))
	pOperandsID.append(resultID)
	print("call asignacion_expr")

def p_for_to(p):
	'''
	for_to : TO
	'''
	pJumps.append(len(quads)) #antes de comp
	print("call for_to")

def p_for_exp(p):
	'''
	for_exp : exp
	'''
	rOperand = pOperands.pop()
	rType = pTypes.pop()
	lOperand = pOperands.pop()
	lType = pTypes.pop()
	resultType = semanticCube['<'][(lType, rType)]
	if resultType != 'error':
		result = vm[-1].temporalAssign(resultType)
		quads.append(('<', lOperand, rOperand, result))
		pOperands.append(result)
		pTypes.append(resultType)
		quads.append(["GOTOF", "", "", None])
		pJumps.append(len(quads) - 1) #despues de comp
		# If any operand were a temporal space, return it to AVAIL

		#QuadsID
		global nTemps
		rOperandID = pOperandsID.pop()
		lOperandID = pOperandsID.pop()
		quadsID.append(('<', lOperandID, rOperandID, "t" + str(nTemps)))
		pOperandsID.append("t" + str(nTemps))
		nTemps += 1
		quadsID.append(["GOTOF", "", "", None])
	else:
		print(f'Semantic error: type mismatch - ({lOperand}:{lType})<({rOperand}:{rType})' )
		sys.exit()
	print("call for_exp")

# Expr
def p_expr(p):
	'''
	expr : or
	'''
	print("call expr")

# Or
def p_or(p):
	'''
	or : and
	   | and or_operador or
	'''
	if len(p) > 2:
		if pOper[-1] == '||':
			rOperand = pOperands.pop()
			rType = pTypes.pop()
			lOperand = pOperands.pop()
			lType = pTypes.pop()
			operator = pOper.pop()
			resultType = semanticCube[operator][(lType, rType)]
			if resultType != 'error':
				result = vm[-1].temporalAssign(resultType)
				quads.append((operator, lOperand, rOperand, result))
				pOperands.append(result)
				pTypes.append(resultType)
				# If any operand were a temporal space, return it to AVAIL

				#QuadsID
				global nTemps
				rOperandID = pOperandsID.pop()
				lOperandID = pOperandsID.pop()
				quadsID.append((operator, lOperandID, rOperandID, "t" + str(nTemps)))
				pOperandsID.append("t" + str(nTemps))
				nTemps += 1
			else:
				print(f'Semantic error: type mismatch - ({lOperand}:{lType}){operator}({rOperand}:{rType})' )
				sys.exit()

	else:
		print("pOper empty.")
	print("call or")

def p_or_operador(p):
	'''
	or_operador : OR
	'''
	pOper.append(p[1])
	print("call or_operador")

# And
def p_and(p):
	'''
	and : equal
		| equal and_operador and
	'''
	if len(p) > 2:
		if pOper[-1] == '&&':
			rOperand = pOperands.pop()
			rType = pTypes.pop()
			lOperand = pOperands.pop()
			lType = pTypes.pop()
			operator = pOper.pop()
			resultType = semanticCube[operator][(lType, rType)]
			if resultType != 'error':
				result = vm[-1].temporalAssign(resultType)
				quads.append((operator, lOperand, rOperand, result))
				pOperands.append(result)
				pTypes.append(resultType)
				# If any operand were a temporal space, return it to AVAIL

				#QuadsID
				global nTemps
				rOperandID = pOperandsID.pop()
				lOperandID = pOperandsID.pop()
				quadsID.append((operator, lOperandID, rOperandID, "t" + str(nTemps)))
				pOperandsID.append("t" + str(nTemps))
				nTemps += 1
			else:
				print(f'Semantic error: type mismatch - ({lOperand}:{lType}){operator}({rOperand}:{rType})' )
				sys.exit()

	else:
		print("pOper empty.")
	print("call and")

def p_and_operador(p):
	'''
	and_operador : AND
	'''
	pOper.append(p[1])
	print("call and_operador")

# Equal
def p_equal(p):
	'''
	equal : compare
		  | compare equal_operador compare
	'''
	if len(p) > 2:
		if pOper[-1] in ('==', '!='):
			rOperand = pOperands.pop()
			rType = pTypes.pop()
			lOperand = pOperands.pop()
			lType = pTypes.pop()
			operator = pOper.pop()
			resultType = semanticCube[operator][(lType, rType)]
			if resultType != 'error':
				result = vm[-1].temporalAssign(resultType)
				quads.append((operator, lOperand, rOperand, result))
				pOperands.append(result)
				pTypes.append(resultType)
				# If any operand were a temporal space, return it to AVAIL

				#QuadsID
				global nTemps
				rOperandID = pOperandsID.pop()
				lOperandID = pOperandsID.pop()
				quadsID.append((operator, lOperandID, rOperandID, "t" + str(nTemps)))
				pOperandsID.append("t" + str(nTemps))
				nTemps += 1
			else:
				print(f'Semantic error: type mismatch - ({lOperand}:{lType}){operator}({rOperand}:{rType})' )
				sys.exit()

	else:
		print("pOper empty.")
	print("call equal")

def p_equal_operador(p):
	'''
	equal_operador : EQUAL
				   | NOT_EQUAL
	'''
	pOper.append(p[1])
	print("call equal_operador")

# Compare
def p_compare(p):
	'''
	compare : exp
			| exp compare_operador exp
	'''
	if len(p) > 2:
		if pOper[-1] in ('>', '<', '>=', '<='):
			rOperand = pOperands.pop()
			rType = pTypes.pop()
			lOperand = pOperands.pop()
			lType = pTypes.pop()
			operator = pOper.pop()
			resultType = semanticCube[operator][(lType, rType)]
			if resultType != 'error':
				result = vm[-1].temporalAssign(resultType)
				quads.append((operator, lOperand, rOperand, result))
				pOperands.append(result)
				pTypes.append(resultType)
				# If any operand were a temporal space, return it to AVAIL

				#QuadsID
				global nTemps
				rOperandID = pOperandsID.pop()
				lOperandID = pOperandsID.pop()
				quadsID.append((operator, lOperandID, rOperandID, "t" + str(nTemps)))
				pOperandsID.append("t" + str(nTemps))
				nTemps += 1
			else:
				print(f'Semantic error: type mismatch - ({lOperand}:{lType}){operator}({rOperand}:{rType})' )
				sys.exit()

	else:
		print("pOper empty.")
	print("call compare")

def p_compare_operador(p):
	'''
	compare_operador : GREATER
					 | LESSER
					 | GREATER_EQUAL
					 | LESSER_EQUAL
	'''
	pOper.append(p[1])
	print("call compare_operador")

# Exp
def p_exp(p):
	'''
	exp : termino
		| termino exp_operador exp
	'''
	global currScope
	# Cambiar try por un if de len(p)
	if len(p) > 2:
		if pOper[-1] in ('+', '-'):
			rOperand = pOperands.pop()
			rType = pTypes.pop()
			lOperand = pOperands.pop()
			lType = pTypes.pop()
			operator = pOper.pop()
			resultType = semanticCube[operator][(lType, rType)]
			if resultType != 'error':
				result = vm[-1].temporalAssign(resultType)
				quads.append((operator, lOperand, rOperand, result))
				pOperands.append(result)
				pTypes.append(resultType)
				# If any operand were a temporal space, return it to AVAIL

				#QuadsID
				global nTemps
				rOperandID = pOperandsID.pop()
				lOperandID = pOperandsID.pop()
				quadsID.append((operator, lOperandID, rOperandID, "t" + str(nTemps)))
				pOperandsID.append("t" + str(nTemps))
				nTemps += 1
			else:
				print(f'Semantic error: type mismatch - ({lOperand}:{lType}){operator}({rOperand}:{rType})' )
				sys.exit()

	else:
		print("pOper empty.")

	print("call exp")

def p_exp_operador(p):
	'''
	exp_operador : PLUS
			 | MINUS
	'''
	pOper.append(p[1])
	print("call exp_operador")

# Termino
def p_termino(p):
	'''
	termino : factor
			| factor termino_operador termino
	'''
	global currScope
	if len(p) > 2:
		if pOper[-1] in ('*', '/', '%'):
			rOperand = pOperands.pop()
			rType = pTypes.pop()
			lOperand = pOperands.pop()
			lType = pTypes.pop()
			operator = pOper.pop()
			resultType = semanticCube[operator][(lType, rType)]
			if resultType != 'error':
				result = vm[-1].temporalAssign(resultType)
				quads.append((operator, lOperand, rOperand, result))
				pOperands.append(result)
				pTypes.append(resultType)
				# If any operand were a temporal space, return it to AVAIL

				#QuadsID
				global nTemps
				rOperandID = pOperandsID.pop()
				lOperandID = pOperandsID.pop()
				quadsID.append((operator, lOperandID, rOperandID, "t" + str(nTemps)))
				pOperandsID.append("t" + str(nTemps))
				nTemps += 1
			else:
				print(f'Semantic error: type mismatch - ({lOperand}:{lType}){operator}({rOperand}:{rType})' )
				sys.exit()
	else:
		print("pOper empty.")
	
	print("call termino")

def p_termino_operador(p):
	'''
	termino_operador : TIMES
					 | DIVIDE
					 | MODULE
	'''
	pOper.append(p[1])
	print("call termino_operador")

# Factor
def p_factor(p):
	'''
	factor : variable
		   | O_PARENTHESIS expr C_PARENTHESIS
		   | llamada
		   | cte
		   | PLUS cte
		   | MINUS cte
	'''
	# if p[1] == variable or p[1] == cte
	print("call factor")

# CTE
def p_cte(p):
	'''
	cte : CTE_INT
		| CTE_FLOAT
	'''
	# Implementar assignVM cte
	index = vm[-1].cteAssign(p[1])
	pOperands.append(index)
	pTypes.append(type(p[1]))

	#QuadsID
	pOperandsID.append(p[1])
	print("call cte")

# Epsilon
def p_epsilon(p):
	'''
	epsilon :
	'''
	print("call epsilon")

def p_error(p):
	print("Parser error with: ", p)

parser = yacc.yacc()

program = None
try:
	s = "testS.txt"#str(input(">> "))
	with open(s, "r") as f:
		program = f.read()
except EOFError :
    print("Error reading code.")

# try:
parser.parse(program)
# except Exception as e:
# 	print("ERR - ",e)