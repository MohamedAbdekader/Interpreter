Files:
Main.py: a file that contains code to run the program
Parser.py: a file that contains the parser program 
Scanner.py: a correct version of my previous scanner
Core.py: It contains the core variables needed for the scanner and parser
Readme: documentation of the project

Description of Parser:
I created a class for each root node. The root node has a children nodes array. I have a parser for each root node that checks for the available children and does semantics checks. Then, for each class, I have a print method that prints each node and its children.

To run the program: 
python Main.py x.code
where x is a number from the correct test cases file.
