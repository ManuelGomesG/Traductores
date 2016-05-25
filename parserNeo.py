import ply.yacc as yacc

global T

T=InstrTree()

# Simbolo inicial
def p_S(p):
	'''S : TkWith LDEC TkBegin INST TkEnd
		 | tkBegin INST TkEnd'''
	if(len(p)==6):
		T.addToken("Start")
		T.addChildren([p[2],p[4]])

	else:
		T.addChildren(p2)
		T.addToken("Start")

	p[0]=T




# Declaracion de variables
def p_DEC(p):
	'''DEC : TkVar LID TkDosPuntos TIPO'''
	p[0]=InstrTree("Declaration",[p[1],p[3]])


# lista de identificadores
def p_LID(p):
	'''LID : TkId TkComa LID
		   | LID TkComa TkId TkIzq EXP
		   | TkId
		   | TkId TkIzq EXP'''



	if(len(p)==6):
		p[0]=InstrTree("IdList",[p[1],p[3],p[5]])
	if(len(p)==4):
		p[0]==InstrTree("IdList",[p[1],p[3]])
	else:
		p[0]==InstrTree("IdList",p[1])



# Tipo
def p_TIPO(p):
	'''TIPO : TkInt
			| TkChar
			| TkBool
			| DMATRIZ'''

	p[0]=InstrTree["Type",p[1]]



# Declaracion de matrices
def p_DMATRIZ(p):
	'''DMATRIZ : TkMatrix TkCorcheteAbre LDIM TkCorcheteCierra TkOf TIPO'''

	p[0]=InstrTree("MatrixDeclaration",[p[3],p[6]])


# Lista de dimensiones
def p_LDIM(p):
	'''LDIM : LDIM TkComa TkInt
			| TkInt'''

	if(len(p)==4):
		p[0]=InstrTree("MatrixDimension"[p[1],p[3]])
	else:
		p[0]=p[1]

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

	if(len(p)==5):
		p[0]=InstrTree("Instruction",[p[1],p[3]])
	if(len(p)==4):
		if(p[1]=='print'):
			p[0]=InstrTree("Instruction",p[2])
		elif(p[1]=='read'):
			p[0]=InstrTree("Instruction",p[2])
		else:
			p[0]=InstrTree("Instruction",[p[1],p[2]])

	else:
		p[0]=InstrTree("Instruction", p[1])



# Lista de declaraciones de variables
def p_LDEC(p):
	'''LDEC : DEC
			| DEC LDEC'''

	if(len(p)==3):
		p[0]=InstrTree("DeclarationList",[p[1],p[2]])
	else:
		p[0]=InstrTree("DeclarationList", p[1])


# Tipos de expresiones
def p_EXP(p):
	'''EXP : ARIT
		   | BOOL
		   | CHAR
		   | MATRIZ
		   | REL'''
	p[0]=InstrTree("Expresion", p[1])

# Condicional
def p_IF(p):
	''' IF : TkIf BOOL TkDer INST TkEnd
		   | tKIF BOOL TkDer INST TkOtherwise TkDer INST TkEnd'''

	if(len(p)==6):
		p[0]=InstrTree("IfInstruction",[p[2],p[4]])
	else:
		p[0]=InstrTree("IfInstruction",[p[2],p[4],p[7]])

# Iteraciones determinadas
def p_REPDET(p):
	'''REPDET : TkFor TkId TkFrom ARIT TkTo ARIT TkDer INST TkEnd
			  | TkFor Tkid TkFrom ARIT TkTo ARIT TkStep ARIT TkDer INST TkEnd'''
	if(len(p)==10):
		p[0]=InstrTree("DetIteration",[p[2],p[4],p[6],p[8]])
	else:
		p[0]=InstrTree("DetIteration",[p[2],p[4],p[6],p[8],p[10]])


# Iteraconies indeterminadas
def p_REPIND(p):
	'''REPINTD : TkWhile BOOL TkDer INST TkEnd'''
	p[0]=InstrTree("DetIteration",[p[2],p[4]])

# Expresiones aritmeticas
def p_ARIT(p):
	'''ARIT : ARIT TkSuma ARIT
			| ARIT TkResta ARIT
			| ARIT TkDiv ARIT
			| ARIT TkMult ARIT
			| ARIT Tkmod ARIT
			| ARIT TkIgual ARIT
			| TkParAbre ARIT TkParCierra
			| TkNum'''

	if(p[2]=='+'):
		p[0]=BinaryOp(p[1],p[3],p[2],"Plus","Arithmetic")
	elif(p[2]=='-'):
		p[0]=BinaryOp(p[1],p[3],p[2],"Minus","Arithmetic")
	elif(p[2]=='/'):
		p[0]=BinaryOp(p[1],p[3],p[2],"Divide","Arithmetic")
	elif(p[2]=='*'):
		p[0]=BinaryOp(p[1],p[3],p[2],"Times","Arithmetic")
	elif(p[2]=='%'):
		p[0]=BinaryOp(p[1],p[3],p[2],"Mod","Arithmetic")
	elif(p[1] == "(" and p[3] == ")"):
		p[0]=p[2]
	elif (p[2] == "="):
		p[0]=BinaryOp(p[1],p[3],p[2],"Equals","Arithmetic")
	else:
		p[0]=Number(p[2])


def p_UMENOS(p):
    'ARIT : TkResta ARIT %prec UMENOS'
    p[0]=UnaryOp(p[1],"Negative",p[2],"Arithmetic")

# Expresiones booleanas
def p_BOOL(p):
	'''BOOL : BOOL TkDisyuncion BOOL
			| BOOL TkConjuncion BOOL
			| BOOL TkIgual BOOL
			| TkNot BOOL
			| TkParAbre BOOL TkParCierra
			| TkTrue
			| TkFalse'''

	if(len(p)==3):
		if(p[2] == "/\\"):
			p[0]=BinaryOp(p[1],p[3],p[2],"Conjuction","Boolean")
		elif (p[2] == "\\/"):	
			p[0]=BinaryOp(p[1],p[3],p[2],"Disjuction","Boolean")
		elif (p[2] == "="):
			p[0]=BinaryOp(p[1],p[3],p[2],"Equals","Boolean")
		else:
			p[0]=p[2]
	elif(len(p)==2):
		p[0]=UnaryOp(p[1],"Negation",p[2],"Arithmetic")
	elif(p[1]=='True' or 'False'):
		p[0]=Bool(p[1])



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

	if()

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

