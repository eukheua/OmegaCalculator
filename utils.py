from config import OPERATION_DICT, subtraction_sign, open_bracket, unary_minus_sign, supported_operations, \
    negation_sign, sum_of_digits_sign, closed_bracket, addition_sign, dot, supported_operators


def clean_white_chars(expression: str) -> str:
    """
    the function cleans all spaces in the expression received as a string
    :param expression: the string expression
    :return: the expression without spaces
    """
    expression = expression.split()
    return "".join(expression)


def calculate_operator_in_left_or_right(stack: list, operator: str) -> None:
    """
    the function calculates a subexpression whose operator is unary and its position is either to the left or right
    and pushes it to the stack
    :param stack: the stack used to calculate the postfix expression
    :param operator: the operator
    :return: None
    """
    operand1 = stack.pop()
    stack.append(OPERATION_DICT[operator].operation_func(operand1))


def calculate_operator_in_middle(stack: list, operator: str) -> None:
    """
    the function calculates a subexpression whose operator is binary and its position is positioned between the operands
    and pushes it to the stack
    :param stack: the stack used to calculate the postfix expression
    :param operator:the operator
    :return: None
    """
    if operator == subtraction_sign:
        if len(stack) > 1 and type(stack[len(stack) - 1]) == float and type(stack[len(stack) - 2]) == float:
            operand2 = stack.pop()
            operand1 = stack.pop()
        else:
            operand2 = 0
            operand1 = stack.pop()
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
    stack.append(OPERATION_DICT[operator].operation_func(operand1, operand2))


def check_potential_switch_of_minus_to_unary_minus(expression_list: list, i: int) -> None:
    """
    the function checks whether an - is actually a sign and should be treated that way
    :param expression_list: a list representing the mathematical expression
    :param i: the current index
    :return: None
    """
    if i == 0 or expression_list[i - 1] == open_bracket:
        expression_list[i] = unary_minus_sign
    if expression_list[i - 1] in supported_operations:
        if OPERATION_DICT[expression_list[i - 1]].position != "right":
            expression_list[i] = unary_minus_sign


def check_negation_sign_potential_error(expression_list: list, i: int) -> None:
    """
    the function checks whether the ~ sign is positioned legally
    :param expression_list: a list representing the mathematical expression
    :param i: the current index
    :return:
    """
    if type(expression_list[i + 1]) != float:
        raise Exception("~ error")


def check_convert_infix_to_postfix_loop_condition(stack: list, expression_list: list, i: int) -> bool:
    """
    the function hold a condition to the order of operations in which the expression shall be calculated
    :param stack: the stack used to calculate the postfix expression
    :param expression_list: a list representing the mathematical expression
    :param i: the current index
    :return: if the current operator should be evaluated before or after the previous one
    """
    return (len(stack) != 0 and
            stack[len(stack) - 1] != open_bracket and
            OPERATION_DICT[stack[len(stack) - 1]].order_in_operations >= OPERATION_DICT[
                expression_list[i]].order_in_operations and not
            (expression_list[i] == sum_of_digits_sign and stack[len(stack) - 1] == unary_minus_sign) and not
            (expression_list[i] == negation_sign and stack[len(stack) - 1] == unary_minus_sign))


def check_if_sum_digits_and_minus_on_same_dimension(expression: str) -> bool:
    """
    the function checks whether an - is adjacent to the same subexpression a # is adjacent to
    :param expression: a string representing the math expression
    :return: whether the condition mentioned above is relevant
    """
    stack = []
    found = False
    for i in range(0, len(expression)):
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


def check_how_to_add_minus_if_next_char_is_open_bracket_or_negation_sign(
        i: int,
        expression_list: list,
        minus_list: list,
) -> None:
    """
    the function checks how to treat an - if the next is ( or ~ meaning that it should be treated as an operand and
    appending the correct operators accordingly
    :param i: the current index
    :param expression_list: a list representing the mathematical expression
    :param minus_list: a list that counts the number of - between too objects
    :return: None
    """
    if len(minus_list) > 0:
        if len(minus_list) == 1:
            expression_list.append(subtraction_sign)
        else:
            if len(minus_list) - i != 0:
                if (len(minus_list) - 1) % 2 != 0:
                    expression_list.append(subtraction_sign)
                else:
                    expression_list.append(addition_sign)
                expression_list.append(subtraction_sign)
            else:
                if len(minus_list) % 2 != 0:
                    expression_list.append(subtraction_sign)
        minus_list.clear()


def check_how_to_add_minus_if_next_char_is_type_float_or_dot(
        number: str,
        expression_list: list,
        expression: str,
        i: int,
        minus_list: list,
        remind_sum_digit: bool
) -> str:
    """
    the function determines how to treat the number that is added next to the expression list
    it checks how to add minuses or not according to the items before the start of the number
    :param number: the num represented as string
    :param expression_list:  the expression represented as list
    :param expression: the expression represented as string
    :param i: current index
    :param minus_list: list that counts the number of - before the number
    :param remind_sum_digit: tells if the # is in the same subexpression as a - due to the special treatment to #
    :return: the sign of the number concatenated to the start of the num string
    """
    if len(minus_list) > 0:
        if len(minus_list) - i != 0:
            number = check_how_to_add_minus_if_next_char_is_type_float_or_dot_when_minus_not_first(
                number,
                expression_list,
                expression,
                i,
                minus_list,
                remind_sum_digit
               )
        else:
            number = check_how_to_add_minus_if_next_char_is_type_float_or_dot_when_minus_first(
                number,
                expression_list,
                minus_list,
                remind_sum_digit
               )
        minus_list.clear()
    number += expression[i]
    return number


