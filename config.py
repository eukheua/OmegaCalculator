from operations import *
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
dot = "."
supported_operations = {addition_sign, subtraction_sign, multiplication_sign, division_sign, exponent_sign, modulo_sign,
                        maximum_sign, minimum_sign, average_sign, negation_sign, factorial_sign, sum_of_digits_sign}
addition = Operator("+", 1, "middle", add)
subtraction = Operator("-", 1, "middle", sub)
multiplication = Operator("*", 2, "middle", mul)
division = Operator("/", 2, "middle", div)
exponent = Operator("^", 3, "middle", power)
modulo = Operator("%", 4, "middle", mod)
maximum = Operator("$", 5, "middle", maximum)
minimum = Operator("&", 5, "middle", minimum)
average = Operator("@", 5, "middle", avg)
negation = Operator("~", 6, "left", neg)
factorial = Operator("!", 6, "right", fac)
sum_of_digits = Operator("#", 6, "right", sum_digits)
OPERATION_DICT = {"+": addition, "-": subtraction, "*": multiplication, "/": division, "^": exponent, "%": modulo,
                  "$": maximum, "&": minimum, "@": average, "~": negation, "!": factorial, "#": sum_of_digits}
