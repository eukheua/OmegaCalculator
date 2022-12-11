from config import *


def clean_spaces(expression):
    expression = expression.split(" ")
    return "".join(expression)


def check_if_sum_digits_and_minus_on_same_dimension(expression):
    stack = []
    found = False
    for i in range(0,len(expression)):
        if expression[i] == sum_of_digits_sign:
            found = True
            break
        elif expression[i] == open_bracket:
            stack.append(open_bracket)
        elif expression[i] == closed_bracket:
            if len(stack) == 0:
                break
            stack.pop()
    if len(stack) != 0 or not found:
        return False
    return True



# fixxx () - interactions
def convert_string_expression_to_list(expression):
    expression_list = []
    number = ""
    minus_list = []
    sum_digit_list = []
    sum_digits_minus_list = []
    remind_sum_digit_action_before_minus = False
    index_sum_digit_before_minuses = 0
    try:
        for i in range(0, len(expression)):
            if len(minus_list) > 0 and expression[i] != subtraction_sign:
                if check_if_sum_digits_and_minus_on_same_dimension(expression[i::]):
                    sum_digits_minus_list = minus_list
                    remind_sum_digit_action_before_minus = True
                    index_sum_digit_before_minuses = i - len(minus_list) - 1
                    # minus_list = []
            if expression[i] == open_bracket or expression[i] == negation_sign:  # if 3--(
                if len(minus_list) > 0:
                    if len(minus_list) - i != 0:
                        if (len(minus_list) - 1) % 2 != 0:
                            expression_list.append(subtraction_sign)
                        else:
                            expression_list.append(addition_sign)
                        expression_list.append(subtraction_sign)
                    else:  # if in start
                        if len(minus_list) % 2 != 0:
                            expression_list.append(subtraction_sign)
                    minus_list = []
            if expression[i].isdigit() is True or expression[i] == dot:
                if len(minus_list) > 0:
                    if len(minus_list) - i != 0:
                        if expression[i - len(minus_list) - 1] in supported_operations:
                            if len(minus_list) % 2 != 0:
                                if remind_sum_digit_action_before_minus:
                                    expression_list.append(subtraction_sign)
                                else:
                                    number += subtraction_sign
                        else:
                            if len(minus_list) == 1:
                                expression_list.append(subtraction_sign)
                            else:
                                if remind_sum_digit_action_before_minus:
                                    if (len(minus_list) - 1) % 2 != 0:
                                        expression_list.append(subtraction_sign)
                                    else:
                                        expression_list.append(addition_sign)
                                    expression_list.append(subtraction_sign)
                                else:
                                    number += subtraction_sign
                                    if (len(minus_list) - 1) % 2 != 0:
                                        expression_list.append(subtraction_sign)
                                    else:
                                        expression_list.append(addition_sign)
                    else:
                        if (len(minus_list)) % 2 != 0:
                            if remind_sum_digit_action_before_minus:
                                expression_list.append(subtraction_sign)
                            else:
                                number += subtraction_sign
                    minus_list = []
                number += expression[i]
                if remind_sum_digit_action_before_minus:
                    sum_digits_minus_list = []
                    remind_sum_digit_action_before_minus = False
                    index_sum_digit_before_minuses = 0
            else:
                if number != "":
                    expression_list.append(float(number))
                    number = ""
                if expression[i] in supported_operators:
                    if expression[i] == open_bracket:
                        if len(minus_list) > 0:
                            if len(minus_list) % 2 == 1:
                                expression_list.append(subtraction_sign)
                            minus_list = []
                        expression_list.append(expression[i])
                    elif expression[i] == subtraction_sign:
                        minus_list.append(subtraction_sign)
                    else:
                        expression_list.append(expression[i])
        if number != "":
            expression_list.append(float(number))
            number = ""
        return expression_list
    except:
        raise ValueError("Not valid expression")


def convert_infix_to_postfix(expression_list):
    stack = []
    postfix_expression_list = []
    for i in range(len(expression_list)):
        if type(expression_list[i]) == float:
            postfix_expression_list.append(expression_list[i])
        else:
            if expression_list[i] == negation_sign:
                if type(expression_list[i + 1]) != float:
                    raise Exception("~ error")
            if expression_list[i] == subtraction_sign:
                if i == 0 or expression_list[i-1] == open_bracket:
                    expression_list[i] = unary_minus_sign
                else:
                    if expression_list[i - 1] != closed_bracket and type(expression_list[i - 1]) != float :
                        expression_list[i] = unary_minus_sign
            if expression_list[i] == closed_bracket:
                while stack[len(stack) - 1] != open_bracket:
                    postfix_expression_list.append(stack.pop())
                stack.pop()
            elif expression_list[i] == open_bracket:
                stack.append(expression_list[i])
            else:
                if len(stack) != 0:
                    while len(stack) != 0 and stack[len(stack) - 1] != open_bracket and OPERATION_DICT[
                        stack[len(stack) - 1]].order_in_operations >= \
                            OPERATION_DICT[expression_list[i]].order_in_operations and not (expression_list[i] == sum_of_digits_sign and stack[len(stack) - 1] == unary_minus_sign) and not (expression_list[i] == negation_sign and stack[len(stack) - 1] == unary_minus_sign):
                        postfix_expression_list.append(stack.pop())
                stack.append(expression_list[i])
    while len(stack) != 0:
        postfix_expression_list.append(stack.pop())
    return postfix_expression_list