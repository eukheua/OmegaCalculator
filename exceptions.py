from colors import *


class CalculatorSyntaxError(Exception):
    def __init__(self, message):
        """
        the function initialize an CalculatorSyntaxError object
        :param message: the message
        """
        self.message = message

    def __str__(self):
        """
        :return: the message
        """
        return self.message


class CalculatorArithmeticError(RuntimeError):
    def __init__(self, message):
        """
        the function initialize an CalculatorArithmeticError object
        :param message: the message
        """
        self.message = message

    def __str__(self):
        """
        :return: the message
        """
        return self.message


class FactorialOnNegativeNumber(CalculatorArithmeticError):
    def __init__(self, message):
        """
        the function initialize an FactorialOnNegativeNumber object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorArithmeticError.__str__(self)


class ExpressionCantBeEvaluated(CalculatorArithmeticError):
    def __init__(self, message):
        """
        the function initialize an ExpressionCantBeEvaluated object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorArithmeticError.__str__(self)


class FactorialOnRationalNumber(CalculatorArithmeticError):
    def __init__(self, message):
        """
        the function initialize an FactorialOnNegativeNumber object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorArithmeticError.__str__(self)


class FactorialResultCantBeAchievedDueToRecursionLimit(CalculatorArithmeticError):
    def __init__(self, message):
        """
        the function initialize an FactorialResultCantBeAchievedDueToRecursionLimit object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorArithmeticError.__str__(self)


class ComplexNumberResult(CalculatorArithmeticError):
    def __init__(self, message):
        """
        the function initialize an ComplexNumberResult object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorArithmeticError.__str__(self)


class OperatorsNotPositionedValidly(CalculatorSyntaxError):
    def __init__(self, message):
        """
        the function initialize an OperatorsNotPositionedValidly object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorSyntaxError.__str__(self)


class DecimalPointNotPositionedValidly(CalculatorSyntaxError):
    def __init__(self, message):
        """
        the function initialize an OperatorsNotPositionedValidly object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorSyntaxError.__str__(self)


class SymbolNotRecognized(CalculatorSyntaxError):
    def __init__(self, message):
        """
        the function initialize an SymbolNotRecognized object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorSyntaxError.__str__(self)


class BracketsNotBalanced(CalculatorSyntaxError):
    def __init__(self, message):
        """
        the function initialize an BracketsNotBalanced object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorSyntaxError.__str__(self)


class EmptyBrackets(CalculatorSyntaxError):
    def __init__(self, message):
        """
        the function initialize an EmptyBrackets object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return RED + str(self.__class__.__name__) + WHITE + "\n" + CalculatorSyntaxError.__str__(self)


def print_exception(exception: Exception | KeyboardInterrupt) -> None:
    """
    the function prints an exception
    :param exception: the exception object or KeyboardInterrupt object
    :return: None
    """
    # built in exceptions
    print("-----------------------------------------")
    print("Error>>>>>>")
    if exception.__class__ == EOFError:
        print(RED + exception.__class__.__name__ + WHITE)
        print("exiting due to EOF input")
        print("-----------------------------------------")
    elif exception.__class__ == KeyboardInterrupt:
        print(RED + exception.__class__.__name__ + WHITE)
        print("exiting due to keyboard interrupt")
        print("-----------------------------------------")
    elif exception.__class__ == OverflowError:
        print(RED + exception.__class__.__name__ + WHITE)
        print("Result out of numeric bounds")
        print("-----------------------------------------")
    elif exception.__class__ == ZeroDivisionError:
        print(RED + exception.__class__.__name__ + WHITE)
        print(exception)
        print("-----------------------------------------")
    elif exception.__class__ == RecursionError:
        print(RED + exception.__class__.__name__ + WHITE)
        print("factorial")
        print(exception)
        print("-----------------------------------------")
    elif exception.__class__ == Exception:
        print(RED + exception.__class__.__name__ + WHITE)
        print("Unknown Exception")
        print(exception)
        print("-----------------------------------------")
    else:
        # custom exceptions
        print(exception)
        print("-----------------------------------------")
