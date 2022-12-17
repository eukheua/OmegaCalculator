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
        return str(self.__class__.__name__) + "\n" + CalculatorArithmeticError.__str__(self)


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
        return str(self.__class__.__name__) + "\n" + CalculatorArithmeticError.__str__(self)


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
        return str(self.__class__.__name__) + "\n" + CalculatorArithmeticError.__str__(self)


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
        return str(self.__class__.__name__) + "\n" + CalculatorArithmeticError.__str__(self)


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
        return str(self.__class__.__name__) + "\n" + CalculatorArithmeticError.__str__(self)


class NegationNotAdjacentToNumber(CalculatorSyntaxError):
    def __init__(self, message):
        """
        the function initialize an NegationNotAdjacentToNumber object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return str(self.__class__) + "\n" + super.__str__(self)


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
        return str(self.__class__.__name__) + "\n" + CalculatorSyntaxError.__str__(self)


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
        return str(self.__class__.__name__) + "\n" + CalculatorSyntaxError.__str__(self)


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
        return str(self.__class__.__name__) + "\n" + CalculatorSyntaxError.__str__(self)


class BracketsNotValid(CalculatorSyntaxError):
    def __init__(self, message):
        """
        the function initialize an BracketsNotValid object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self):
        """
        :return: the message
         """
        return str(self.__class__.__name__) + "\n" + CalculatorSyntaxError.__str__(self)


def print_exception(exception: Exception) -> None:
    """
    the function prints an exception
    :param exception: the exception object
    :return: None
    """
    # built in exceptions
    print("\n\nError>>>>>>")
    if exception.__class__ == OverflowError:
        print(exception.__class__.__name__)
        print("Result too large")
        print(exception)
    elif exception.__class__ == ZeroDivisionError:
        print(exception.__class__.__name__)
        print(exception)
    elif exception.__class__ == RecursionError:
        print(exception.__class__.__name__)
        print("factorial")
        print(exception)
    elif exception.__class__ == Exception:
        print(exception.__class__.__name__)
        print("Unknown Exception")
        print(exception)
    else:
        # custom exceptions
        print(exception)
