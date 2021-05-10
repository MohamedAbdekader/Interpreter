Files:
Main.py: a file that contains code to run the program
Interpreter.py: a file that contains the parser program and execution program
Scanner.py: a correct version of my previous scanner
Core.py: It contains the core variables needed for the scanner and parser
Readme: documentation of the project

Description of Interpreter:
I created a class for each root node. The root node has a children nodes array. I have a parser for each root node that checks for the available children and does semantics checks. Then, for each class, I have a print method that prints each node and its children. For execution, I added an execution method in each class that executes the program. I have data structures that differentiate between local and global variables. I also added one more data structure that differentiate between variables with the same name. For example, in 7.code, there are two variables in different scopes; I change the name of the new variable to differentiate between them. In some classes, I added execute methods that specifically executes global variables and other for local variables.

To run the program: 
python Main.py x.code x.data 
where x is a number from the correct test cases file.
