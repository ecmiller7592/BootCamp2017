# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(1,1) == 2, "Addition failed on positive integers"
    pass

def test_smallest_factor():
    assert soln.smallest_factor(1) == 1, "Failed for 1"
    assert soln.smallest_factor(2) == 2, "Failed for smallest prime (2)"
    assert soln.smallest_factor(17) == 17, "Failed for larger prime (17)"
    assert soln.smallest_factor(18) == 2, "Failed for non-two smallest factor (18)"
    pass

# Problem 2: Test the operator function from solutions.py
def test_operator():
    assert soln.operator(2,1,'+') == 3, 'Failed Addition'
    assert soln.operator(2,1,'*') == 2, 'Failed Multiplication'
    assert soln.operator(2,1,'-') == 1, 'Failed Subtraction'
    assert soln.operator(2,1,'/') == 2, 'Failed Qualified Division'

    with pytest.raises(Exception) as specerror:
        soln.operator(4,0,'p')
    assert specerror.typename == 'ValueError'
    assert specerror.value.args[0] == "Oper can only be: '+', '/', '-', or '*'"

    with pytest.raises(Exception) as lengtherror:
        soln.operator(4,0,'++')
    assert lengtherror.typename == 'ValueError'
    assert lengtherror.value.args[0] == "Oper should be one character"

    with pytest.raises(Exception) as strerror:
        soln.operator(4,0,3)
    assert strerror.typename == 'ValueError'
    assert strerror.value.args[0] == "Oper should be a string"

    with pytest.raises(Exception) as diverror:
        soln.operator(4,0,'/')
    assert diverror.typename == 'ValueError'
    assert diverror.value.args[0] == "You can't divide by zero!"
    pass

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_subtraction(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4,-3)
    assert number_1 - number_3 == soln.ComplexNumber(-1,-7)
    assert number_2 - number_3 == soln.ComplexNumber(3,-4)
    assert number_3 - number_3 == soln.ComplexNumber(0,0)

def test_complex_division(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    with pytest.raises(Exception) as diverror:
        number_1 / soln.ComplexNumber(0,0)
    assert diverror.typename == 'ValueError'
    assert diverror.value.args[0] == "Cannot divide by zero"

    assert number_1 / number_3 == soln.ComplexNumber(4/17, -1/17)
    assert number_2 / number_3 == soln.ComplexNumber(11/17,-7/17)

def test_complex_equality(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 != number_2
    assert number_1 == number_1
def test_complex_string(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert str(number_1) == "1+2i"
    assert str(soln.ComplexNumber(2,-2)) == "2-2i"
def test_complex_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert soln.ComplexNumber(3,1).norm() < 800

def set_tester():
    assert soln.Setg.matchpicker(12,"set.txt") == 178

    with pytest.raises(Exception) as numerror:
        soln.Setg.matchpicker(12,"g.txt")
    assert numerror.typename == 'ValueError'
    assert numerrorr.value.args[0] == "Not a valid card sorting"

    with pytest.raises(Exception) as namerr:
        soln.Setg.matchpicker(12,"fake.txt")
    assert namerr.typename == 'NameError'
    assert namerr.value.args[0] == "Not a valid file"
# Problem 4: Write test cases for the Set game.
