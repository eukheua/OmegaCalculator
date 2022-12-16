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


"""class SumOfDigitsOnNegativeNumber(RuntimeError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.__class__) + "\n" + self.message"""


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
        return str(self.__class__) + "\n" + CalculatorArithmeticError.__str__(self)


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
        return str(self.__class__) + "\n" + CalculatorArithmeticError.__str__(self)


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
        return str(self.__class__) + "\n" + CalculatorSyntaxError.__str__(self)


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
        return str(self.__class__) + "\n" + CalculatorSyntaxError.__str__(self)


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
        return str(self.__class__) + "\n" + CalculatorSyntaxError.__str__(self)
