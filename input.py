from calculator import evaluate, print_result
from exceptions import print_exception


def print_entrance_message() -> None:
    """
    this functions prints the entrance message
    :return: None
    """
    print("Hello, and welcome to the omega calculator.\n"
          "This program receives a mathematical expression from the user and returns the result.\n"
          "The program supports the well known operators and some that are unique to the Omega Calculator:\n"
          "+: Addition\n"
          "-: Subtraction\n"
          "*: Multiplication\n"
          "/: Division\n"
          "^: Exponent\n"
          "%: Modulu\n"
          "$: Max\n"
          "&: Min\n"
          "@: Average\n"
          "~: Negation\n"
          "!: Factorial\n"
          "#: SumOfDigits\n"
          "The program also supports the brackets (), the decimal point and the minus as a sign\n"
          "To exit the program pls type and EOF input or use a specific keyboard interrupt for terminating the run\n"
          "These are all the instructions enjoy!!!\n")


def start_calculator() -> None:
    """
    activates the calculator
    :return: None
    """
    running = True
    expression = ""
    print_entrance_message()
    while running is True:
        try:
            expression = input("Pls enter your mathematical expression: \n")
        except EOFError as eofError:
            print_exception(eofError)
            running = False
        except KeyboardInterrupt as k_b_i:
            print_exception(k_b_i)
            running = False
        finally:
            if not running:
                running = False
                exit(0)
        result = evaluate(expression)
        if result is not None:
            print_result(result)
            expression = ""

