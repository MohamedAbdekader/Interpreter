from Core import Core
from Cond import Cond
import StmtSeq

class If:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.cond = Cond()
		self.cond.parse(parser)
		parser.expectedToken(Core.THEN)
		parser.scanner.nextToken()
		self.ss1 = StmtSeq.StmtSeq()
		self.ss1.parse(parser)
		if parser.scanner.currentToken() == Core.ELSE:
			parser.scanner.nextToken()
			self.ss2 = StmtSeq.StmtSeq()
			self.ss2.parse(parser)
		parser.expectedToken(Core.ENDIF)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.cond.semantic(parser)
		parser.scopes.append([])
		self.ss1.semantic(parser)
		parser.scopes.pop()
		if hasattr(self, 'ss2'):
			parser.scopes.append([])
			self.ss2.semantic(parser)
			parser.scopes.pop()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("if ", end='')
		self.cond.print()
		print(" then\n", end='')
		self.ss1.print(indent+1)
		if hasattr(self, 'ss2'):
			for x in range(indent):
				print("  ", end='')
			print("else\n", end='')
			self.ss2.print(indent+1)
		for x in range(indent):
			print("  ", end='')
		print("endif\n", end='')

	def execute(self, executor):
		if self.cond.execute(executor):
			#Add a map for the new local scope, pop when done
			before = executor.before 
			executor.pushScope()
			self.ss1.execute(executor)
			executor.popScope()
			while len(executor.gc) != before and len(executor.gc)!=0:
				executor.before = executor.before - 1
				executor.gc.pop()
				print("gc:"+str(len(executor.gc)))
		elif hasattr(self, 'ss2'):
			#Add a map for the new local scope, pop when done
			before = executor.before 
			executor.pushScope()
			self.ss2.execute(executor)
			executor.popScope()
			while len(executor.gc) != before and len(executor.gc)!=0:
				executor.before = executor.before - 1
				executor.gc.pop()
				print("gc:"+str(len(executor.gc)))