#Author:Mohamed Abdelkader
from Core import Core
from Scanner import Scanner

#It will save variables to check if there are duplicates or if they arent assigned yet
IDS = []
#Class for the program root node
class program:
  # Initialize the program root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "Program"
    self.indentation = 0
    self.decl = False
    self.children = []
  
  # Method to parse the program node
  def parseProgram(self,scanner):
    # Check if current token is PROGRAM
    if(scanner.currentToken()!=Core.PROGRAM):
      print("ERROR: 'program' was not found at the beginning of program")
      exit()
    
    #Add Program to nodes and get next token 
    self.children.append("Program")
    scanner.nextToken()

    # Parse decl-seq and add it to children if it's there
    if(scanner.currentToken()== Core.INT): 
      self.decl = True
      decl_seq = declSeq()
      self.children.append(decl_seq)
      decl_seq.parseDeclSeq(scanner)

    # Check if current token is BEGIN
    if(scanner.currentToken()!= Core.BEGIN):
      print("ERROR: 'begin' was not found at the beginning of program")
      exit()

    #Add Begin to nodes and get next token 
    self.children.append("Begin")
    scanner.nextToken()

    # Parse stmt-seq and add it to children 
    stmt_seq = stmtSeq()
    self.children.append(stmt_seq)
    stmt_seq.parseStmtSeq(scanner)

    # Check if current token is END
    if(scanner.currentToken()!=Core.END):
      print("ERROR: 'end' was not found at the end of program")
      exit()
    
    #Add End to children
    self.children.append("End")

  # Method to print the program tree 
  def printProgram(self):
  #Print program and add indentation to next line
    print("program")
    self.indentation += 1
    #if there is decl-seq
    if(self.decl==True):
    #Print decl-seq
      self.children[1].printDeclSeq(self.indentation)
    #print begin
      print("begin")
    #print stmt-seq
      self.children[3].printStmtSeq(self.indentation)
    #print end
      print("end")
    else:
    #print begin
      print("begin")
  #print stmt-seq
      self.children[2].printStmtSeq(self.indentation)
  #print end
      print("end")

#Class for the decl-seq root node
class declSeq():
  # Initialize the decl-seq root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "decl-seq"
    self.children = []

  # Method to parse the decl-seq node
  def parseDeclSeq(self,scanner):
    #Add the decl node to children if it exists
    decl = declNode()
    self.children.append(decl)
    decl.parseDecl(scanner)
    
    #Check if there is a semicolon at the end of declaration 
    if(decl.children[2] != ";"):
      print("ERROR: Expected ';'")
      exit()
    #If current token is begin, return to program node
    if(scanner.currentToken() == Core.BEGIN): return

    #Check if current token is another int declaration
    if(scanner.currentToken() == Core.INT):
    #Add the decl node to children 
      decl_seq = declSeq()
      self.children.append(decl_seq)
      decl_seq.parseDeclSeq(scanner)

# Method to print the decl-seq tree  
  def printDeclSeq(self,indentation):
    self.children[0].printDecl(indentation)
    if(len(self.children)>1):self.children[1].printDeclSeq(indentation)

#Class for the decl root node
class declNode():
  # Initialize the decl root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "decl"
    self.children = []
  # Method to parse the decl node
  def parseDecl(self,scanner):
    #Check if current token is int
    if(scanner.currentToken() != Core.INT):
        print("ERROR: 'int' was not found ")
        exit()

    #Add int to children and get next token
    self.children.append("int")
    scanner.nextToken()

    #Add the idlist node to children if it exists
    id_list = IDList()
    self.children.append(id_list)
    id_list.parseIdList(scanner)

    #Check if semicolon is at the end and add it to children
    if(scanner.currentToken() != Core.SEMICOLON):
        print("ERROR: Expected ';' ")
        exit()
    self.children.append(";")
    scanner.nextToken()

  #Method to print the decl node
  def printDecl(self,indentation):
    for c in range(0,indentation):
      print("\t",end = '')
    print("int ",end = '')
    self.children[1].printIdList()
    print(";")

