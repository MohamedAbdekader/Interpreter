#Author:Mohamed Abdelkader
from Scanner import Scanner
from Core import Core
from Interpreter import Parser
import sys
def main():
  # Initialize the scanner with the input file and data with data file
  scanner = sys.argv[1]
  data = sys.argv[2]
  #Parse and execute project
  p = Parser(scanner, data)
  p.parse()
  p.semantic()
  p.execute()
    
if __name__ == "__main__":
    main()