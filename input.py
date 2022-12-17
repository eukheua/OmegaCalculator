from calculator import *
from validations import *

# fix ()


def main():
    running = True
    expression = ""
    while running is True:
        try:
            expression = input("Pls Enter your mathematical expression: \n")
        except EOFError as eofError:
            print("\n\nError>>>>>>")
            print(eofError.__class__.__name__)
            print("exiting due to EOF input")
            running = False
        except KeyboardInterrupt as k_b_i:
            print("\n\nError>>>>>>")
            print(k_b_i.__class__.__name__)
            print("exiting due to keyboard interrupt")
            running = False
        finally:
            if running:
                print("receiving input was successful moving on>>>")
            else:
                running = False
                exit(0)
        expression = clean_white_chars(expression)
        if not assert_validations(expression):
            continue
        expression = convert_string_expression_to_list(expression)
        expression = convert_infix_to_postfix(expression)
        try:
            result = calculate_postfix(expression)
            print_result(result)
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
        finally:
            expression = ""
            print("\nreached finally block looping again\n")


if __name__ == "__main__":
    main()
