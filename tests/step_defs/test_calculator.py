from pytest_bdd import given,when,then,scenario
from . import Calculator

scenario('../features/calculator.feature')

@given("I have a calculator")
def calculator():
    return Calculator()

@when("I add 2 and 5")
def add():
    return calculator().add(2,5)

@then("the result should be 7")
def result():
    assert add() == 7

calculator();  