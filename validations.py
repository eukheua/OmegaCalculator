from config import open_bracket, closed_bracket, supported_operators, dot, supported_operations, OPERATION_DICT, \
    subtraction_sign, negation_sign
from colors import *
from exceptions import BracketsNotBalanced, EmptyBrackets, SymbolNotRecognized, OperatorsNotPositionedValidly, \
    DecimalPointNotPositionedValidly, CalculatorSyntaxError


def assert_validations(expression):
    valid = True
    validation_list = [validate_brackets_balance(expression),
                       validate_brackets_not_empty(expression),
                       validate_legal_symbols(expression),
                       validate_operators(expression),
                       validate_decimal_point(expression)]
    for item in validation_list:
        if item is not True:
            valid = False
            print_invalidation_exception(item[1])
    return valid


def print_invalidation_exception(exception: CalculatorSyntaxError) -> None:
    """
    the function prints the message of syntax exceptions nicely
    :param exception:  exception object
    :return: None
    """
    print("-----------------------------------------")
    print(exception)
    print("-----------------------------------------")


def validate_brackets_balance(expression: str) -> tuple[bool, BracketsNotBalanced] | bool:
    """
    the function validates brackets are balanced
    :param expression: the string expression
    :return: if brackets are balanced True
             else False and BracketsNotBalanced exception Object
    """
    stack = []
    balanced = True
    problem_index = 0
    for i in range(len(expression)):
        if balanced is False:
            break
        if expression[i] == open_bracket:
            stack.append(expression[i])
            problem_index = i
        if expression[i] == closed_bracket:
            if len(stack) == 0:
                balanced = False
                problem_index = i
            else:
                stack.pop()
    if len(stack) > 0:
        balanced = False
    if not balanced:
        message = generate_message(expression, problem_index, BracketsNotBalanced)
        invalidity = BracketsNotBalanced(message)
        return False, invalidity
    return True


def validate_brackets_not_empty(expression: str) -> tuple[bool, EmptyBrackets] | bool:
    """
    the function validates brackets are not empty
    :param expression: the string expression
    :return: if brackets are not empty True
             else False and EmptyBrackets exception Object
    """
    empty = False
    problem_index = []
    for i in range(len(expression)):
        if False is True:
            break
        if expression[i] == open_bracket:
            if i < len(expression) - 1:
                if expression[i+1] == closed_bracket:
                    empty = True
                    problem_index = i, i+1
    if empty:
        message = generate_message(expression, problem_index, EmptyBrackets)
        invalidity = EmptyBrackets(message)
        return False, invalidity
    return True


def validate_legal_symbols(expression: str) -> tuple[bool, SymbolNotRecognized] | bool:
    """
    the function validates that all symbols in expression are supported
    :param expression: the string expression
    :return: if all symbols in expression are supported True
             else False and SymbolNotRecognized exception Object
    """
    valid = True
    problem_index = 0
    for i in range(len(expression)):
        if not valid:
            break
        if not expression[i].isdigit() and expression[i] not in supported_operators and expression[i] != dot:
            valid = False
            problem_index = i
    if not valid:
        message = generate_message(expression, problem_index, SymbolNotRecognized)
        invalidity = SymbolNotRecognized(message)
        return False, invalidity
    return True


def validate_decimal_point(expression: str) -> tuple[bool, DecimalPointNotPositionedValidly] | bool:
    """
    the function validates that decimal point in case of rational numbers is inserted correctly
    :param expression: the string expression
    :return: if all decimal points in expression are inserted correctly True
             else False and DecimalPointNotPositionedValidly exception Object
    """
    valid = True
    problem_index = 0
    for i in range(len(expression)-1):
        if expression[i] == dot and expression[i+1] == dot:
            valid = False
            problem_index = i
            break
    if not valid:
        message = generate_message(expression, problem_index, DecimalPointNotPositionedValidly)
        invalidity = DecimalPointNotPositionedValidly(message)
        return False, invalidity
    return True


