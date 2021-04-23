from Id import Id
from IdList import IdList
from Core import Core
import sys


class NewDecl:
	
	def parse(self, parser):
		parser.expectedToken(Core.DEFINE)
		parser.scanner.nextToken()
		parser.expectedToken(Core.ID)
		self.var = parser.scanner.getID()
		self.id = Id()
		self.id.parse(parser)
		parser.expectedToken(Core.SEMICOLON)
		parser.scanner.nextToken()

	def semantic(self, parser):
		self.id.doublyDeclared(parser)
		self.id.addToScope(parser)

	def print(self, indent):
		for x in range(indent):
			print("  ", end='')
		print("define ", end='')
		self.id.print()
		print(";\n", end='')

	def execute(self, executor):
		self.id.executeAllocate(executor) 
		executor.refs.append(self.var)
		executor.map[self.var]=None