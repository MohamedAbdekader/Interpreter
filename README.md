# Description
This is an interpreter for a pretend language called Core. The project was divided into 5 different parts. Each part added an additional feature 
to the interpreter. Until, eventually, I implmeneted a full interpreter for the Core language that includes a scanner, parser, interpreter, executor, 
and a garbage collector. 

# Grammar
The Core language grammar is shown below.

    <prog> ::= program <decl-seq> begin <stmt-seq> end | program begin <stmt-seq> end
    <decl-seq> ::= <decl> | <decl><decl-seq> | <func-decl> | <func-decl><decl-seq>
    <stmt-seq> ::= <stmt> | <stmt><stmt-seq>
    <decl> ::= int <id-list> ;
    <id-list> ::= id | id , <id-list>
    <func-decl> ::= id ( <formals> ) begin <stmt-seq> endfunc
    <formals> ::= id | id , <formals>
    <stmt> ::= <assign> | <if> | <loop> | <in> | <out> | <decl> | <func-call> | <new-decl>
    <new-decl> ::= define id;
    <func-call> ::= begin id ( <formals> ) ;
    <assign> ::= id = <expr> ; | id = new <expr> ; | id = define id ;
    <in> ::= input id ;
    <out> ::= output <expr> ;
    <if> ::= if <cond> then <stmt-seq> endif | if <cond> then <stmt-seq> else <stmt-seq> endif
    <loop> ::= while <cond> begin <stmt-seq> endwhile
    <cond> ::= <cmpr> | ! ( <cond> ) | <cmpr> or <cond>
    <cmpr> ::= <expr> == <expr> | <expr> < <expr> | <expr> <= <expr>
    <expr> ::= <term> | <term> + <expr> | <term> – <expr>
    <term> ::= <factor> | <factor> * <term>
    <factor> ::= id | const | ( <expr> )

# Project Parts
## First Part 
I implemented a Scanner class that takes as input a text file and outputs a stream of tokens from the CORE language.

## Second Part
I implemented a Parser that generates a parse tree for the input program, using the top-down recursive descent approach.

## Third Part
I implemented an Interpreter by using the recursive descent to walk over the parse tree built by your parser, and \execute" the Core program by 
performing the actions described.

## Fourth Part
I modified the Interpreter to now handle function definitions and function calls.

## Fifth Part
I modified the Interpreter to now handle references and garbage collection. 

# Input 
For the first two parts, you only need one input text file with that includes a Core program.
For the last three parts, you will need two input text files, one that includes a Core program, and another one that includes integers to be inputted 
if the program needs an innput.

# Test Cases
For each part, there are two folders, Correct and Error. The Correct folders contain input text files and what is expected to be outputted. The Error folders 
contain Core programs that are supposed to output errors to ensure that your error catching works.
