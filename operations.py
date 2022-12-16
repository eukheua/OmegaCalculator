class Operator(object):
    """
    this class represents an operator
    """

    def __init__(self, symbol: str, order_in_operations: int, position: str, operation_func) -> None:
        """
        the function initialize an operator object
        :param symbol: the symbol
        :param order_in_operations: order in operation represented by number
        :param position: position of operator relative to the operand
        :param operation_func: the function that the symbol represents
        """
        self.symbol = symbol
        self.order_in_operations = order_in_operations
        self.position = position
        self.operation_func = operation_func


def add(op1: float, op2: float) -> float:
    """
    the function adds two float type number
    :param op1: first operand
    :param op2: second operand
    :return: the sum of the two operands
    """
    return op1 + op2


def sub(op1: float, op2: float) -> float:
    """
    the function subtracts two float type number
    :param op1: first operand
    :param op2: second operand
    :return: the difference of the two operands
    """
    return op1 - op2


def mul(op1: float, op2: float) -> float:
    """
    the function multiplies two float type number
    :param op1: first operand
    :param op2: second operand
    :return: the multiplication of the two operands
    """
    return op1 * op2


def div(op1: float, op2: float) -> float:
    """
    the function divides two float type number
    :param op1: first operand
    :param op2: second operand
    :return: the quotient of the two operands
    """
    if op2 == 0:
        raise ZeroDivisionError("Division by zero")
    return op1 / op2


def power(op1: float, op2: float) -> float:
    """
       the function raises op1 in the power of op2
       :param op1: base
       :param op2: exponent
       :return: the result of the power raise
    """
    result = pow(op1, op2)
    if type(result) is complex:
        raise Exception("complex")
    return result


def mod(op1: float, op2: float) -> float:
    """
        the function divides two float type number to get the remnant
        :param op1: first operand
        :param op2: second operand
        :return: the remnant of the division operation
    """
    if op2 == 0:
        raise ZeroDivisionError("Division by zero")
    return op1 % op2


def maximum(op1: float, op2: float) -> float:
    """
        the function compares two float numbers to find maximal number
        :param op1: first operand
        :param op2: second operand
        :return: the maximal of the two operands
    """
    if op1 > op2:
        return op1
    else:
        return op2


def minimum(op1: float, op2: float) -> float:
    """
        the function compares two float numbers to find minimal number
        :param op1: first operand
        :param op2: second operand
        :return: the minimal of the two operands
    """
    if op1 < op2:
        return op1
    else:
        return op2


def avg(op1: float, op2: float) -> float:
    """
        the function finds average of two float numbers
        :param op1: first operand
        :param op2: second operand
        :return: the average of the two operands
    """
    return (op1 + op2) / 2


def neg(op: float) -> float:
    """
        the function negates a float number
        :param op: operand
        :return: the negation of the operand
    """
    return -op


def fac(op: float) -> float:
    """
        the function calculates the factorial of a float number
        :param op: operand
        :return: the factorial of the operand
    """
    if op < 0:
        raise Exception("Factorial done on negative number")
    elif int(op) != op:
        raise Exception("Factorial done on rational number")
    if op == 1 or op == 0:
        return 1.0
    return fac(op - 1) * op


def sum_digits(op: float) -> float:
    """
        the function calculates the sum of digits of a float number
        :param op: operand
        :return: the sum of digits of the operand
    """
    if op < 0:
        sign = -1
        op = -op
    else:
        sign = 1
    sum_of_digits = 0
    # converts number potentially represented in scientific notation for example 4.1e+05
    op = "{:f}".format(op)
    for c in op:
        if c.isdigit():
            sum_of_digits += float(c)
        else:
            if c == 'e':
                break
    return sum_of_digits * sign
