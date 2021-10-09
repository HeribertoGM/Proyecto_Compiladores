
import ply.lex as lex
import ply.yacc as yacc

from Semantic import addGlobalVariables, addLocalVariables, addMethod, addVariableTemp, addTypeTemp, printVars

# -----------------------
# Lexer
# -----------------------

tokens = [
	# palabras reservadas
	'PROGRAM',
	'MAIN',
	'LET',
	'INT',
	'FLOAT',
	'CHAR',
	'STRING',
	'FUNCTION',
	'VOID',
	'RETURN',
	'READ',
	'WRITE',
	'IF',
	'ELSE',
	'WHILE',
	'FOR',
	'TO',
	# puntuacion
	'O_CBRACKET',
	'C_CBRACKET',
	'O_PARENTHESIS',
	'C_PARENTHESIS',
	'O_ABRACKET',
	'C_ABRACKET',
	'SEMICOLON',
	'COLON',
	'COMMA',
	# operadores
	'ASSIGN',
	'OR',
	'AND',
	'EQUAL',
	'NOT_EQUAL',
	'GREATER',
	'LESSER',
	'GREATER_EQUAL',
	'LESSER_EQUAL',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'MODULE',
	# regex
	'ID',
	'CTE_INT',
	'CTE_FLOAT',
	'CTE_CHAR',
	'CTE_STRING'
]

reserved = {
	'program': 'PROGRAM',
	'main': 'MAIN',
	'let': 'LET',
	'int': 'INT',
	'float': 'FLOAT',
	'char': 'CHAR',
	'string': 'STRING',
	'function': 'FUNCTION',
 	'void': 'VOID',
	'return': 'RETURN',
	'read': 'READ',
	'write': 'WRITE',
	'if': 'IF',
	'else': 'ELSE',
	'while': 'WHILE',
 	'for': 'FOR',
	'to': 'TO',
}

t_O_CBRACKET = r'\{'
t_C_CBRACKET = r'\}'
t_O_PARENTHESIS = r'\('
t_C_PARENTHESIS = r'\)'
t_O_ABRACKET = r'\['
t_C_ABRACKET = r'\]'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMMA = r'\,'

t_ASSIGN = r'\='
t_OR = r'\|\|'
t_AND = r'\&\&'
t_EQUAL = r'\=\='
t_NOT_EQUAL = r'\!\='
t_GREATER = r'\>'
t_LESSER = r'\<'
t_GREATER_EQUAL = r'\>\='
t_LESSER_EQUAL = r'\<\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MODULE = r'\%'

t_ignore = ' \t\n'

def t_PROGRAM(t):
	r'program'
	return t

def t_MAIN(t):
	r'main'
	return t

def t_LET(t):
	r'let'
	return t

def t_INT(t):
	r'int'
	return t

def t_FLOAT(t):
	r'float'
	return t

def t_CHAR(t):
	r'char'
	return t

def t_STRING(t):
	r'string'
	return t

def t_FUNCTION(t):
	r'function'
	return t

def t_VOID(t):
	r'void'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_READ(t):
	r'read'
	return t

def t_WRITE(t):
	r'write'
	return t

def t_IF(t):
	r'if'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_FOR(t):
	r'for'
	return t

def t_TO(t):
	r'to'
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = 'ID'
	return t

def t_CTE_FLOAT(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_CTE_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_CTE_CHAR(t):
	r'(\')[a-zA-Z0-9_]*(\')'
	t.value = str(t.value)
	return t

def t_CTE_STRING(t):
	r'(\")[a-zA-Z0-9_]*(\")'
	t.value = str(t.value)
	return t

def t_error(t):
	print("lexer error with: ", t.value)
	t.lexer.skip(1)

lexer = lex.lex()


# inp = str(input(">> "))
# while inp != "":
# 	lexer.input(inp)
# 	while True:
# 		tok = lexer.token()
# 		if not tok:
# 			break
# 		print(tok)

# 	inp = str(input(">> "))


# -----------------------
# Parser
# -----------------------

# Programa
def p_programa(p):
	'''
	programa : PROGRAM ID SEMICOLON declaracion_global funcion MAIN O_PARENTHESIS C_PARENTHESIS bloque
	'''
	print("call programa")
	addMethod(p[2], None, True)
	printVars()

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
	addVariableTemp(p[1])
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
	print("call factor")

# CTE
def p_cte(p):
	'''
	cte : CTE_INT
		| CTE_FLOAT
	'''
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
    print("ERR")
	
parser.parse(program)