from Core import Core
from Cond import Cond
import StmtSeq

class Loop:
	
	def parse(self, parser):
		parser.scanner.nextToken()
		self.cond = Cond()
		self.cond.parse(parser)
		parser.expectedToken(Core.BEGIN)
		parser.scanner.nextToken()
		self.ss = StmtSeq.StmtSeq()
		self.ss.parse(parser)
		parser.expectedToken(Core.ENDWHILE)
		parser.scanner.nextToken()
	
	def semantic(self, parser):
		self.cond.semantic(parser)
		parser.scopes.append([])
		self.ss.semantic(parser)
		parser.scopes.pop()
	
	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("while ", end='')
		self.cond.print()
		print(" begin\n", end='')
		self.ss.print(indent+1)
		for x in range(indent):
			print("  ", end='')
		print("endwhile\n", end='')

	def execute(self, executor):
		while self.cond.execute(executor):
			#Add a map for the new local scope, pop when done
			before = executor.before 
			executor.pushScope()
			self.ss.execute(executor)
			executor.popScope()
			while len(executor.gc) != before and len(executor.gc)!=0:
				executor.before = executor.before - 1
				executor.gc.pop()
				print("gc:"+str(len(executor.gc)))