from config import OPERATION_DICT
from parser import convert_string_expression_to_list, convert_infix_to_postfix
from utils import clean_white_chars, calculate_operator_in_middle, calculate_operator_in_left_or_right
from validations import assert_validations
from exceptions import print_exception, FactorialOnNegativeNumber, FactorialOnRationalNumber, ComplexNumberResult, \
    ExpressionCantBeEvaluated, FactorialResultCantBeAchievedDueToRecursionLimit


def evaluate(expression: str) -> None | float:
    """
    this function receives the expression and returns the appropriate return value
    :param expression: a string representation of expression
    :return: the answer or None in case of validation or runtime error
    """
    expression = clean_white_chars(expression)
    if not assert_validations(expression):
        return
    expression = convert_string_expression_to_list(expression)
    expression = convert_infix_to_postfix(expression)
    try:
        result = calculate_postfix(expression)
        return result
    except ZeroDivisionError as z_d_e:
        print_exception(z_d_e)
    except FactorialOnNegativeNumber as f_o_n_n:
        print_exception(f_o_n_n)
    except FactorialOnRationalNumber as f_o_r_n:
        print_exception(f_o_r_n)
    except ComplexNumberResult as c_n_r:
        print_exception(c_n_r)
    except ExpressionCantBeEvaluated as e_c_b_e:
        print_exception(e_c_b_e)
    except OverflowError as o_f_e:
        print_exception(o_f_e)
    except FactorialResultCantBeAchievedDueToRecursionLimit as r_e:
        print_exception(r_e)
    except Exception as exception:
        print_exception(exception)


def print_result(result: float) -> None:
    """
    the function prints the result of the mathematical expression
    :param result:  the result
    :return: None
    """
    print("\nThe result is : " + str(result))
    print("-----------------------------------------")


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
        raise ExpressionCantBeEvaluated("The expression Cant be evaluated")
    if stack[0] == float('inf') or stack[0] == float('-inf'):
        raise OverflowError()
    return stack[0]
