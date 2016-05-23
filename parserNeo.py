import ply.yacc as yacc

# Simbolo inicial
def p_S(p):
	'''S : TkWith LDEC TkBegin INST TkEnd
		 | tkBegin INST TkEnd'''

# Declaracion de variables
def p_DEC(p):
	'''DEC : TkVar LID TkDosPuntos TIPO'''

# lista de identificadores
def p_LID(p):
	'''LID : LID TkComa TkID
		   | LID TkComa TkId TkIzq EXP
		   | TkId
		   | TkId TkIzq EXP'''
# Tipo
def p_TIPO(p):
	'''TIPO : TkInt
			| TkChar
			| TkBool
			| DMATRIZ'''

# Declaracion de matrices
def p_DMATRIZ(p):
	'''DMATRIZ : TkMatrix TkCorcheteAbre LDIM TkCorcheteCierra TkOf TIPO'''

# Lista de dimensiones
def p_LDIM(p):
	'''LDIM : LDIM TkComa TkInt
			| TkInt'''

# Instrucciones
def p_INST(p):
	'''INST : TkId TkIzq EXP TkPunto
			| INST INST TkPunto
			| IF TkPunto
			| REPDET TkPunto
			| REPIND TkPunto
			| S TkPunto
			| TkRead TkId TkPunto
			| TkPrint EXP TkPunto'''

# Lista de declaraciones de variables
def p_LDEC(p):
	'''LDEC : LDEC
			| LDEC LDEC'''

# Tipos de expresiones
def p_EXP(p):
	'''EXP : ARIT
		   | BOOL
		   | CHAR
		   | MATRIZ
		   | REL'''

# Condicional
def p_IF(p):
	''' IF : TkIf BOOL TkDer INST TkEnd
		   | tKIF BOOL TkDer INST TkOtherwise TkDer INST TkEnd'''

# Iteraciones determinadas
def p_REPDET(p):
	'''REPDET : TkFor TkId TkFrom ARIT to ARIT TkDer INST TkEnd
			  | TkFor Tkid TkFrom ARIT to ARIT TkStep ARIT TkDer INST TkEnd'''

# Iteraconies indeterminadas
def p_REPIND(p):
	'''REPINTD : TkWhile BOOL TkDer INST TkEnd'''

# Expresiones aritmeticas
def p_ARIT(p):
	'''ARIT : ARIT TkSuma ARIT
			| ARIT TkResta ARIT
			| ARIT TkDiv ARIT
			| ARIT TkMult ARIT
			| ARIT Tkmod ARIT
			| TkParAbre ARIT TkParCierra
			| TkNum'''

def p_UMENOS(p):
    'ARIT : TkResta ARIT %prec UMENOS'

# Expresiones booleanas
def p_BOOL(p):
	'''BOOL : BOOL TkDisyuncion BOOL
			| BOOL TkConjuncion BOOL
			| TkNot BOOL
			| TkParAbre BOOL TkParCierra
			| TkTrue
			| TkFalse'''

#Expresiones de caracteres
def p_CHAR(p):
	'''CHAR : TkChar TkSiguienteCar
			| TkChar TkAnteriorCar
			| TkValorAscii TkChar'''

# Expresiones matriciales
def p_MATRIZ(p):
	'''MATRIZ : MATRIZ TkConcatenacion MATRIZ
			  | MATRIZ TkTrasposicion
			  | TkRotacion MATRIZ
			  | TkParAbre MATRIZ TkParCierra
			  | TkLlaveAbre LDIM TkLlaveCierra
			  | TkLlaveAbre MATRIZ TkComa MATRIZ TkLlaveCierra'''

# Expresiones relacionales
def p_REL(p):
	'''REL : ARCH TkMenor ARCH
		   | ARCH TkMenorIgual ARCH
		   | ARCH TkMayor ARCH
		   | ARCH TkMayorIgual ARCH
		   | ARCH TkIgual ARCH
		   | ARCH TkNoIgual ARCH
		   | BOOLM TkIgual BOOLM
		   | BOOLM TkNoIgual BOOLM'''

# Agrupacion de expresiones aritmeticas y de caracteres
def p_ARCH(p):
	'''ARCH : ARITM
	        | CHAR'''

# Agrupacion de expresoines booleanas y matriciales
def p_BOOLM(p):
	'''BOOLM : BOOL
			 | MATRIZ'''

precedence = (
	('left', 'TkSuma', 'TkResta', 'TkDisyuncion', 'TkSiguienteCar', 'TkAnteriorCar', 'TkConcatenacion'),
	('left' , 'TkMult', 'TkDiv', 'TkMod', 'TkConjuncion'),
	('right', 'TkRotacion'),
	('left', 'TkTrasposicion')
	('right', 'UMENOS', 'TkNot', 'TkValorAscii'),
)

