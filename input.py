from calculator import evaluate, print_result


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
        result = evaluate(expression)
        if result is not None:
            print_result(result)
            expression = ""


if __name__ == "__main__":
    main()
