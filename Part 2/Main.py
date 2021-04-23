#Author:Mohamed Abdelkader
from Scanner import Scanner
from Core import Core
from Parser import program
import sys

def main():
  # Initialize the scanner with the input file
  S = Scanner(sys.argv[1])

  #Check if file is empty
  if(S.currentToken()==Core.EOF):
    print ("ERROR: File is empty!")
    exit()
    
  # generate parse tree according to the scanner
  root = program()
  root.parseProgram(S)
  S.nextToken()

  #Check end of file
  if(S.currentToken()!=Core.EOF):
    print ("ERROR: Characters detected after EOF!")
    exit()

  #Print program from parse tree
  root.printProgram()
    
if __name__ == "__main__":
    main()