#Class for the id-list root node
class IDList():
  # Initialize the id-list root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "id-list"
    self.children = []
  # Method to parse the id-list node
  def parseIdList(self, scanner):
    #Check if current token is ID and add it to children
    if(scanner.currentToken()!=Core.ID):
      print("ERROR: variable name is not an id")
      exit()
    self.children.append(scanner.getID())
    scanner.nextToken()

    #Check if current token is comma. If yes, get another id-list
    if(scanner.currentToken() == Core.COMMA):
      self.children.append(",")
      scanner.nextToken()
      id_list = IDList()
      self.children.append(id_list)
      id_list.parseIdList(scanner)

    #Check if id is doubly declared
    if(self.children[0] in IDS):
      print("ERROR: Doubly declared variable!")
      exit()
    
    IDS.append(self.children[0])
  #Method that prints the id-list node 
  def printIdList(self):
    print(self.children[0],end = '')
    if(len(self.children)>1): 
      print(",",end = '')
      self.children[2].printIdList()
    

#Class for the stmt-seq root node
class stmtSeq():
  # Initialize the stmt-seq root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "stmt-seq"
    self.children = []
  # Method to parse the stmt-seq node
  def parseStmtSeq(self,scanner):
  #Add the stmt node to children if it exists
    stmt = stmtNode()
    self.children.append(stmt)
    stmt.parseStmt(scanner)
    #Return to program node if it reaches END
    if(scanner.currentToken() == Core.END): return
    #Check if current token is a continuation of the stmt-seq and add them to children
    if(scanner.currentToken() in [Core.ID, Core.IF, Core.WHILE, Core.OUTPUT, Core.INPUT, Core.INT]):   
      stmt_seq = stmtSeq()
      self.children.append(stmt_seq)
      stmt_seq.parseStmtSeq(scanner)
  #Program to print stmt-seq node  
  def printStmtSeq(self,indentation):
    self.children[0].printStmt(indentation)
    if(len(self.children)>1):self.children[1].printStmtSeq(indentation)

#Class for the stmt root node
class stmtNode():
  # Initialize the stmt root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "stmt"
    self.children = []
  # Method to parse the stmt node
  def parseStmt(self,scanner):
    #Check if current node is an ID and add it to children
    if(scanner.currentToken() == Core.ID):
      assign = assignNode()
      self.children.append(assign)
      assign.parseAssign(scanner)
    #Check if current node is if and add it to children
    elif scanner.currentToken() == Core.IF:
      IF = IFNode()
      self.children.append(IF)
      IF.parseIf(scanner)
    #Check if current node is a while loop and add it to children
    elif scanner.currentToken() == Core.WHILE:
      loop = loopNode()
      self.children.append(loop)
      loop.parseLoop(scanner)
      #Check if current node is an input and add it to children
    elif scanner.currentToken() == Core.INPUT:
      inputIns = inputNode()
      self.children.append(inputIns)
      inputIns.parseInput(scanner)
      #Check if current node is an output and add it to children
    elif scanner.currentToken() == Core.OUTPUT:
      outputIns = outputNode()
      self.children.append(outputIns)
      outputIns.parseOutput(scanner)
    #Check if current node is an int declaration and add it to children
    elif scanner.currentToken() == Core.INT:
      decl = declNode()
      self.children.append(decl)
      decl.parseDecl(scanner)

  # Method to print the stmt node 
  def printStmt(self,indentation):
    if self.children[0].txt == "assign":self.children[0].printAssign(indentation)
    if self.children[0].txt == "input":self.children[0].printInput(indentation)
    if self.children[0].txt == "output":self.children[0].printOutput(indentation)
    if self.children[0].txt == "loop":self.children[0].printLoop(indentation)
    if self.children[0].txt == "if":self.children[0].printIf(indentation)
    if self.children[0].txt == "decl":self.children[0].printDecl(indentation)

