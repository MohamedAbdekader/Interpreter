Author: Mohamed Abdelkader

Files:
Main.py: a file that contains code to run the program
Parser.py: a file that contains the parser program 
Scanner.py: a correct version of my previous scanner
Core.py: It contains the core variables needed for the scanner and parser
Readme: documentation of the project

Special Features:
None

Description of Parser:
I created a class for each root node. The root node has a children nodes array. I have a parser for each root node that checks for the available children and does semantics checks. Then, for each class, I have a print method that prints each node and its children.

Test cases:
I added some test cases that I created myself which has the same format as the test cases given to us.I also found some bugs that I had such as not allowing this grammar: program begin <stmt-seq> end

Bugs:
I believe I don't have any.