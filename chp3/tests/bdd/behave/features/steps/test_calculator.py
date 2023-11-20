import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'util'))

from behave import given, when, then
from calculator import Calculator

@given('I have a calculator')
def step_impl(context):
    context.calc = Calculator()

@when('I enter "{num1}" and "{num2}"')
def step_impl(context, num1, num2):
    context.result = context.calc.add(int(num1), int(num2))

@then('the result should be "{expected_result}"')
def step_impl(context, expected_result):
    assert context.result == int(expected_result)
