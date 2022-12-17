from parser import *
from utils import *

# calculating func


def print_result(result: float) -> None:
    """
    the function prints the result of the mathematical expression
    :param result:  the result
    :return: None
    """
    print("\n\n\n")
    print("The result is : " + str(result))


def calculate_postfix(expression: list) -> float:
    """
    the function gets a postfix expression and calculates it
    :param expression: postfix expression list
    :return: the result of the expression
    """
    stack = []
    for item in expression:
        if len(stack) >0:
            if stack[0] < float('-inf') or stack[0] > float('inf'):
                raise Exception("woowowowow")
        if type(item) == float:
            stack.append(item)
        else:
            operator = item
            if OPERATION_DICT[operator].position == "middle":
                calculate_operator_in_middle(stack, operator)
            if OPERATION_DICT[operator].position == "left" or OPERATION_DICT[operator].position == "right":
                calculate_operator_in_left_or_right(stack, operator)
    if len(stack) != 1:
        raise ExpressionCantBeEvaluated("The expression Cant be evaluated")
    return stack[0]
