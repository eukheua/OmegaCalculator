from parser import *
from operations import *
from config import *


def evaluate_expression(expression):
    expression = clean_spaces(expression)
    expression = convert_string_expression_to_list(expression)
    expression = convert_infix_to_postfix(expression)
    return calculate_postfix(expression)

def calculate_postfix(expression):
    stack = []
    for item in expression:
        if type(item) == float:
            stack.append(item)
        else:
            operator = item
            if OPERATION_DICT[operator].position == "middle":
                if operator == subtraction_sign:
                    if len(stack)>1 and type(stack[len(stack)-1]) == float and type(stack[len(stack)-2]) == float:
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                    else:
                        operand2 = stack.pop()
                        operand1 = 0
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                stack.append(OPERATION_DICT[operator].operation_func(operand1,operand2))
            if OPERATION_DICT[operator].position == "left":
                operand1 = stack.pop()
                stack.append(OPERATION_DICT[operator].operation_func(operand1))
            if OPERATION_DICT[operator].position == "right":
                operand1 = stack.pop()
                stack.append(OPERATION_DICT[operator].operation_func(operand1))
    if len(stack) > 1:
        raise RuntimeError("illegal expression")
    return stack[0]
