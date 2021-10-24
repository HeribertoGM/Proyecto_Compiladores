import ply.yacc as yacc
from Lexer import *
from Semantic import *

# Programa
def p_programa(p):
	'''
	programa : PROGRAM ID SEMICOLON declaracion_global funcion MAIN O_PARENTHESIS C_PARENTHESIS bloque
	'''
	print("call programa")
	addMethod(p[2], None, True)
	deleteSemanticCube()
	printVars()
	printQuads()

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
	print("call declaracion_funcion")

def p_declaracion_global(p):
	'''
	declaracion_global : declaracion
	'''
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
	variable : ID O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET
			 | ID O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET
			 | ID O_ABRACKET exp C_ABRACKET
			 | ID 
	'''
	pOperands.append(p[1])
	# pTypes.append(functionDictionary[-1]['functionVariables'][VAR_ID][TYPE])
	print("call variable")

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
	asignacion : variable ASSIGN expr
	'''
	print("call asignacion")

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
					| CTE_STRING
					| expr COMMA escritura_prime
					| CTE_STRING COMMA escritura_prime
	'''
	# AssignVM cte
	print("call escritura_prime")

# Decision
def p_decision(p):
	'''
	decision : IF O_PARENTHESIS expr C_PARENTHESIS bloque else
	'''
	print("call decision")

def p_else(p):
	'''
	else : ELSE bloque
		 | epsilon
	'''
	print("call else")

# While
def p_while(p):
	'''
	while : WHILE O_PARENTHESIS expr C_PARENTHESIS bloque
	'''
	print("call while")

# For
def p_for(p):
	'''
	for : FOR variable ASSIGN exp TO exp bloque
	'''
	print("call for")

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
	   | and OR or
	'''
	print("call or")

# And
def p_and(p):
	'''
	and : equal
		| equal AND and
	'''
	print("call and")

# Equal
def p_equal(p):
	'''
	equal : compare
		  | compare EQUAL compare
		  | compare NOT_EQUAL compare
	'''
	print("call equal")

# Compare
def p_compare(p):
	'''
	compare : exp
			| exp GREATER exp
			| exp LESSER exp
			| exp GREATER_EQUAL exp
			| exp LESSER_EQUAL exp
	'''
	print("call compare")

# Exp
def p_exp(p):
	'''
	exp : termino
		| termino PLUS exp
		| termino MINUS exp
	'''
	print("call exp")

# Termino
def p_termino(p):
	'''
	termino : factor
			| factor TIMES termino
			| factor DIVIDE termino
			| factor MODULE termino
	'''
	try:
		if pOper[-1] in ('*', '/', '%'):
			rOperand = pOperands.pop()
			rType = pTypes.pop()
			lOperand = pOperands.pop()
			lType = pTypes.pop()
			operator = pOper.pop()
			resultType = semanticCube[operator][(lType, rType)]
			if resultType != 'error':
				# result = AVAIL.next()
				# # # # TRATAR DE Buscar variable como local y luego global
				# quads.append((operator, lOperand, rOperand, result))
				# pOperands.append(result)
				print("",end="")

			else:
				print("Semantic error: type mismatch.")
	except:
		print("pOper empty.")

	try:
		pOper.append(p[2])
	except:
		print("No operator")

	print("call termino")

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

parser.parse(program)