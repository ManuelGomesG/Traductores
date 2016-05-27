#!/usr/bin/python3
# Universidad Simon Bolívar 
#
# Traductores e interpretadores - CI3715
#
# Manuel Gomes. Carnet: 11-10375
# Ricardo Vethencourt. Carnet: 09-10894
#
# Proyecto 1
# Estructuras para el arbol sintáctico.



class BinaryOp():

	def __init__(self,left,right,op,opV,typ):
		self.left=left
		self.right=right
		self.op=op
		self.opV=opV
		self.type=typ

	def getValues(self):
		pass

class UnaryOp():
	def __init__(self,op,opV,term,typ):
		self.op=op
		self.opV=opV
		self.term=typ
		self.typ=typ

	def getValue():
		pass

class Number():
	def __init__(self,value):
		self.value=value
		self.type="Número"

class Bool():
	def __init__(self,value):
		self.value=value
		self.type="Booleano"

class Ident():
	def __init__(self,value):
		self.value=value
		self.type="Identificador"

class InstrTree():
	def __init__(self,token=None,child=None,instr=None):
		self.token=token
		if child:
			self.child=child
		else:
			self.child=[]
		self.instr=instr

	def addChildren(self,children):
		self.child=child

	def addToken(self,token):
		self.token=token

	def addInstr(self,instr):
		self.instr=instr


