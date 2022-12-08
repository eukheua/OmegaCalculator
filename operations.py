import math


class Operator(object):
    def __init__(self, symbol, order_in_operations, position, operation_func):
        self.symbol = symbol
        self.order_in_operations = order_in_operations
        self.position = position
        self.operation_func = operation_func


def add(op1, op2):
    return op1 + op2


def sub(op1, op2):
    return op1 - op2


def mul(op1, op2):
    return op1 * op2


def div(op1, op2):
    return op1 / op2


def power(op1, op2):
    return math.pow(op1, op2)


def mod(op1, op2):
    return op1 % op2


def maximum(op1, op2):
    if op1 > op2:
        return op1
    else:
        return op2


def minimum(op1, op2):
    if op1 < op2:
        return op1
    else:
        return op2


def avg(op1, op2):
    return (op1 + op2) / 2


def neg(op):
    return -op


def fac(op):
    if op < 0:
        raise Exception("Factorial done on negative number")
    if op == 1 or op == 0:
        return 1
    return fac(op - 1) * op


def sum_digits(op):
    sum_of_digits = 0
    for c in str(op):
        if c.isdigit():
            sum_of_digits += float(c)
        else:
            if c == 'e':
                break
    return sum_of_digits
