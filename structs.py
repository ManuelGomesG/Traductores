


class BinaryOp (Expr):
	def __init__(self,left,right,op,opV,typ):
		self.left=left
		self.right=right
		self.op=op
		self.opV=opV
		self.type=typ


	def getValues(self):
		pass

class UnaryOp(Expr):
	def __init__(self,op,opV,term,typ):
		self.op=op
		self.opV=opV
		self.term=typ
		self.typ=typ

	def getValue():
		pass

class Number(Expr):
	def __init__(self,value):
		self.value=value
		self.type="Número"

class Bool(Expr):
	def __init__(self,value):
		self.value=value
		self.type="Booleano"

class Ident(Expr):
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


