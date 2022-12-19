import pytest
from calculator import evaluate
from exceptions import *
from validations import *


# 1-13 simple tests
def test_1():
    assert evaluate("1+1") == 2.0


def test_2():
    assert evaluate("55-4") == 51.0


def test_3():
    assert evaluate("-4*3") == -12.0


def test_4():
    assert evaluate("12/3") == 4.0


def test_5():
    assert evaluate("5^3") == 125.0


def test_6():
    assert evaluate("100%3") == 1.0


def test_7():
    assert evaluate("40$-13") == 40.0


def test_8():
    assert evaluate("50&3") == 3.0


def test_9():
    assert evaluate("32@2") == 17.0


def test_10():
    assert evaluate("~45") == -45.0


def test_11():
    assert evaluate("6!") == 720.0


def test_12():
    assert evaluate("5467#") == 22.0


def test_13():
    assert evaluate("-(2)^3") == -8.0


def test_14():
    assert evaluate("100%3+54#") == 10.0


def test_15():
    assert evaluate("4!#!") == 720.0


# nonsense test
def test_16():
    assert evaluate("$#%DFGDFTGGWRYT$y\t\0sdfsdf52432dfds") is None
    error1 = validate_legal_symbols("$#%DFGDFTGGWRYT$y\t\0sdfsdf52432dfds")
    assert error1[0] is False
    assert type(error1[1]) == SymbolNotRecognized
    error2 = validate_operators("$#%DFGDFTGGWRYT$y\t\0sdfsdf52432dfds")
    assert error2[0] is False
    assert type(error2[1]) == OperatorsNotPositionedValidly


# empty word test
def test_17():
    assert evaluate("") is None


# white chars test
def test_18():
    assert evaluate("\t\n\n\n\n   \t\t\n") is None


# 19-39 complex tests
def test_19():
    assert evaluate("3*5%2+65/(-47#$-(2+6))") == -5.125


def test_20():
    assert evaluate("-36#*-(-(47#-554#))###") == 27.0


def test_21():
    assert evaluate("(5^3-(4*5%34#))^2+5!$1111") == 12136.0


def test_22():
    assert evaluate("-8+(-(54)#@65)/5!%~42") == -12.666666666666668


def test_23():
    assert evaluate("(654*4)$99^3/5!#!#-~23") == 2983746839.0


def test_24():
    assert evaluate("1--(4+3/5%3+(-(4+3-2)))") == 1.5


def test_25():
    assert evaluate("-(4+6)*756#--8^4-(555#)") == -4291.0


def test_26():
    assert evaluate("(6+(-5#-4$6)#)/(((-2)^4)&(5%3))") == 2.0


def test_27():
    assert evaluate("5*3---(4-~66#^4*4)@12^3!") == 5.090743258738076e+27


def test_28():
    assert evaluate("(6!#!#-5!#!#)/60%43*(3-5)") == -2.4705882352941178


def test_29():
    assert evaluate("-~5!# * 3 @ 1 + -1 ^ 4 + ((2)) * ((4 ^ -~-2.00)) ") == 7.125


def test_30():
    with pytest.raises(Exception) as e:
        evaluate("2---3! + 4!-~3 - 09 * 0.001 * 10 ^ 3 * (2-1)")
        assert e.type == FactorialOnNegativeNumber


def test_31():
    assert evaluate("(4*------ --9 /(2&4)^2!) -100^3 ") == -999991.0


def test_32():
    assert evaluate("~17$30*3.3&5.5-(12#-2!)") == 98.0


def test_33():
    assert evaluate("(5%2+300@10)-    3^2/9+55&3") == 158.0


def test_34():
    assert evaluate("30*0.1$2--~5+(10!*2-30)%5-(30/5+1)") == 48.0


def test_35():
    assert evaluate("(5+6-7*8+9^2)/2-38&36+(10 @2---10#)*~1") == -23.0


def test_36():
    assert evaluate("6!-3^3*2+  (~2/~1+2#)*1-3%2+1") == 670.0


def test_37():
    assert evaluate("100&99/33+1.1^2-(3!+~1)%2+7*7") == 52.21


def test_38():
    assert evaluate("13%2+(6!$50+(3+3+2^5)+~1)-5.5") == 752.5


def test_39():
    assert evaluate("5$(4*-123#^2 /12.7@5.3)-100%(12*2.5)") == 6.0


def test_40():
    assert evaluate("(5+6-7*8+9^2)/2-38&36+(10 @2---10#)*~1") == -23.0


# 41 - 44 simple syntax errors
def test_41():
    error = validate_legal_symbols("6^3e")
    assert error[0] is False
    assert type(error[1]) == SymbolNotRecognized


def test_42():
    error = validate_operators("4~~5")
    assert error[0] is False
    assert type(error[1]) == OperatorsNotPositionedValidly


def test_43():
    error = validate_brackets_balance("(4.5+4))")
    assert error[0] is False
    assert type(error[1]) == BracketsNotBalanced


def test_44():
    error = validate_brackets_not_empty("4..5+4-()")
    assert error[0] is False
    assert type(error[1]) == EmptyBrackets