def validate_operators(expression: str) -> tuple[bool, OperatorsNotPositionedValidly] | bool:
    """
    the function validates that all the operators are well positioned
    :param expression: the string expression
    :return: if all the operators are well positioned True
             else False and OperatorsNotPositionedValidly exception Object
    """
    valid = True
    problem_index = 0
    for i in range(len(expression)):
        if valid is False:
            break
        if expression[i] in supported_operations:
            if OPERATION_DICT[expression[i]].position == "middle":
                valid, problem_index = check_operator_validity_middle(expression, i, valid, problem_index)
            elif OPERATION_DICT[expression[i]].position == "left":
                valid, problem_index = check_operator_validity_left(expression, i, valid, problem_index)
            elif OPERATION_DICT[expression[i]].position == "right":
                valid, problem_index = check_operator_validity_right(expression, i, valid, problem_index)

        if expression[i] == open_bracket:
            valid, problem_index = check_opened_bracket_validity(expression, i, valid, problem_index)
        if expression[i] == closed_bracket:
            valid, problem_index = check_closed_bracket_validity(expression, i, valid, problem_index)

    if not valid:
        message = generate_message(expression, problem_index, OperatorsNotPositionedValidly)
        invalidity = OperatorsNotPositionedValidly(message)
        return False, invalidity
    return True


def check_operator_validity_middle(expression: str, i: int, valid: bool, problem_index: int) -> tuple[bool, int]:
    """
    the function determines whether a middle positioned operator is in valid position or not
    :param expression: string expression
    :param i: index
    :param valid: if valid or not
    :param problem_index: the index of the problem
    :return: whether the operator is in a valid place and the position of the error
    """
    if expression[i] == subtraction_sign:
        if i < len(expression) - 1:
            if expression[i + 1] == closed_bracket:
                valid = False
                problem_index = i
    else:
        if i > 0:
            if expression[i - 1] == open_bracket:
                valid = False
                problem_index = i
            if expression[i - 1] in OPERATION_DICT:
                if OPERATION_DICT[expression[i - 1]].position != "right":
                    valid = False
                    problem_index = i
        else:
            valid = False
            problem_index = i
        if i < len(expression) - 1:
            if expression[i + 1] in OPERATION_DICT:
                if OPERATION_DICT[expression[i + 1]].position != "left" and expression[i + 1] != subtraction_sign:
                    valid = False
                    problem_index = i
        else:
            valid = False
            problem_index = i
    return valid, problem_index


def check_operator_validity_left(expression: str, i: int, valid: bool, problem_index: int) -> tuple[bool, int]:
    """
    the function determines whether a left positioned operator is in valid position or not
    :param expression: string expression
    :param i: index
    :param valid: if valid or not
    :param problem_index: the index of the problem
    :return: whether the operator is in a valid place and the position of the error
    """
    if expression[i] == negation_sign:
        if i < len(expression) - 1:
            if not check_negation_sign_validity(expression, i+1):
                valid = False
                problem_index = i
        else:
            valid = False
            problem_index = i
    return valid, problem_index


def check_negation_sign_validity(expression: str, i: int) -> bool:
    """
    the function determines whether a negation sign is positioned correctly due to its special conditions
    :param expression: string expression
    :param i: index
    :return: whether the ~ is in a valid place
    """
    while expression[i] == subtraction_sign:
        i += 1
    if not expression[i].isdigit() and expression[i] != dot:
        return False
    return True


def check_operator_validity_right(expression: str, i: int, valid: bool, problem_index: int) -> tuple[bool, int]:
    """
    the function determines whether a right positioned operator is in valid position or not
    :param expression: string expression
    :param i: index
    :param valid: if valid or not
    :param problem_index: the index of the problem
    :return: whether the operator is in a valid place and the position of the error
    """
    if i > 0:
        if expression[i - 1] in supported_operations:
            if OPERATION_DICT[expression[i - 1]].position != "right":
                valid = False
                problem_index = i
        else:
            if expression[i - 1].isdigit() is False and expression[i - 1] != dot\
                    and expression[i - 1] != closed_bracket:
                valid = False
                problem_index = i
    else:
        valid = False
        problem_index = i
    return valid, problem_index