def check_how_to_add_minus_if_next_char_is_type_float_or_dot_when_minus_first(
        number: str,
        expression_list: list,
        minus_list: list,
        remind_sum_digit: bool
) -> str:
    """
    the function determines how to treat the number that is added next to the expression list
    it checks how to add minuses or not according to the items before the start of the number
    if the number is the first item in the expression
    :param number: the num represented as string
    :param expression_list:  the expression represented as list
    :param minus_list: list that counts the number of - before the number
    :param remind_sum_digit: tells if the # is in the same subexpression as a - due to the special treatment to #
    :return: the sign of the number concatenated to the start of the num string
    """
    if (len(minus_list)) % 2 != 0:
        if remind_sum_digit:
            expression_list.append(subtraction_sign)
        else:
            number += subtraction_sign
    return number


def check_how_to_add_minus_if_next_char_is_type_float_or_dot_when_minus_not_first(
        number: str,
        expression_list: list,
        expression: str,
        i: int,
        minus_list: list,
        remind_sum_digit: bool
) -> str:
    """
    the function determines how to treat the number that is added next to the expression list
    it checks how to add minuses or not according to the items before the start of the number
    if the number is not the first item in the expression
    :param number: the num represented as string
    :param expression_list:  the expression represented as list
    :param expression: the expression represented as string
    :param i: current index
    :param minus_list: list that counts the number of - before the number
    :param remind_sum_digit: tells if the # is in the same subexpression as a - due to the special treatment to #
    :return: the sign of the number concatenated to the start of the num string
    """
    if expression[i - len(minus_list) - 1] in supported_operations:
        if OPERATION_DICT[expression[i - len(minus_list) - 1]].position == "right":
            number = if_before_minus_there_is_number_or_closed_bracket(
                number,
                expression_list,
                minus_list,
                remind_sum_digit
            )
        else:
            number = if_before_minus_there_is_operator_or_opened_bracket(
                number,
                expression_list,
                minus_list,
                remind_sum_digit
            )
    else:
        if expression[i - len(minus_list) - 1] == closed_bracket or\
                expression[i - len(minus_list) - 1].isdigit() or\
                expression[i - len(minus_list) - 1] == dot:
            number = if_before_minus_there_is_number_or_closed_bracket(
                number,
                expression_list,
                minus_list,
                remind_sum_digit
            )
        if expression[i - len(minus_list) - 1] == open_bracket:
            number = if_before_minus_there_is_operator_or_opened_bracket(
                number,
                expression_list,
                minus_list,
                remind_sum_digit
            )
    return number


def if_before_minus_there_is_operator_or_opened_bracket(
        number: str,
        expression_list: list,
        minus_list: list,
        remind_sum_digit: bool
) -> str:
    """
    the function determines how to treat the number that is added next to the expression list
    it checks how to add minuses or not according to the items before the start of the number
    if the number is the first item in the expression and before the - there is an operator or open bracket
    :param number: the num represented as string
    :param expression_list:  the expression represented as list
    :param minus_list: list that counts the number of - before the number
    :param remind_sum_digit: tells if the # is in the same subexpression as a - due to the special treatment to #
    :return: the sign of the number concatenated to the start of the num string
    """
    if len(minus_list) % 2 != 0:
        if remind_sum_digit:
            expression_list.append(subtraction_sign)
        else:
            number += subtraction_sign
    return number


def if_before_minus_there_is_number_or_closed_bracket(
        number: str,
        expression_list: list,
        minus_list: list,
        remind_sum_digit: bool
) -> str:
    """
    the function determines how to treat the number that is added next to the expression list
    it checks how to add minuses or not according to the items before the start of the number
    if the number is the first item in the expression and before the - there is a number or closed bracket
    :param number: the num represented as string
    :param expression_list:  the expression represented as list
    :param minus_list: list that counts the number of - before the number
    :param remind_sum_digit: tells if the # is in the same subexpression as a - due to the special treatment to #
    :return: the sign of the number concatenated to the start of the num string
    """
    if len(minus_list) == 1:
        expression_list.append(subtraction_sign)
    else:
        if remind_sum_digit:
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
    return number


def check_what_to_do_with_current_char(
        number: str,
        expression_list: list,
        expression: str,
        i: int,
        minus_list: list
) -> str:
    """
    the function determines what to do with the current char
    if - add to minus list
    if the char is not a digit or . and it reached here after a new number was formed then add it to list
    if an operator add it to list
    :param number:  the num represented as string
    :param expression_list: the expression represented as list
    :param expression: the expression represented as string
    :param i: index
    :param minus_list: list that counts the number of - before the number
    :return: return the current value of number (it could be initialized)
    """
    if number != "":
        expression_list.append(float(number))
        number = ""
    if expression[i] in supported_operators:
        if expression[i] == subtraction_sign:
            minus_list.append(subtraction_sign)
        else:
            expression_list.append(expression[i])
    return number
