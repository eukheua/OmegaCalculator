from calculator import evaluate_expression


def print_result(result):
    print("\n\n\n")
    print(result)


def main():
    try:
        expression = input("Pls Enter your mathematical expression: \n")
        result = evaluate_expression(expression)
        print_result(result)
    except RuntimeError as runTimeErr:
        print("\n\nError>>>>>>")
        print(runTimeErr)
    except EOFError as eofError:
        print("\n\nError>>>>>>")
        print(eofError)
    except Exception as exception:
        print("\n\nError>>>>>>")
        print(exception)
    finally:
        print("exiting omega calculator")


if __name__ == "__main__":
    main()