def check_opened_bracket_validity(expression: str, i: int, valid: bool, problem_index: int) -> tuple[bool, int]:
    """
    the function determines whether an opened bracket is in valid position or not
    :param expression: string expression
    :param i: index
    :param valid: if valid or not
    :param problem_index: the index of the problem
    :return: whether the opened bracket is in a valid place and the position of the error
    """
    if i < len(expression) - 1:
        if expression[i + 1] in supported_operations:
            if OPERATION_DICT[expression[i + 1]].position != "left" and expression[i + 1] != subtraction_sign:
                valid = False
                problem_index = i
    if i > 0:
        if expression[i - 1].isdigit() is True or expression[i - 1] == dot:
            valid = False
            problem_index = i
    return valid, problem_index


def check_closed_bracket_validity(expression: str, i: int, valid: bool, problem_index: int) -> tuple[bool, int]:
    """
    the function determines whether a closed bracket is in valid position or not
    :param expression: string expression
    :param i: index
    :param valid: if valid or not
    :param problem_index: the index of the problem
    :return: whether the closed bracket is in a valid place and the position of the error
    """
    if i > 0:
        if expression[i - 1] in supported_operations:
            if OPERATION_DICT[expression[i - 1]].position != "right":
                valid = False
                problem_index = i
    if i < len(expression) - 1:
        if expression[i + 1].isdigit() is True or expression[i + 1] == dot:
            valid = False
            problem_index = i
    return valid, problem_index


def generate_message(expression: str, problem_index: int | list, exception_class: object) -> str:
    """
    the function generates a message for exception
    :param expression: string expression
    :param problem_index: index of problem
    :param exception_class: the class of the exception
    :return: exception message
    """
    if exception_class == BracketsNotBalanced:
        return "Invalidity Type: Unbalanced brackets\n\n" \
            + "Unbalanced bracket at: \n" \
            + expression[:problem_index] + f"{RED} -->{WHITE}" + expression[problem_index] + f"{RED}<-- {WHITE}" \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of unbalanced bracket: " + str(problem_index)
    elif exception_class == EmptyBrackets:
        return "Invalidity Type: Empty brackets\n\n" \
            + "Empty bracket at: \n" \
            + expression[:problem_index[0]] + f"{RED} -->{WHITE}"\
               + expression[problem_index[0]]\
               + expression[problem_index[1]]\
               + f"{RED}<-- {WHITE}" \
            + expression[problem_index[1] + 1:len(expression)] \
            + "\n" + "indexes of empty brackets: " + str(problem_index[0]) + ", " + str(problem_index[1])
    elif exception_class == SymbolNotRecognized:
        return "Invalidity Type: Symbol is not recognized\n\n" \
            "Invalid symbol at: \n" \
            + expression[:problem_index] + f"{RED} -->{WHITE}" + expression[problem_index] + f"{RED}<-- {WHITE}" \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of invalid symbol : " + str(problem_index)
    elif exception_class == OperatorsNotPositionedValidly:
        return "Invalidity Type: Operator is not positioned correctly\n\n" \
            "Invalidly positioned operator at: \n" \
            + expression[:problem_index] + f"{RED} -->{WHITE}" + expression[problem_index] + f"{RED}<-- {WHITE}" \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of invalidly positioned operator : " + str(problem_index)
    elif exception_class == DecimalPointNotPositionedValidly:
        return "Invalidity Type: Decimal Point is not positioned validly\n\n" \
            "Invalid decimal point at: \n" \
            + expression[:problem_index] + f"{RED} -->{WHITE}" + expression[problem_index] + f"{RED}<-- {WHITE}" \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of invalid decimal point : " + str(problem_index)
    else:
        return "Invalidity Type: Unknown\n\n" \
            "Invalid input at: \n" \
            + expression[:problem_index] + f"{RED} -->{WHITE}" + expression[problem_index] + f"{RED}<-- {WHITE}" \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of invalid input : " + str(problem_index)
