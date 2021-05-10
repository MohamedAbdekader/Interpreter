Files:
Readme: documentation of the project
Main.py: a file that contains code to run the program
Scanner.py: a correct version of my previous scanner
Core.py: It contains the core variables needed for the scanner and parser
Assign.py: It contains code that assigns values to other values and expressions.
cmpr.py: Contain methods to parse, print and execute comparisions
cond.py: Contain methods to parse, print and execute conditions between variables
decl.py: Contain methods to parse, print and execute declaartion
declseq.py: Contain methods to parse, print and execute a single declaration. 
executor.py: Contains several methods that execute different files.
expr.py: Contain methods to parse, print and execute expressions
factor.py: Contain methods to parse, print and execute factors
formals.py: Contain methods to parse, print and execute formals
funccall.py: Contain methods to parse, print and execute function calling
funcdecl.py: Contain methods to parse, print and execute function declaration
id.py: Contain methods to parse, print and execute a single identifier.
idlist.py: Contain methods to parse, print and execute a list of ids.
if.py: Contain methods to parse, print and execute if statments
input.py: Contain methods to parse, print and execute inputting variables
output.py: Contain methods to parse, print and execute outputting variables
loop.py:Contain methods to parse, print and execute while loops
newdecl.py: Contain methods to parse, print and execute reference declarations
parser.py: contains code to parse several parts of the language
program.py: Contains parse program, printing program and executing program methods
stmtseq.py: Contains parse program, printing program and executing a list of statments 
term.py: Contains parse program, printing program and executing single terms

Description:
I created three different data structures. One list for references, one list for garbage collection, and one map that maps references with their values. 
When a new declaration is done, it adds it to the references list and maps a NULL value to it. When I assign a reference to a new value, I map the reference to the value and add the value to the garbage collector.
The garbage collector removes values as scopes are removed and values are not affiliated to references.

To run the program: 
python Main.py x.code x.data 
where x is a number from the correct test cases file.
