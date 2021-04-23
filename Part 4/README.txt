Author: Mohamed Abdelkader

Files:
Main.py: a file that contains code to run the program
Interpreter.py: a file that contains the parser program and execution program
Scanner.py: a correct version of my previous scanner
Core.py: It contains the core variables needed for the scanner and parser
Readme: documentation of the project

Special Features:
None

Description of Interpreter:
I created a class for each root node. The root node has a children nodes array. I have a parser for each root node that checks for the available children and does semantics checks. Then, for each class, I have a print method that prints each node and its children. For execution, I added an execution method in each class that executes the program. I have data structures that differentiate between local and global variables. I also added one more data structure that differentiate between variables with the same name. In the formals class, I check for formal and actual parameters and check the semantics. In the func call class, I map the formal parameters to the actual parameters and I map back to the main function to set values to each other. I also check which function is being called using a data structure that differentiates between scopes and func names. In func decl class, I check if function is already declared and adds it to a data structure if it's a new one.

Test cases:
I added some test cases that I created myself which has the same format as the test cases given to us. I also added some test cases that I found on Piazza. I found a bug where I did not check if number of parameters in the function call were the same as the number of parameters in the function declaration, but I fixed it.


Bugs:
I believe I don't have any.