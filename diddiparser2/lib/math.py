"""
Math: Math operations for DiddiScript
"""

import math

from diddiparser2.diddiscript_types import Floating, Integer
from diddiparser2.messages import run_error

DIDDISCRIPT_FUNCTIONS = ["sum_operation", "subtraction_operation", "multiplication_operation", "division_operation", "power"]


def check_numbers(*args):
    for arg in args:
        if not isinstance(arg, Floating) and not isinstance(arg, Integer):
            run_error(
              "Expected Floating or Integer DiddiScript types, "
              f"but got {type(arg).__name__}"
            )


def sum_operation(*args):
    """
    An equivalent to the sum operator.
    """
    check_numbers(*args)
    result = 0
    counter = 1
    for arg in args:
        if counter == 1:
            result = arg.value
        else:
            result += arg.value
        counter += 1
    return Floating(result)


def subtraction_operation(*args):
    """
    An equivalent to the subtraction operator.
    """
    check_numbers(*args)
    result = 0
    counter = 1
    for arg in args:
        if counter == 1:
            result = arg.value
        else:
            result -= arg.value
        counter += 1
    return Floating(result)


def multiplication_operation(*args):
    """
    An equivalent to the multiplication operator.
    """
    check_numbers(*args)
    result = 0
    counter = 1
    for arg in args:
        if counter == 1:
            result = arg.value
        else:
            result *= arg.value
        counter += 1
    return Floating(result)


def division_operation(*args):
    """
    An equivalent to the division operator.
    """
    check_numbers(*args)
    result = 0
    counter = 1
    for arg in args:
        if counter == 1:
            result = arg.value
        else:
            try:
                result = result / arg.value
            except ZeroDivisionError:
                run_error(f"Division by zero: '{result} / {arg.value}'")
        counter += 1
    return Floating(result)


def power(num, exp):
    "Get the pow()."
    check_numbers(num, exp)
    return Floating(math.pow(num.value, exp.value))
