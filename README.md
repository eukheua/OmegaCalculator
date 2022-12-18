# OmegaCalculator
Concluding task of python studies - chose to implement it with system 1 (אסכולה 1)

Hi Potential user.
The git repository you are visiting right now contains files and modules for a calculator based on command line input.
The modules and their importance are:

**config**: this module stores all the constant variables that are initialized at the start of the program run.

**colors**: this module contains graphic additions to make messages clearer and ellegant.

**operations**: this module stores the arthimetic functions and the Operator class that represents the mathematical supported actions.

**parser**: this module contains the functions responsible for parsing the expression from input string to a 
postfix calculatable list representing the meaning of the expression.

**calculator**: this module contains the function responsible for handling the process of calculation from parsing to calculating. 
it also contains the function resposible for evaluating a postfix expression and returning the answer.
this module catches arthimetic exceptions.

**utils**: this module contain subfunction and assisting functions for the main functions in parser and calculator 
due to S.O.L.I.D requirements.

**exceptions**: this module contains the custom exception and errors classess for the calculator there are syntax exceptions 
and arthimetic ones.

**validations**: this module contains validation and assisting functions that are called before the parsing and calculating functions in order to prevent syntax errors from running in the first place.

**input**: in charge of input receiving and showing the result at the command line.
contains the main loop and handles syntax and input exceptions.
 
**main**: this module is the entry point to my program.

These are all the modules and descriptions about them.
Enjoy your use of my project!!!
