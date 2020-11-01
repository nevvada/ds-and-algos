"""
https://edabit.com/challenge/aoN2XoAfQzPQeRNRt

Operations
Write a function that does the following things: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge, the variable will be defined for you. All you have to do is look at the variable, do some string to integer conversions use some if conditionals, and combine them based on the operation.

The numbers and operation will be given as a string, and you should return the value as a string as well.

Examples
operation("1", "2", "add" ) ➞ "3"

operation("4", "5", "subtract") ➞ "-1"

operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as a string, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide go ahead and round down to an integer.
"""

# First approach
def operation(num1, num2, op):
  op_dict = {
    "add": "+",
    "divide": "/",
    "multiply": "*",
    "subtract": "-",
  }

  try:
    expression = "{} {} {}".format(num1, op_dict[op], num2)
    return str(round(eval(expression)))

  except ZeroDivisionError:
    return "undefined"

# Second approach
def operation_2(num1, num2, op):
  op_dict = {
    "add": "+",
    "divide": "/",
    "multiply": "*",
    "subtract": "-",
  }

  try:
    return str(round(eval(num1 + op_dict[op] + num2)))
  except:
    return "undefined"