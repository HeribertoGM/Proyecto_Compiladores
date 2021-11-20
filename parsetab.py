
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CHAR COLON COMMA CTE_CHAR CTE_FLOAT CTE_INT CTE_STRING C_ABRACKET C_CBRACKET C_PARENTHESIS DIVIDE ELSE EQUAL FLOAT FOR FUNCTION GREATER GREATER_EQUAL ID IF INT LESSER LESSER_EQUAL LET MAIN MINUS MODULE NOT_EQUAL OR O_ABRACKET O_CBRACKET O_PARENTHESIS PLUS PROGRAM READ RETURN SEMICOLON STRING TIMES TO VOID WHILE WRITE\n\tprograma : PROGRAM ID SEMICOLON declaracion_global funcion main bloque\n\t\n\tmain : MAIN O_PARENTHESIS C_PARENTHESIS\n\t\n\tbloque : O_CBRACKET bloque_prime C_CBRACKET\n\t\n\tbloque_prime : estatuto bloque_prime\n\t\t\t\t | epsilon\n\t\n\tdeclaracion_funcion : declaracion\n\t\n\tdeclaracion_global : declaracion\n\t\n\tdeclaracion : declaracion_base\n\t\t\t\t| declaracion_base declaracion\n\t\n\tdeclaracion_base : LET declaracion_prime COLON declaracion_tipo SEMICOLON\n\t\n\tdeclaracion_prime : declaracion_variable\n\t\t\t\t\t  | declaracion_variable COMMA declaracion_prime\n\t\n\tdeclaracion_variable : ID O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET\n\t\t\t\t\t\t | ID O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET\n\t\t\t\t\t\t | ID O_ABRACKET CTE_INT C_ABRACKET\n\t\t\t\t\t\t | ID \n\t\n\tdeclaracion_tipo : INT\n\t\t\t\t\t | FLOAT\n\t\t\t\t\t | CHAR\n\t\t\t\t\t | STRING\n\t\n\ttipo : INT\n\t\t | FLOAT\n\t\t | CHAR\n\t\t | STRING\n\t\n\tfuncion : funcion_base funcion\n\t\t\t| epsilon\n\t\n\tfuncion_base : FUNCTION funcion_ident O_PARENTHESIS funcion_prime C_PARENTHESIS declaracion_funcion bloque\n\t\n\tfuncion_prime : tipo ID\n\t\t\t\t  | tipo ID COMMA funcion_prime\n\t\n\tfuncion_ident : VOID ID\n \t\t\t\t  | INT ID\n\t\t\t\t  | FLOAT ID\n\t\t\t\t  | CHAR ID\n\t\t\t\t  | STRING ID\n\t\n\tvariable : ID O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET\n\t\t\t | ID O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET\n\t\t\t | ID O_ABRACKET exp C_ABRACKET\n\t\t\t | ID \n\t\n\testatuto : asignacion SEMICOLON\n\t\t\t | llamada SEMICOLON\n\t\t\t | retorno SEMICOLON\n\t\t\t | lectura SEMICOLON\n\t\t\t | escritura SEMICOLON\n\t\t\t | decision\n\t\t\t | while\n\t\t\t | for\n\t\n\tasignacion : variable ASSIGN asignacion_expr\n\t\n\tasignacion_expr : expr\n\t\n\tllamada : ID O_PARENTHESIS llamada_prime C_PARENTHESIS\n\t\n\tllamada_prime : exp\n\t\t\t\t  | exp COMMA llamada_prime\n\t\n\tretorno : RETURN O_PARENTHESIS expr C_PARENTHESIS\n\t\n\tlectura : READ O_PARENTHESIS lectura_prime C_PARENTHESIS\n\t\n\tlectura_prime : variable\n\t\t\t\t  | variable COMMA lectura_prime\n\t\n\tescritura : WRITE O_PARENTHESIS escritura_prime C_PARENTHESIS\n\t\n\tescritura_prime : expr\n\t\t\t\t\t| CTE_STRING\n\t\t\t\t\t| expr COMMA escritura_prime\n\t\t\t\t\t| CTE_STRING COMMA escritura_prime\n\t\n\tdecision : IF O_PARENTHESIS expr C_PARENTHESIS bloque else\n\t\n\telse : ELSE bloque\n\t\t | epsilon\n\t\n\twhile : WHILE O_PARENTHESIS expr C_PARENTHESIS bloque\n\t\n\tfor : FOR variable ASSIGN exp TO exp bloque\n\t\n\texpr : or\n\t\n\tor : and\n\t   | and OR or\n\t\n\tand : equal\n\t\t| equal AND and\n\t\n\tequal : compare\n\t\t  | compare EQUAL compare\n\t\t  | compare NOT_EQUAL compare\n\t\n\tcompare : exp\n\t\t\t| exp GREATER exp\n\t\t\t| exp LESSER exp\n\t\t\t| exp GREATER_EQUAL exp\n\t\t\t| exp LESSER_EQUAL exp\n\t\n\texp : termino\n\t\t| termino exp_operador exp\n\t\n\texp_operador : PLUS\n\t\t\t\t | MINUS\n\t\n\ttermino : factor\n\t\t\t| factor termino_operador termino\n\t\n\ttermino_operador : TIMES\n\t\t\t\t\t | DIVIDE\n\t\t\t\t\t | MODULE\n\t\n\tfactor : variable\n\t\t   | O_PARENTHESIS expr C_PARENTHESIS\n\t\t   | llamada\n\t\t   | cte\n\t\t   | PLUS cte\n\t\t   | MINUS cte\n\t\n\tcte : CTE_INT\n\t\t| CTE_FLOAT\n\t\n\tepsilon :\n\t'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,29,73,],[0,-1,-3,]),'ID':([2,8,21,22,23,24,25,27,30,46,53,54,55,63,66,67,68,69,70,73,75,76,77,78,79,80,81,82,83,84,85,86,87,103,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,146,150,152,153,172,176,177,178,181,183,187,188,190,],[3,16,33,34,35,36,37,16,57,57,-44,-45,-46,89,91,-21,-22,-23,-24,-3,-39,-40,-41,-42,-43,108,108,108,108,89,108,108,108,108,108,108,108,108,108,108,108,108,108,108,-81,-82,108,-85,-86,-87,108,89,108,108,108,-96,-64,108,-61,-63,-62,-65,108,]),'SEMICOLON':([3,38,39,40,41,42,48,49,50,51,52,93,94,95,96,97,98,99,100,101,102,104,105,108,109,110,143,144,145,147,148,149,151,160,161,162,163,164,165,166,167,168,169,170,186,192,],[4,71,-17,-18,-19,-20,75,76,77,78,79,-88,-47,-48,-66,-67,-69,-71,-74,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-52,-53,-56,-68,-70,-72,-73,-75,-76,-77,-78,-80,-84,-89,-36,-35,]),'LET':([4,7,71,90,],[8,8,-10,8,]),'FUNCTION':([5,6,7,10,13,71,73,157,],[12,-7,-8,12,-9,-10,-3,-27,]),'MAIN':([5,6,7,9,10,11,13,19,71,73,157,],[-96,-7,-8,18,-96,-26,-9,-25,-10,-3,-27,]),'O_CBRACKET':([7,13,17,64,71,93,101,102,104,105,108,109,110,123,124,143,144,145,147,154,155,168,169,170,182,184,186,192,],[-8,-9,30,-2,-10,-88,-79,-83,-90,-91,-38,-94,-95,30,-6,-92,-93,-49,-37,30,30,-80,-84,-89,30,30,-36,-35,]),'VOID':([12,],[21,]),'INT':([12,26,32,125,],[22,39,67,67,]),'FLOAT':([12,26,32,125,],[23,40,68,68,]),'CHAR':([12,26,32,125,],[24,41,69,69,]),'STRING':([12,26,32,125,],[25,42,70,70,]),'COLON':([14,15,16,43,72,159,189,],[26,-11,-16,-12,-15,-14,-13,]),'COMMA':([15,16,72,89,91,93,96,97,98,99,100,101,102,104,105,108,109,110,112,116,118,119,143,144,145,147,159,160,161,162,163,164,165,166,167,168,169,170,186,189,192,],[27,-16,-15,-38,125,-88,-66,-67,-69,-71,-74,-79,-83,-90,-91,-38,-94,-95,146,150,152,153,-92,-93,-49,-37,-14,-68,-70,-72,-73,-75,-76,-77,-78,-80,-84,-89,-36,-13,-35,]),'O_ABRACKET':([16,57,72,89,108,147,159,186,],[28,82,92,82,82,172,179,190,]),'O_PARENTHESIS':([18,20,33,34,35,36,37,57,58,59,60,61,62,80,81,82,83,85,86,87,103,108,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,146,152,153,172,178,190,],[31,32,-30,-31,-32,-33,-34,81,83,84,85,86,87,103,103,103,103,103,103,103,103,81,103,103,103,103,103,103,103,103,103,103,-81,-82,103,-85,-86,-87,103,103,103,103,103,103,]),'CTE_INT':([28,80,81,82,83,85,86,87,92,103,106,107,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,146,152,153,172,178,179,190,],[44,109,109,109,109,109,109,109,126,109,109,109,109,109,109,109,109,109,109,109,109,109,-81,-82,109,-85,-86,-87,109,109,109,109,109,185,109,]),'C_CBRACKET':([30,45,46,47,53,54,55,73,74,75,76,77,78,79,176,177,181,183,187,188,],[-96,73,-96,-5,-44,-45,-46,-3,-4,-39,-40,-41,-42,-43,-96,-64,-61,-63,-62,-65,]),'RETURN':([30,46,53,54,55,73,75,76,77,78,79,176,177,181,183,187,188,],[58,58,-44,-45,-46,-3,-39,-40,-41,-42,-43,-96,-64,-61,-63,-62,-65,]),'READ':([30,46,53,54,55,73,75,76,77,78,79,176,177,181,183,187,188,],[59,59,-44,-45,-46,-3,-39,-40,-41,-42,-43,-96,-64,-61,-63,-62,-65,]),'WRITE':([30,46,53,54,55,73,75,76,77,78,79,176,177,181,183,187,188,],[60,60,-44,-45,-46,-3,-39,-40,-41,-42,-43,-96,-64,-61,-63,-62,-65,]),'IF':([30,46,53,54,55,73,75,76,77,78,79,176,177,181,183,187,188,],[61,61,-44,-45,-46,-3,-39,-40,-41,-42,-43,-96,-64,-61,-63,-62,-65,]),'WHILE':([30,46,53,54,55,73,75,76,77,78,79,176,177,181,183,187,188,],[62,62,-44,-45,-46,-3,-39,-40,-41,-42,-43,-96,-64,-61,-63,-62,-65,]),'FOR':([30,46,53,54,55,73,75,76,77,78,79,176,177,181,183,187,188,],[63,63,-44,-45,-46,-3,-39,-40,-41,-42,-43,-96,-64,-61,-63,-62,-65,]),'C_PARENTHESIS':([31,65,89,91,93,96,97,98,99,100,101,102,104,105,108,109,110,111,112,114,115,116,117,118,119,120,121,142,143,144,145,147,158,160,161,162,163,164,165,166,167,168,169,170,171,173,174,175,186,192,],[64,90,-38,-28,-88,-66,-67,-69,-71,-74,-79,-83,-90,-91,-38,-94,-95,145,-50,148,149,-54,151,-57,-58,154,155,170,-92,-93,-49,-37,-29,-68,-70,-72,-73,-75,-76,-77,-78,-80,-84,-89,-51,-55,-59,-60,-36,-35,]),'C_ABRACKET':([44,93,101,102,104,105,108,109,110,113,126,143,144,145,147,168,169,170,180,185,186,191,192,],[72,-88,-79,-83,-90,-91,-38,-94,-95,147,159,-92,-93,-49,-37,-80,-84,-89,186,189,-36,192,-35,]),'ASSIGN':([56,57,88,89,147,186,192,],[80,-38,122,-38,-37,-36,-35,]),'ELSE':([73,176,],[-3,182,]),'PLUS':([80,81,82,83,85,86,87,93,101,102,103,104,105,108,109,110,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,144,145,146,147,152,153,169,170,172,178,186,190,192,],[106,106,106,106,106,106,106,-88,136,-83,106,-90,-91,-38,-94,-95,106,106,106,106,106,106,106,106,106,106,-81,-82,106,-85,-86,-87,-92,-93,-49,106,-37,106,106,-84,-89,106,106,-36,106,-35,]),'MINUS':([80,81,82,83,85,86,87,93,101,102,103,104,105,108,109,110,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,144,145,146,147,152,153,169,170,172,178,186,190,192,],[107,107,107,107,107,107,107,-88,137,-83,107,-90,-91,-38,-94,-95,107,107,107,107,107,107,107,107,107,107,-81,-82,107,-85,-86,-87,-92,-93,-49,107,-37,107,107,-84,-89,107,107,-36,107,-35,]),'CTE_FLOAT':([80,81,82,83,85,86,87,103,106,107,122,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,146,152,153,172,178,190,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,-81,-82,110,-85,-86,-87,110,110,110,110,110,110,]),'CTE_STRING':([85,152,153,],[119,119,119,]),'TIMES':([93,102,104,105,108,109,110,143,144,145,147,170,186,192,],[-88,139,-90,-91,-38,-94,-95,-92,-93,-49,-37,-89,-36,-35,]),'DIVIDE':([93,102,104,105,108,109,110,143,144,145,147,170,186,192,],[-88,140,-90,-91,-38,-94,-95,-92,-93,-49,-37,-89,-36,-35,]),'MODULE':([93,102,104,105,108,109,110,143,144,145,147,170,186,192,],[-88,141,-90,-91,-38,-94,-95,-92,-93,-49,-37,-89,-36,-35,]),'GREATER':([93,100,101,102,104,105,108,109,110,143,144,145,147,168,169,170,186,192,],[-88,131,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-80,-84,-89,-36,-35,]),'LESSER':([93,100,101,102,104,105,108,109,110,143,144,145,147,168,169,170,186,192,],[-88,132,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-80,-84,-89,-36,-35,]),'GREATER_EQUAL':([93,100,101,102,104,105,108,109,110,143,144,145,147,168,169,170,186,192,],[-88,133,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-80,-84,-89,-36,-35,]),'LESSER_EQUAL':([93,100,101,102,104,105,108,109,110,143,144,145,147,168,169,170,186,192,],[-88,134,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-80,-84,-89,-36,-35,]),'EQUAL':([93,99,100,101,102,104,105,108,109,110,143,144,145,147,164,165,166,167,168,169,170,186,192,],[-88,129,-74,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-75,-76,-77,-78,-80,-84,-89,-36,-35,]),'NOT_EQUAL':([93,99,100,101,102,104,105,108,109,110,143,144,145,147,164,165,166,167,168,169,170,186,192,],[-88,130,-74,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-75,-76,-77,-78,-80,-84,-89,-36,-35,]),'AND':([93,98,99,100,101,102,104,105,108,109,110,143,144,145,147,162,163,164,165,166,167,168,169,170,186,192,],[-88,128,-71,-74,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-72,-73,-75,-76,-77,-78,-80,-84,-89,-36,-35,]),'OR':([93,97,98,99,100,101,102,104,105,108,109,110,143,144,145,147,161,162,163,164,165,166,167,168,169,170,186,192,],[-88,127,-69,-71,-74,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,-70,-72,-73,-75,-76,-77,-78,-80,-84,-89,-36,-35,]),'TO':([93,101,102,104,105,108,109,110,143,144,145,147,156,168,169,170,186,192,],[-88,-79,-83,-90,-91,-38,-94,-95,-92,-93,-49,-37,178,-80,-84,-89,-36,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracion_global':([4,],[5,]),'declaracion':([4,7,90,],[6,13,124,]),'declaracion_base':([4,7,90,],[7,7,7,]),'funcion':([5,10,],[9,19,]),'funcion_base':([5,10,],[10,10,]),'epsilon':([5,10,30,46,176,],[11,11,47,47,183,]),'declaracion_prime':([8,27,],[14,43,]),'declaracion_variable':([8,27,],[15,15,]),'main':([9,],[17,]),'funcion_ident':([12,],[20,]),'bloque':([17,123,154,155,182,184,],[29,157,176,177,187,188,]),'declaracion_tipo':([26,],[38,]),'bloque_prime':([30,46,],[45,74,]),'estatuto':([30,46,],[46,46,]),'asignacion':([30,46,],[48,48,]),'llamada':([30,46,80,81,82,83,85,86,87,103,122,127,128,129,130,131,132,133,134,135,138,146,152,153,172,178,190,],[49,49,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'retorno':([30,46,],[50,50,]),'lectura':([30,46,],[51,51,]),'escritura':([30,46,],[52,52,]),'decision':([30,46,],[53,53,]),'while':([30,46,],[54,54,]),'for':([30,46,],[55,55,]),'variable':([30,46,63,80,81,82,83,84,85,86,87,103,122,127,128,129,130,131,132,133,134,135,138,146,150,152,153,172,178,190,],[56,56,88,93,93,93,93,116,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,93,116,93,93,93,93,93,]),'funcion_prime':([32,125,],[65,158,]),'tipo':([32,125,],[66,66,]),'asignacion_expr':([80,],[94,]),'expr':([80,83,85,86,87,103,152,153,],[95,114,118,120,121,142,118,118,]),'or':([80,83,85,86,87,103,127,152,153,],[96,96,96,96,96,96,160,96,96,]),'and':([80,83,85,86,87,103,127,128,152,153,],[97,97,97,97,97,97,97,161,97,97,]),'equal':([80,83,85,86,87,103,127,128,152,153,],[98,98,98,98,98,98,98,98,98,98,]),'compare':([80,83,85,86,87,103,127,128,129,130,152,153,],[99,99,99,99,99,99,99,99,162,163,99,99,]),'exp':([80,81,82,83,85,86,87,103,122,127,128,129,130,131,132,133,134,135,146,152,153,172,178,190,],[100,112,113,100,100,100,100,100,156,100,100,100,100,164,165,166,167,168,112,100,100,180,184,191,]),'termino':([80,81,82,83,85,86,87,103,122,127,128,129,130,131,132,133,134,135,138,146,152,153,172,178,190,],[101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,169,101,101,101,101,101,101,]),'factor':([80,81,82,83,85,86,87,103,122,127,128,129,130,131,132,133,134,135,138,146,152,153,172,178,190,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'cte':([80,81,82,83,85,86,87,103,106,107,122,127,128,129,130,131,132,133,134,135,138,146,152,153,172,178,190,],[105,105,105,105,105,105,105,105,143,144,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'llamada_prime':([81,146,],[111,171,]),'lectura_prime':([84,150,],[115,173,]),'escritura_prime':([85,152,153,],[117,174,175,]),'declaracion_funcion':([90,],[123,]),'exp_operador':([101,],[135,]),'termino_operador':([102,],[138,]),'else':([176,],[181,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID SEMICOLON declaracion_global funcion main bloque','programa',7,'p_programa','Parser.py',9),
  ('main -> MAIN O_PARENTHESIS C_PARENTHESIS','main',3,'p_main','Parser.py',20),
  ('bloque -> O_CBRACKET bloque_prime C_CBRACKET','bloque',3,'p_bloque','Parser.py',28),
  ('bloque_prime -> estatuto bloque_prime','bloque_prime',2,'p_bloque_prime','Parser.py',34),
  ('bloque_prime -> epsilon','bloque_prime',1,'p_bloque_prime','Parser.py',35),
  ('declaracion_funcion -> declaracion','declaracion_funcion',1,'p_declaracion_funcion','Parser.py',42),
  ('declaracion_global -> declaracion','declaracion_global',1,'p_declaracion_global','Parser.py',50),
  ('declaracion -> declaracion_base','declaracion',1,'p_declaracion','Parser.py',58),
  ('declaracion -> declaracion_base declaracion','declaracion',2,'p_declaracion','Parser.py',59),
  ('declaracion_base -> LET declaracion_prime COLON declaracion_tipo SEMICOLON','declaracion_base',5,'p_declaracion_base','Parser.py',65),
  ('declaracion_prime -> declaracion_variable','declaracion_prime',1,'p_declaracion_prime','Parser.py',71),
  ('declaracion_prime -> declaracion_variable COMMA declaracion_prime','declaracion_prime',3,'p_declaracion_prime','Parser.py',72),
  ('declaracion_variable -> ID O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET','declaracion_variable',10,'p_declaracion_variable','Parser.py',79),
  ('declaracion_variable -> ID O_ABRACKET CTE_INT C_ABRACKET O_ABRACKET CTE_INT C_ABRACKET','declaracion_variable',7,'p_declaracion_variable','Parser.py',80),
  ('declaracion_variable -> ID O_ABRACKET CTE_INT C_ABRACKET','declaracion_variable',4,'p_declaracion_variable','Parser.py',81),
  ('declaracion_variable -> ID','declaracion_variable',1,'p_declaracion_variable','Parser.py',82),
  ('declaracion_tipo -> INT','declaracion_tipo',1,'p_declaracion_tipo','Parser.py',101),
  ('declaracion_tipo -> FLOAT','declaracion_tipo',1,'p_declaracion_tipo','Parser.py',102),
  ('declaracion_tipo -> CHAR','declaracion_tipo',1,'p_declaracion_tipo','Parser.py',103),
  ('declaracion_tipo -> STRING','declaracion_tipo',1,'p_declaracion_tipo','Parser.py',104),
  ('tipo -> INT','tipo',1,'p_tipo','Parser.py',118),
  ('tipo -> FLOAT','tipo',1,'p_tipo','Parser.py',119),
  ('tipo -> CHAR','tipo',1,'p_tipo','Parser.py',120),
  ('tipo -> STRING','tipo',1,'p_tipo','Parser.py',121),
  ('funcion -> funcion_base funcion','funcion',2,'p_funcion','Parser.py',128),
  ('funcion -> epsilon','funcion',1,'p_funcion','Parser.py',129),
  ('funcion_base -> FUNCTION funcion_ident O_PARENTHESIS funcion_prime C_PARENTHESIS declaracion_funcion bloque','funcion_base',7,'p_funcion_base','Parser.py',135),
  ('funcion_prime -> tipo ID','funcion_prime',2,'p_funcion_prime','Parser.py',141),
  ('funcion_prime -> tipo ID COMMA funcion_prime','funcion_prime',4,'p_funcion_prime','Parser.py',142),
  ('funcion_ident -> VOID ID','funcion_ident',2,'p_funcion_ident','Parser.py',148),
  ('funcion_ident -> INT ID','funcion_ident',2,'p_funcion_ident','Parser.py',149),
  ('funcion_ident -> FLOAT ID','funcion_ident',2,'p_funcion_ident','Parser.py',150),
  ('funcion_ident -> CHAR ID','funcion_ident',2,'p_funcion_ident','Parser.py',151),
  ('funcion_ident -> STRING ID','funcion_ident',2,'p_funcion_ident','Parser.py',152),
  ('variable -> ID O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET','variable',10,'p_variable','Parser.py',160),
  ('variable -> ID O_ABRACKET exp C_ABRACKET O_ABRACKET exp C_ABRACKET','variable',7,'p_variable','Parser.py',161),
  ('variable -> ID O_ABRACKET exp C_ABRACKET','variable',4,'p_variable','Parser.py',162),
  ('variable -> ID','variable',1,'p_variable','Parser.py',163),
  ('estatuto -> asignacion SEMICOLON','estatuto',2,'p_estatuto','Parser.py',182),
  ('estatuto -> llamada SEMICOLON','estatuto',2,'p_estatuto','Parser.py',183),
  ('estatuto -> retorno SEMICOLON','estatuto',2,'p_estatuto','Parser.py',184),
  ('estatuto -> lectura SEMICOLON','estatuto',2,'p_estatuto','Parser.py',185),
  ('estatuto -> escritura SEMICOLON','estatuto',2,'p_estatuto','Parser.py',186),
  ('estatuto -> decision','estatuto',1,'p_estatuto','Parser.py',187),
  ('estatuto -> while','estatuto',1,'p_estatuto','Parser.py',188),
  ('estatuto -> for','estatuto',1,'p_estatuto','Parser.py',189),
  ('asignacion -> variable ASSIGN asignacion_expr','asignacion',3,'p_asignacion','Parser.py',196),
  ('asignacion_expr -> expr','asignacion_expr',1,'p_asignacion_expr','Parser.py',202),
  ('llamada -> ID O_PARENTHESIS llamada_prime C_PARENTHESIS','llamada',4,'p_llamada','Parser.py',222),
  ('llamada_prime -> exp','llamada_prime',1,'p_llamada_prime','Parser.py',228),
  ('llamada_prime -> exp COMMA llamada_prime','llamada_prime',3,'p_llamada_prime','Parser.py',229),
  ('retorno -> RETURN O_PARENTHESIS expr C_PARENTHESIS','retorno',4,'p_retorno','Parser.py',237),
  ('lectura -> READ O_PARENTHESIS lectura_prime C_PARENTHESIS','lectura',4,'p_lectura','Parser.py',244),
  ('lectura_prime -> variable','lectura_prime',1,'p_lectura_prime','Parser.py',250),
  ('lectura_prime -> variable COMMA lectura_prime','lectura_prime',3,'p_lectura_prime','Parser.py',251),
  ('escritura -> WRITE O_PARENTHESIS escritura_prime C_PARENTHESIS','escritura',4,'p_escritura','Parser.py',258),
  ('escritura_prime -> expr','escritura_prime',1,'p_escritura_prime','Parser.py',264),
  ('escritura_prime -> CTE_STRING','escritura_prime',1,'p_escritura_prime','Parser.py',265),
  ('escritura_prime -> expr COMMA escritura_prime','escritura_prime',3,'p_escritura_prime','Parser.py',266),
  ('escritura_prime -> CTE_STRING COMMA escritura_prime','escritura_prime',3,'p_escritura_prime','Parser.py',267),
  ('decision -> IF O_PARENTHESIS expr C_PARENTHESIS bloque else','decision',6,'p_decision','Parser.py',275),
  ('else -> ELSE bloque','else',2,'p_else','Parser.py',281),
  ('else -> epsilon','else',1,'p_else','Parser.py',282),
  ('while -> WHILE O_PARENTHESIS expr C_PARENTHESIS bloque','while',5,'p_while','Parser.py',289),
  ('for -> FOR variable ASSIGN exp TO exp bloque','for',7,'p_for','Parser.py',296),
  ('expr -> or','expr',1,'p_expr','Parser.py',303),
  ('or -> and','or',1,'p_or','Parser.py',310),
  ('or -> and OR or','or',3,'p_or','Parser.py',311),
  ('and -> equal','and',1,'p_and','Parser.py',318),
  ('and -> equal AND and','and',3,'p_and','Parser.py',319),
  ('equal -> compare','equal',1,'p_equal','Parser.py',326),
  ('equal -> compare EQUAL compare','equal',3,'p_equal','Parser.py',327),
  ('equal -> compare NOT_EQUAL compare','equal',3,'p_equal','Parser.py',328),
  ('compare -> exp','compare',1,'p_compare','Parser.py',335),
  ('compare -> exp GREATER exp','compare',3,'p_compare','Parser.py',336),
  ('compare -> exp LESSER exp','compare',3,'p_compare','Parser.py',337),
  ('compare -> exp GREATER_EQUAL exp','compare',3,'p_compare','Parser.py',338),
  ('compare -> exp LESSER_EQUAL exp','compare',3,'p_compare','Parser.py',339),
  ('exp -> termino','exp',1,'p_exp','Parser.py',346),
  ('exp -> termino exp_operador exp','exp',3,'p_exp','Parser.py',347),
  ('exp_operador -> PLUS','exp_operador',1,'p_exp_operador','Parser.py',375),
  ('exp_operador -> MINUS','exp_operador',1,'p_exp_operador','Parser.py',376),
  ('termino -> factor','termino',1,'p_termino','Parser.py',384),
  ('termino -> factor termino_operador termino','termino',3,'p_termino','Parser.py',385),
  ('termino_operador -> TIMES','termino_operador',1,'p_termino_operador','Parser.py',413),
  ('termino_operador -> DIVIDE','termino_operador',1,'p_termino_operador','Parser.py',414),
  ('termino_operador -> MODULE','termino_operador',1,'p_termino_operador','Parser.py',415),
  ('factor -> variable','factor',1,'p_factor','Parser.py',423),
  ('factor -> O_PARENTHESIS expr C_PARENTHESIS','factor',3,'p_factor','Parser.py',424),
  ('factor -> llamada','factor',1,'p_factor','Parser.py',425),
  ('factor -> cte','factor',1,'p_factor','Parser.py',426),
  ('factor -> PLUS cte','factor',2,'p_factor','Parser.py',427),
  ('factor -> MINUS cte','factor',2,'p_factor','Parser.py',428),
  ('cte -> CTE_INT','cte',1,'p_cte','Parser.py',436),
  ('cte -> CTE_FLOAT','cte',1,'p_cte','Parser.py',437),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','Parser.py',447),
]
