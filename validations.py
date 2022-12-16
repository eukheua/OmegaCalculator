from config import *
from exceptions import *
from exceptions import BracketsNotValid


class InValidity(object):
    def __init__(self, message: str) -> None:
        """
        the function initialize an InValidity object
        :param message: the message
        """
        self.message = message

    def __str__(self) -> str:
        """
        :return: the message
        """
        return self.message


class BracketsInValidity(InValidity):
    def __init__(self, message: str) -> None:
        """
        the function initialize an BracketsInValidity object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self) -> str:
        """
        :return: the message
        """
        return super.__str__(self)


class LegalSignsInValidity(InValidity):
    def __init__(self, message: str) -> None:
        """
        the function initialize an BracketsInValidity object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self) -> str:
        """
        :return: the message
        """
        return super.__str__(self)


class OperatorsInValidity(InValidity):
    def __init__(self, message: str) -> None:
        """
        the function initialize an BracketsInValidity object
        :param message: the message
        """
        super().__init__(message)

    def __str__(self) -> str:
        """
        :return: the message
        """
        return super.__str__(self)


def main():
    validation_list = []
    validation_list.append(validate_brackets("((~~)"))
    validation_list.append(validate_legal_symbols("((e~~)"))
    validation_list.append(validate_operators("((~~)"))
    for item in validation_list:
        if item is not True:
            valid = False
            print("-----------------------------------------")
            print(item[1])
            print("-----------------------------------------")


def validate_brackets(expression: str) -> tuple[bool, BracketsNotValid] | bool:
    """
    the function validates brackets
    :param expression: the string expression
    :return: if brackets are valid True
             else False and BracketsNotValid exception Object
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
            stack.pop()
    if len(stack) > 0:
        balanced = False
    if not balanced:
        message = generate_message(expression, problem_index, BracketsNotValid)
        invalidity = BracketsNotValid(message)
        return False, invalidity
    return True


def validate_negation_signs(expression):
    valid = True
    problem_index = 0
    for i in range(len(expression)):
        if expression[i] == negation_sign and expression[i - 1] == negation_sign and i != 0:
            valid = False
        if expression[i] == negation_sign and (expression[i + 1].isdigit() or expression[i + 1] == dot) and \
                i != len(expression - 1):
            problem_index = i - 1
            valid = False
        if not valid:
            break
    if not valid:
        message = "Invalidity Type: Negation sign adjacent to negation sign\n\n" \
                  "Invalid ~ at: \n" \
                  + expression[:problem_index] + "->" + expression[problem_index] + "<-" \
                  + expression[problem_index + 1:len(expression)] \
                  + "\n" + "index of ~: " + str(problem_index)
        return False, message
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
        if not expression[i].isdigit() and expression[i] not in supported_operators:
            valid = False
            problem_index = i
            break
    if not valid:
        message = generate_message(expression, problem_index, SymbolNotRecognized)
        invalidity = SymbolNotRecognized(message)
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
        if i < len(expression) - 1:
            if expression[i + 1] in OPERATION_DICT:
                if OPERATION_DICT[expression[i + 1]].position != "left" and expression[i + 1] != subtraction_sign:
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
            if expression[i + 1].isdigit() is False \
                    and expression[i + 1] != dot and expression[i + 1] != subtraction_sign:
                valid = False
                problem_index = i
    return valid, problem_index


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
        if expression[i - 1].isdigit is True or expression[i - 1] == dot:
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
        if expression[i + 1].isdigit is True or expression[i + 1] == dot:
            valid = False
            problem_index = i
    return valid, problem_index


def generate_message(expression: str, problem_index: int, exception_class: object) -> str:
    """
    the function generates a message for exception
    :param expression: string expression
    :param problem_index: index of problem
    :param exception_class: the class of the exception
    :return: exception message
    """
    if exception_class == BracketsNotValid:
        return "Invalidity Type: Unbalanced brackets\n\n" \
            + "Unbalanced bracket at: \n" \
            + expression[:problem_index] + " -->" + expression[problem_index] + "<-- " \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of bracket: " + str(problem_index)
    elif exception_class == SymbolNotRecognized:
        return "Invalidity Type: Symbol is not recognized\n\n" \
            "Invalid symbol at: \n" \
            + expression[:problem_index] + "->" + expression[problem_index] + "<-" \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of invalid symbol : " + str(problem_index)
    elif exception_class == OperatorsNotPositionedValidly:
        return "Invalidity Type: Operator is not positioned correctly\n\n" \
            "Invalid operator at: \n" \
            + expression[:problem_index] + " ->" + expression[problem_index] + "<- " \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of invalid operator : " + str(problem_index)
    else:
        return "Invalidity Type: Unknown\n\n" \
            "Invalid input at: \n" \
            + expression[:problem_index] + " ->" + expression[problem_index] + "<- " \
            + expression[problem_index + 1:len(expression)] \
            + "\n" + "index of invalid input : " + str(problem_index)


if __name__ == '__main__':
    main()
