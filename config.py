from operations import *


# constants of all operators and symbols used
open_bracket = '('
closed_bracket = ')'
addition_sign = '+'
subtraction_sign = '-'
multiplication_sign = '*'
division_sign = '/'
exponent_sign = '^'
modulo_sign = '%'
maximum_sign = '$'
minimum_sign = '&'
average_sign = '@'
negation_sign = '~'
factorial_sign = '!'
sum_of_digits_sign = "#"
# unary minus is a representation of the negation - when it can't be forced into a number it isn't a legal input
unary_minus_sign = 'u-'
dot = "."

# creating all the Operator types which shall be used to represent the operators
addition = Operator(addition_sign, 1, "middle", add)
subtraction = Operator(subtraction_sign, 1, "middle", sub)
multiplication = Operator(multiplication_sign, 2, "middle", mul)
division = Operator(division_sign, 2, "middle", div)
exponent = Operator(exponent_sign, 3, "middle", power)
modulo = Operator(modulo_sign, 4, "middle", mod)
maximum = Operator(maximum_sign, 5, "middle", maximum)
minimum = Operator(minimum_sign, 5, "middle", minimum)
average = Operator(average_sign, 5, "middle", avg)
negation = Operator(negation_sign, 6, "left", neg)
factorial = Operator(factorial_sign, 6, "right", fac)
sum_of_digits = Operator(sum_of_digits_sign, 6, "right", sum_digits)
unary_minus = Operator(unary_minus_sign, 6, "left", neg)
# creating the dictionary that will give me quick access to the attributes of each operator
OPERATION_DICT = {"+": addition, "-": subtraction, "*": multiplication, "/": division, "^": exponent, "%": modulo,
                  "$": maximum, "&": minimum, "@": average, "~": negation, "!": factorial, "#": sum_of_digits,
                  "u-": unary_minus}
# all the supported operations
supported_operations = {addition_sign, subtraction_sign, multiplication_sign, division_sign, exponent_sign, modulo_sign,
                        maximum_sign, minimum_sign, average_sign, negation_sign, factorial_sign, sum_of_digits_sign}

# all the supported operations including the supported kind of bracket
supported_operators = supported_operations.union(open_bracket, closed_bracket)
