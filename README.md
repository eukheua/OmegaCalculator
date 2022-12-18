# OmegaCalculator
Concluding task of python studies
Hi Potential user.
The git repository you are visiting right now contains files and modules for a calculator based on string input.
The modules and their importance are:

config: this module stores all the constant variables that are initialized at the start of the program run

operations: this module stores the arthimetic function and the Operator class that represents the mathematical possible actions.

parser: this module contains the functions responsible for parsing the expression from input string to a 
postfix calculatable list representing the meaning of the expression.

calculator: this module contains the function responsible for handling the process of calculation from parsing to calculating. 
it also contains the function resposible for evaluating a postfix expression and returning the answer.
this module catches arthimetic exceptions

utils: this module contain subfunction and assisting functions for the main functions in parser and calculator 
due to S.O.L.I.D requirements.

exceptions: this module contains the custom exception and errors classess for the calculator there are syntax exceptions 
and arthimetic ones.

validations: this module contains validation functions that are called before the parsing and calculating functions in order to 
avoid syntax errors from running in the first place.

input: main module and the one the input is handled from, contains the main loop and handles syntax and input exceptions.

colors: this module contains graphic additions to make messages clearer and ellegant.

these are all the modules and explanations about them.
enjoy your use of my project!!!