#Class for the assign root node
class assignNode():
    # Initialize the assign root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "assign"
    self.children = []
  #Method to parse the assign rote node
  def parseAssign(self,scanner):
  #Check if current token is an id and add it to children
    if scanner.currentToken() != Core.ID:
      print("ERROR: An id was not found in an assign statment")
      exit()
    self.children.append(scanner.getID())
    scanner.nextToken()
  #Check if current token is an '=' and add it to children
    if scanner.currentToken() != Core.ASSIGN:
      print("ERROR: Expected '=' in an assign statment")
      exit()
    self.children.append("=")
    scanner.nextToken()
  #Add expr Node to children if it exists
    expr = exprNode()
    self.children.append(expr)
    expr.parseExpr(scanner)
  #Check if there is a semicolon and add it to children
    if scanner.currentToken() != Core.SEMICOLON:
      print("ERROR: Missing ';' at the end of an assign stmt")
      exit()
    self.children.append(";")
    scanner.nextToken()

  #Method to print assign node
  def printAssign(self,indentation):
    for c in range(0,indentation):
      print("\t",end = '')
    print(self.children[0]+"=", end = '')
    self.children[2].printExpr()
    print(";")

#Class for the expr root node
class exprNode():
  # Initialize the expr root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "expr"
    self.children = []
  #Method to parse the expr rote node
  def parseExpr(self, scanner):
    #Add term node to children if it exists
    term = termNode()
    self.children.append(term)
    term.parseTerm(scanner)
    #Check if current token is an add sign and add it to children
    if(scanner.currentToken() == Core.ADD):
      self.children.append("+")
      scanner.nextToken()
      expr = exprNode()
      self.children.append(expr)
      expr.parseExpr(scanner)
    #Check if current token is a subtract sign and add it to children
    elif scanner.currentToken() == Core.SUB:
      self.children.append("-")
      scanner.nextToken()
      expr = exprNode()
      self.children.append(expr)
      expr.parseExpr(scanner)

# Method to print the expr node
  def printExpr(self):
    self.children[0].printTerm()
    if("+" in self.children): 
      print("+",end = '')
      self.children[2].printExpr() 
    if("-" in self.children):
      print("-", end = '')
      self.children[2].printExpr()

#Class for the term root node
class termNode():
  # Initialize the term root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "term"
    self.children = []
  #Method to parse the term rote node
  def parseTerm(self,scanner):
  #Add factor node to children if it exists
    factor = factorNode()
    self.children.append(factor)
    factor.parseFactor(scanner)
    #Check if current token is multiply and add it and the term to children
    if(scanner.currentToken() == Core.MULT):
      self.children.append("*")
      scanner.nextToken()
      term = termNode()
      self.children.append(term)
      term.parseTerm(scanner)
  #Method to print the term node  
  def printTerm(self):
    self.children[0].printFactor()

    if "*" in self.children:
      print("*",end = '')
      self.children[2].printTerm()

#Class for the factor root node
class factorNode():
  # Initialize the factor root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "factor"
    self.children = []
  #Method to parse the factor node
  def parseFactor(self,scanner):
  #Check if current token is an id and it to children
    if scanner.currentToken() == Core.ID:
      var = scanner.getID()
      self.children.append(var)
      self.txt = "ID"
      scanner.nextToken()

      #Check if variable is assigned
      if(var not in IDS):
        print("Error: Undeclared variable detected!")
        exit()
    #Check if current token is a constant and it to children
    elif scanner.currentToken() == Core.CONST:
      self.children.append(scanner.getCONST())
      self.txt = "CONST"
      scanner.nextToken()
    #Check if current token is a '(' and it to children
    elif scanner.currentToken() == Core.LPAREN:
      self.txt = "PAREN"
      self.children.append("(")
      scanner.nextToken()
    #Add expr node to children 
      expr = exprNode()
      self.children.append(expr)
      expr.parseExpr(scanner)
    #Check if ')' is current token and add it to children
      if scanner.currentToken() != Core.RPAREN:
        print("ERROR: Expected ')'")
        exit()
          
      self.children.append(")")
      scanner.nextToken()
    # invalid character if not one of the previous 
    else:
      print("ERROR: Invalid Character detected!")
      exit()

  #Method to print the factor node
  def printFactor(self):
    if self.txt == "ID":
      print(self.children[0],end = '')
    elif self.txt == "CONST":
      print(str(self.children[0]), end = '')
    else:
      print("(",end = '')
      self.children[1].printExpr()
      print(")",end = '')

