#!/usr/bin/python3
# Universidad Simon Bolívar 
#
# Traductores e interpretadores - CI3715
#
# Manuel Gomes. Carnet: 11-10375
# Ricardo Vethencourt. Carnet: 09-10894
#
# Proyecto 1
# Definición de clases utilizadas en el programa.

import sys


# Clase token

class token:

	def __init__(self, name=None, row=None, column=None, val=None):
		"""Clase que define un token
			Argumentos:
			name:	Nombre del token. (None por defecto)
			row:	Fila donde se encuentra.(None por defecto)
			column:	Posición en la fila. (None por defecto)
			arg:	Argumento del token. (None por defecto)
		"""	

		self.name=name
		self.row=row
		self.column=column
		self.val=val


# Lista que contendrá tokens y errores.
class tkList:
	"""Lista de tokens"""
	def __init__(self, tokens=[], errors=[]):
		"""
		Definición e inicialización de la lista de tokens
		Argumentos:
			tokens:		Lista de tokens "correctos" ([] por defecto).
			errors:		lista de errores ([] por defecto).
		"""
		self.tokens = tokens
		self.errors = errors


	def addToken(self,token):
		"""Agrega un token correcto al final de la lista de tokens"""
		self.tokens.append(token)
		

	def adddError(self,error):
		"""Agrega un error a la lista de errores"""
		self.errors.append(error)


	def printTokens(self):
		"""Función para imprimir los tokens en pantalla"""
		for token in self.tokens:
			if token.val==None:
				print("Token: "+token.name+ ", fila: "+ str(token.row) + \
					", columna: " + str(token.column))

			else:
				print("Token: "+token.name+ " , valor: ("+str(token.val )+\
					"), fila: "+ str(token.row) + ", columna: " + \
					str(token.column))

	def printError(self):
		"""Imprime en pantalla el contenido de la lista de errores"""
		for err in self.errors:
			print(err + '\n')

		




		