

import ply.lex as lex
import sys
from classes import *

global tokenlist

tokenlist=tkList()


with open(sys.argv[1], 'r') as content_file:
	content = 	content_file.read()
content_file.close()


tokens = (
	"TkBegin","TkWhile","TkBool","TkIf","TkId", "TkNum", "TkTrue", "TkFalse",
	"TkCaracter", "TkComa", "TkPunto", "TkDosPuntos", "TkParAbre", 
	"TkParCierra", "TkCorcheteAbre", "TkCorcheteCierra", "TkLlaveAbre", 
	"TkLlaveCierra", "TkHacer", "TkAsignacion", "TkSuma", "TkResta", "TkMulr",
	"TkDiv", "TkMod", "TkConjuncion", "TkDisyuncion", "TkNegacion", "TkMenor",
	"TkMenorIgual", "TkMayor", "TkMayorIgual", "TkIgual", "TkSiguienteCar",
	"TkAnteriorCar", "TkValorAscii", "TkConcatenacion", "TkRotacion", 
	"TkTrasposicion","TkEnd", "TkInt", "TkMult", "TkWith", "TkNegacion",
	)


# Palabras reservadas con sus tokens respectivos.
reserved = {
	"begin":	"TkBegin",
	"while":	"TkWhile",
	"bool":		"TkBool",
	"if":		"TkIf",
	"end":		"TkEnd",
	"int":		"TkInt",
	"char":		"TkChar",
	"with":		"TkWith",
	"not":		"TkNegacio"
	}

#------------------------------------------------------------------------------#
#									REGLAS									   #
#------------------------------------------------------------------------------#


# Expresiones Regulares para los tokens simples.




t_TkComa			= r'\,'
t_TkPunto			= r'\.'
t_TkDosPuntos		= r'\:'
t_TkParAbre 		= r'\('
t_TkParCierra		= r'\)'
t_TkCorcheteAbre	= r'\['
t_TkCorcheteCierra	= r'\]'
t_TkLlaveAbre		= r'\{'
t_TkLlaveCierra		= r'\}'
t_TkHacer			= r'\-\>'
t_TkAsignacion		= r'\<\-'
t_TkSuma			= r'\+'
t_TkResta   		= r'\-'
t_TkMult    		= r'\*'
t_TkDiv     		= r'\/'
t_TkMod				= r'\%'
t_TkConjuncion		= r'\/\\'
t_TkDisyuncion		= r'\\\/'
t_TkNegacion		= r'not'
t_TkMenor			= r'\<'
t_TkMenorIgual		= r'\<\='
t_TkMayor			= r'\>'
t_TkMayorIgual		= r'\>\='
t_TkIgual 			= r'\='
t_TkSiguienteCar	= r'\+\+'
t_TkAnteriorCar	= r'\-'
t_TkValorAscii		= r'\#'
t_TkConcatenacion	= r'\:\:'
t_TkRotacion 		= r'\$'
t_TkTrasposicion	= r'\?'



def find_column(input, tok):
		"""
		Busqueda de la columna de un token dado
		"""
		last_cr = input.rfind('\n',1, tok.lexpos)
		if last_cr < 0:
			last_cr = -1
		column = (tok.lexpos - last_cr) 
		return column


# Definición de los enteros
def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)    
    return t

#Definición de caracteres    
def t_TkCaracter(t):
	r'\'.\''
	t.type = reserved.get(t.value,'TkCaracter')
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'



# Manejo de errores
def t_error(t):
    print("Error: Caracter inesperado "+ '"' +\
	 t.value[0] + '"' + " en la fila " + str(t.lineno) +", columna " +\
	  str(find_column(content, t)))
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'TkId')    # Check for reserved words
    return t

def t_Comment(t):	
	r'%{.*}%'
	for commentContent in t.value:
		for word in commentContent:
			if (word == '\n'):
				t.lexer.lineno += 1
	t.lexer.lineno += 1
	t.lexer.skip(1)

# Generando el lexer
