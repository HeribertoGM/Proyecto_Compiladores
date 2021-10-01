
import ply.lex as lex
import ply.yacc as yacc

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

t_ignore = '[ \t\n]'

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