#Class for the if root node
class IFNode():
    # Initialize the if root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "if"
    self.children = []
  #Method to parse if node
  def parseIf(self,scanner):
    #Check if current token is if and add it to children
    if(scanner.currentToken() != Core.IF):
      print("ERROR: Expected 'if' ")
      exit()
    self.children.append("if")
    scanner.nextToken()
    #Add cond node to children
    cond = condNode()
    self.children.append(cond)
    cond.parseCond(scanner)
    #Check if current token is then and add it to children
    if(scanner.currentToken() != Core.THEN):
      print("ERROR: Expected 'then' ")
      exit()
    self.children.append("then")
    scanner.nextToken()

    #Add stmt-seq node
    stmt_seq = stmtSeq()
    self.children.append(stmt_seq)
    stmt_seq.parseStmtSeq(scanner)
    #Check if current token is endif and add it to children
    if(scanner.currentToken() == Core.ENDIF):
      self.children.append("endif")
      scanner.nextToken()
    #Check if current token is else and add it to children along with the stmt-seq
    elif scanner.currentToken() == Core.ELSE:
      self.children.append("else")
      scanner.nextToken()
      elseStmt_seq = stmtSeq()
      self.children.append(elseStmt_seq)
      elseStmt_seq.parseStmtSeq(scanner)
      #Check if current token is endif and add it to children
      if(scanner.currentToken() != Core.ENDIF):
        print("ERROR: Expected endif")
        exit()
      self.children.append("endif")
      scanner.nextToken()
  #If endif is not found
    else:
      print("ERROR: Expected 'endif'")
      exit()

#Method to print the if node
  def printIf(self,indentation):
    for c in range(0,indentation):
      print("\t", end = '')
    print("if ",end = '')
    self.children[1].printCond()
    print(" then")
    self.children[3].printStmtSeq(indentation+1)

    if("else" in self.children):
      for c in range(0,indentation):
        print("\t", end = '')
      print("else")
        
      self.children[5].printStmtSeq(indentation+1)
      for c in range(0,indentation):
        print("\t", end = '')
      print("endif")
    else:
      for c in range(0,indentation):
        print("\t", end = '')
      print("endif")

#Class for the cond root node
class condNode():
  # Initialize the if root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "cond"
    self.children = []
  #Method to parse the cond node
  def parseCond(self,scanner):
    #Check if current token is not negation 
    if scanner.currentToken() != Core.NEGATION:
    #Add cmpr node
      cmpr = cmprNode()
      self.children.append(cmpr)
      cmpr.parseCmpr(scanner)
      #If current token is or, add a second cond
      if scanner.currentToken() == Core.OR:
        self.children.append("or")
        scanner.nextToken()
        cond2 = condNode()
        self.children.append(cond2)
        cond2.parseCond(scanner)
    #If negation, aff it to children and get other characters
    else:
      self.children.append("!")
      scanner.nextToken()
      if(scanner.currentToken()!= Core.LPAREN):
        print("ERROR: Expected '(' after '!'")
        exit()
      self.children.append("(")
      scanner.nextToken()
      cond = condNode()
      self.children.append(cond)
      cond.parseCond(scanner)
      #Check if next character is )
      if(scanner.currentToken()!= Core.RPAREN):
        print("ERROR: Expected ')'")
        exit()
      self.children.append(")")
      scanner.nextToken()
  #Method to print cond node 
  def printCond(self):
    if self.children[0]!= "!":
      self.children[0].printCmpr()
      if "or" in self.children:
        print("or",end = '')
        self.children[3].printCmpr()
    else:
      print("!(",end='')
      self.children[2].printCond()
      print(")",end = '')

#Class for the cmpr root node
class cmprNode():
  # Initialize the cmpr root node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "cmpr"
    self.children = []

  #Method to parse the cmpr node
  def parseCmpr(self,scanner):
    #Add expr node to cchildren node
    expr = exprNode()
    self.children.append(expr)
    expr.parseExpr(scanner)
    #Check if current token is an equal token and add it to children
    if scanner.currentToken() == Core.EQUAL:
      self.children.append("==")
      scanner.nextToken()
      #Add second expression to children
      expr2 = exprNode()
      self.children.append(expr2)
      expr2.parseExpr(scanner)
    #Check if current is a less token and add it to children
    elif scanner.currentToken() == Core.LESS:
      self.children.append("<")
      scanner.nextToken()
      #Add second expression to children
      expr2 = exprNode()
      self.children.append(expr2)
      expr2.parseExpr(scanner)
    
    #Check if current is a lessequal token and add it to children
    elif scanner.currentToken() == Core.LESSEQUAL:
      self.children.append("<=")
      scanner.nextToken()
      #Add second expression to children
      expr2 = exprNode()
      self.children.append(expr2)
      expr2.parseExpr(scanner)

    #If not one of previous 
    else:
      print("ERROR: Terminal symbol placement is not permitted")
      exit()

