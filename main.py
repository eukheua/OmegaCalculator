from validations import *
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print(validate_operators("3*5%2+65/(-47#$-(2+6))"))
    print(validate_operators("5^3-(4*5%34#)"))
    print(validate_operators("-36#*-(-(47#-554#))###"))
    print(validate_operators("2.3#"))
    print(validate_operators("6!#!#!#!#"))
def change(x,y):
    x = x+2
    print(x)
    return x
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
