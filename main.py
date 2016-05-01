#!/usr/bin/python3
# Universidad Simon Bolívar 
#
# Traductores e interpretadores - CI3715
#
# Manuel Gomes. Carnet: 11-10375
# Ricardo Vethencourt. Carnet: 09-10894
#
# Proyecto 1
# Programa que realiza un análisis lexicográfico de un archivo.
import sys
from lexNEO import *


#Generando el lexer
lexer = lex.lex()


lexer.input(content)

# Tokenizando
while (True):
	tok = lexer.token()
	if (not tok):
		break
	if (tok.type == 'TkIdent' or tok.type == 'TkNum' or\
	 tok.type == 'TkCaracter'):
		tokenlist.tokens.append(token(tok.type, tok.lineno,\
		 find_column(content, tok), tok.value))
	else:
		tokenlist.tokens.append(token(tok.type, tok.lineno,\
		 find_column(content, tok)))

tokenlist.printTokens()