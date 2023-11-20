import sys
import os
import pytest
#sys.path.append('D:/devworkspace/python-ency/chp3/tests/bdd/util')
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'util'))
from calculator import Calculator
from pytest_bdd import scenario, given, when, then, parsers



@scenario('../features/calculator.feature','Add two numbers')
def test_add():
    print(sys.path.append(os.path.dirname(os.path.dirname(__file__))+'util'))
    pass

@pytest.fixture
@given("I have a calculator")
def calculator():
    return Calculator()

@when(parsers.parse('I enter "{a}" and "{b}"'))
def enter_numbers(calculator, a, b):
    calculator.a = int(a)
    calculator.b = int(b)

@then(parsers.parse('the result should be "{result}"'))
def verify_result(calculator, result):
    assert calculator.add(calculator.a, calculator.b) == int(result)