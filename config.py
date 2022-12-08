from operations import add, sub, mul, div, power, mod, maximum, minimum, avg, neg, fac, sum_digits, Operator

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
unary_minus = Operator("u-", 6, "left", neg)
OPERATION_DICT = {"+": addition, "-": subtraction, "*": multiplication, "/": division, "^": exponent, "%": modulo,
                  "$": maximum, "&": minimum, "@": average, "~": negation, "!": factorial, "#": sum_of_digits,
                  "u-": unary_minus}
OPERATION_ORDER_DICT = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "$": 5, "&": 5, "@": 5, "~": 6, "!": 6}
OPERATORS_STRING = "+-*/^%$&@~!"
SUPPORTED_BRACKETS = "()"
DIGITS = "0123456789"

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
unary_minus_sign = 'u-'
dot = "."

supported_operations = {addition_sign, subtraction_sign, multiplication_sign, division_sign, exponent_sign, modulo_sign,
                        maximum_sign, minimum_sign, average_sign, negation_sign, factorial_sign, sum_of_digits_sign}

#  includes all supported characters excluding numbers
supported_operators = supported_operations.union(open_bracket, closed_bracket)

supported_operators_plus = supported_operations.union(open_bracket)
