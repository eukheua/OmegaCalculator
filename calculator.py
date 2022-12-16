from parser import *
from utils import *

# calculating func


def evaluate_expression(expression):
    expression = clean_spaces(expression)
    print(expression)
    expression = convert_string_expression_to_list(expression)
    print(expression)
    expression = convert_infix_to_postfix(expression)
    print(expression)
    return calculate_postfix(expression)


def calculate_postfix(expression: list) -> float:
    """
    the function gets a postfix expression and calculates it
    :param expression: postfix expression list
    :return: the result of the expression
    """
    stack = []
    for item in expression:
        if type(item) == float:
            stack.append(item)
        else:
            operator = item
            if OPERATION_DICT[operator].position == "middle":
                calculate_operator_in_middle(stack, operator)
            if OPERATION_DICT[operator].position == "left" or OPERATION_DICT[operator].position == "right":
                calculate_operator_in_left_or_right(stack, operator)
    if len(stack) != 1:
        raise RuntimeError("illegal expression")
    return stack[0]
