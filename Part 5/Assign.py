from Id import Id
from IdList import IdList
from Expr import Expr
from Core import Core
from NewDecl import NewDecl
from Executor import Executor

class Assign:
	
	def parse(self, parser):
		self.identifier = parser.scanner.getID()
		self.id = Id()
		self.id.parse(parser)
		parser.expectedToken(Core.ASSIGN)
		parser.scanner.nextToken()
		if(parser.scanner.currentToken() == Core.NEW):
			parser.scanner.nextToken()
			self.var = parser.scanner.getID() 
			self.exprGC = Expr()
			self.exprGC.parse(parser)
			parser.expectedToken(Core.SEMICOLON)
			parser.scanner.nextToken()
		elif(parser.scanner.currentToken() == Core.DEFINE):
			parser.scanner.nextToken()
			parser.expectedToken(Core.ID)
			self.var = parser.scanner.getID()
			self.name = Id()
			self.name.parse(parser)
			parser.expectedToken(Core.SEMICOLON)
			parser.scanner.nextToken()
		else:
			self.expr = Expr()
			self.expr.parse(parser)
			parser.expectedToken(Core.SEMICOLON)
			parser.scanner.nextToken()

	def semantic(self, parser):
		self.id.semantic(parser)
		if hasattr(self, 'expr'):
			self.expr.semantic(parser)
		elif hasattr(self,'name'):
			self.name.semantic(parser)
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		self.id.print()
		print("=", end='')
		#self.expr.print()
		print(";\n", end='')


	def execute(self, executor):
		if hasattr(self, 'expr'):
			self.id.executeAssign(executor, self.expr.execute(executor))
		elif hasattr(self, 'exprGC'):
			executor.map[self.identifier] = self.var
			executor.gc.append(self.var)
			print("gc:"+str(len(executor.gc)))
			self.id.executeAssign(executor, self.exprGC.execute(executor))
		else:
			self.name.executeAllocate(executor)
			if executor.map[self.var] is not None:
				executor.map[self.identifier] = executor.map[self.var]
				self.id.executeAssign(executor,executor.map[self.var])