#Method to print the cmpr node
  def printCmpr(self):
    self.children[0].printExpr()
    if "==" in self.children:
        print("==",end = '')
    elif "<=" in self.children:
        print("<=",end = '')
    else:
        print("<",end = '')
    self.children[2].printExpr()

#Class for the input root node
class inputNode():
  # Initialize the input input node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "input"
    self.children = []
  #Method to parse the input node
  def parseInput(self,scanner):
    #Check if current token is input token and add it to children
    if scanner.currentToken() != Core.INPUT:
      print("ERROR: Expected 'input' ")
      exit()
    self.children.append("input")
    scanner.nextToken() 

    #Check if current token is an id token and add it to children
    if scanner.currentToken() != Core.ID:
      print("ERROR: Invalid id behind 'input'")
      exit()
    self.children.append(scanner.getID())
    scanner.nextToken()
        
    #Check if current token is a ; token and add it to children
    if scanner.currentToken() != Core.SEMICOLON:
      print("ERROR: Expected ';' ")
      exit()
    self.children.append(";")
    scanner.nextToken() 

  #Method to print the input node
  def printInput(self,indentation):
    for c in range(0,indentation):
      print("\t", end = '')
    print("input "+self.children[1]+";")

#Class for the output root node
class outputNode():
  # Initialize the output  node with name and an array to store the children nodes
  def __init__(self):
    self.txt = "output"
    self.children = []

  #Method to parse output method 
  def parseOutput(self,scanner):
    #Check if current token is output and add to children 
    if scanner.currentToken() != Core.OUTPUT:
      print("ERROR: Expected 'output'")
      exit()
    self.children.append("output")
    scanner.nextToken() 
    #add expr node
    expr = exprNode()
    self.children.append(expr)
    expr.parseExpr(scanner)

    #Check if current token is semicolon and add to children 
    if scanner.currentToken() != Core.SEMICOLON:
      print("ERROR: Expected ';' ")
      exit()
    self.children.append(";")
    scanner.nextToken() 

  #Method to print the output node
  def printOutput(self,indentation):
    for c in range(0,indentation):
      print("\t",end = '')
    print("output ", end = '')
    self.children[1].printExpr()
    print(";")

#Class for the loop root node
class loopNode():
  # Initialize the loop node with name and an array to store the children nodes
  def __init__(self):
      self.txt = "loop"
      self.children = []

  #method to parse loop node
  def parseLoop(self,scanner):
    #Check if current token is output and add to children 
    if(scanner.currentToken() != Core.WHILE):
      print("ERROR: Expected 'while'")
      exit() 
    self.children.append("while")
    scanner.nextToken()

    #Add cond node to children
    cond = condNode()
    self.children.append(cond)
    cond.parseCond(scanner)

    #Check if current token is begin and it to children
    if(scanner.currentToken() != Core.BEGIN):
      print("ERROR: Expected 'begin' after while and conitional")
      exit()
    self.children.append("begin")
    scanner.nextToken()
  #Add stmt-seq to children
    stmt_seq = stmtSeq()
    self.children.append(stmt_seq)
    stmt_seq.parseStmtSeq(scanner)
    #Check if it has endwhile and add it to children

    if(scanner.currentToken() != Core.ENDWHILE):
      print("ERROR: Expected 'endwhile'")
      exit() 

    self.children.append("endwhile")
    scanner.nextToken()

#Method to print loop node
  def printLoop(self,indentation):
      for c in range(0,indentation):
        print("\t", end = '')
      print("while ",end = '')
      self.children[1].printCond()
      print(" begin")
      self.children[3].printStmtSeq(indentation+1)
      for c in range(0,indentation):
        print("\t", end = '')
      print("endwhile")