#Author: Mohamed Abdelkader
from Core import Core

class Scanner:
  # Constructor should open the file and find the first token
  def __init__(self, filename):
    #Create a dictionary of the keywords and specials in the Core file 
    self.keywords = {
      "program":Core.PROGRAM,
      "begin": Core.BEGIN,
      "end": Core.END,
      "new": Core.NEW,
      "define": Core.DEFINE,
      "int": Core.INT,
      "endfunc": Core.ENDFUNC,
      "if": Core.IF,
      "then": Core.THEN,
      "else": Core.ELSE,
      "while": Core.WHILE,
      "endwhile": Core.ENDWHILE,
      "endif": Core.ENDIF,
      ";": Core.SEMICOLON,
      "(": Core.LPAREN, 
      ")": Core.RPAREN,
      ",": Core.COMMA,
      "=": Core.ASSIGN,
      "!": Core.NEGATION,
      "or": Core.OR,
      "==": Core.EQUAL,
      "<": Core.LESS,
      "<=": Core.LESSEQUAL,
      "+": Core.ADD,
      "-": Core.SUB,
      "*": Core.MULT,
      "input": Core.INPUT,
      "output": Core.OUTPUT  
    }
    #Open the file
    self.file = open(filename, 'r')
    self.currentStr = ""
    self.token = ""
    #Counter that helps the getToken() function undersrand whether 
    # the "" is the end of file or an error 
    self.counter = 0
    self.currentChar = self.file.read(1)
    #Get the first token
    self.getToken()
    #Update counter to show file is not empty
    self.counter = self.counter + 1

  # nextToken should advance the scanner to the next token
  def nextToken(self):
    self.currentStr = ""
    self.getToken()
     
  # currentToken should return the current token
  def currentToken(self):
    return self.token

  # If the current token is ID, return the string value of the identifier
	# Otherwise, return value does not matter
  def getID(self):
    return str(self.currentStr)

  # If the current token is CONST, return the numerical value of the constant
	# Otherwise, return value does not matter
  def getCONST(self):
    return int(self.currentStr)
  
  #Get the token c haracter by character from the input file and categorize
  #the tokens according to their types
  def getToken(self):
    # while character is space, get next character 
    while str.isspace(self.currentChar):
      self.currentChar = self.file.read(1)
    
    # If character is empty, check if file is empty or it's the end of file
    if self.currentChar == "":
      if self.counter > 0:
        self.token = Core.EOF
        self.file.close()
      else: 
        self.token = Core.ERROR
        self.file.close()
        print("ERROR: File is Empty!")

    # Categorize character if it's not empty
    else:
      # Check if the character is a sign in the dictionary of keywords
      if self.currentChar in self.keywords.keys():
        self.currentStr += self.currentChar
        #If the current character is a "less than" sign, check if it's LESSEQUAL or LESS
        if self.currentChar == "<":
          nextChar = self.file.read(1)
          #If next character is "=", it's LESSEQUAL; if not, it's LESS
          if nextChar == "=":
            self.token = Core.LESSEQUAL
            self.currentStr += nextChar
            self.currentChar = nextChar
            self.currentChar = self.file.read(1)
          else:
            self.token = Core.LESS
            self.currentChar = nextChar
        #If the current character is an "equal" sign, check if it's ASSIGN or EQUAL
        elif self.currentChar == "=":
          nextChar = self.file.read(1)
          #If next character is "=", it's EQUAL; if not, it's ASSIGN
          if nextChar == "=":
            self.token = Core.EQUAL
            self.currentStr += nextChar
            self.currentChar = nextChar
            self.currentChar = self.file.read(1)
          else:
            self.token = Core.ASSIGN
            self.currentChar = nextChar
        # If it's not an "equal" or "less than" sign, find its meaning in the dictionary 
        else:
          self.token = self.keywords[self.currentChar]
          self.currentChar = self.file.read(1)
        
       # Check if the character is an alphabet
      elif str.isalpha(self.currentChar):
        self.currentStr += self.currentChar
        self.currentChar = self.file.read(1)
        # Continue taking words to create a word 
        while (str.isalpha(self.currentChar) or str.isnumeric(self.currentChar)):
          self.currentStr += self.currentChar
          self.currentChar = self.file.read(1)

        # Check if the word is a keyword in the dictionary or a word
        if self.currentStr in self.keywords.keys():
          self.token = self.keywords[self.currentStr]
        else:
          self.token = Core.ID

      # Check if the chacarter is a number
      elif str.isnumeric(self.currentChar):
        self.currentStr += self.currentChar
        self.currentChar = self.file.read(1)
        # Continue reading the characters until the full constant is read
        while(str.isnumeric(self.currentChar)):
          self.currentStr += self.currentChar
          self.currentChar = self.file.read(1)
        
        # Check if the number is a valid constant; if not, send an error message and token
        if(int(self.currentStr) in range(0,1024)):
          self.token = Core.CONST
        else:
          self.token = Core.ERROR
          self.file.close()
          print("ERROR: Constant Out of Range!")
      
      # If it's not any of the previous cases, it is an invalid character
      # Print an error message and send an error token
      else:
        self.token = Core.ERROR
        self.file.close()
        print("ERROR: Invalid Character Detected!")