from utils import check_if_sum_digits_and_minus_on_same_dimension, \
    check_how_to_add_minus_if_next_char_is_open_bracket_or_negation_sign, \
    check_how_to_add_minus_if_next_char_is_type_float_or_dot, check_what_to_do_with_current_char, \
    check_negation_sign_potential_error, check_potential_switch_of_minus_to_unary_minus, \
    check_convert_infix_to_postfix_loop_condition
from config import *


def convert_string_expression_to_list(expression: str) -> list:
    """
    the function converts raw input of the expression to a list that represents its actual meaning
    :param expression: string representing the expression
    :return: List that represents its actual meaning
    """
    expression_list = []
    number = ""
    minus_list = []
    remind_sum_digit_action_before_minus = False
    for i in range(0, len(expression)):
        if len(minus_list) > 0 and expression[i] != subtraction_sign:
            if check_if_sum_digits_and_minus_on_same_dimension(expression[i::]):
                remind_sum_digit_action_before_minus = True
        if expression[i] == open_bracket or expression[i] == negation_sign:
            check_how_to_add_minus_if_next_char_is_open_bracket_or_negation_sign(i, expression_list, minus_list)
        if expression[i].isdigit() is True or expression[i] == dot:
            number = check_how_to_add_minus_if_next_char_is_type_float_or_dot(
                number,
                expression_list,
                expression,
                i,
                minus_list,
                remind_sum_digit_action_before_minus
            )
            if remind_sum_digit_action_before_minus:
                remind_sum_digit_action_before_minus = False
        else:
            number = check_what_to_do_with_current_char(number, expression_list, expression, i, minus_list)
    if number != "":
        expression_list.append(float(number))
    return expression_list


def convert_infix_to_postfix(expression_list: list) -> list:
    """
    the function converts the infix representation of the expression to a postfix representation
    :param expression_list: expression: list representing the expression
    :return: postfix representation of expression
    """
    stack = []
    postfix_expression_list = []
    for i in range(len(expression_list)):
        if type(expression_list[i]) == float:
            postfix_expression_list.append(expression_list[i])
        else:
            if expression_list[i] == negation_sign:
                check_negation_sign_potential_error(expression_list, i)
            if expression_list[i] == subtraction_sign:
                check_potential_switch_of_minus_to_unary_minus(expression_list, i)
            if expression_list[i] == closed_bracket:
                while stack[len(stack) - 1] != open_bracket:
                    postfix_expression_list.append(stack.pop())
                stack.pop()
            elif expression_list[i] == open_bracket:
                stack.append(expression_list[i])
            else:
                if len(stack) != 0:
                    while check_convert_infix_to_postfix_loop_condition(stack, expression_list, i):
                        postfix_expression_list.append(stack.pop())
                stack.append(expression_list[i])
    while len(stack) != 0:
        postfix_expression_list.append(stack.pop())
    return postfix_expression_list
