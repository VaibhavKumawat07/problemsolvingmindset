#  Understanding Modules
# A module is simply a Python file (.py) that contains reusable code such as functions, variables, and classes.
# We can add module using import keyword

# Using math module
import math
import datetime


def math_module():
    # Finding square root
    print("Square of a number : ", math.sqrt(25))

    # Finding factorial
    print("Factorial of a number : ", math.factorial(5))


def date_time_module():
    # Give current date and time
    now = datetime.datetime.now()
    print("Current Date & Time:", now)

    # Format date
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted Date:", formatted_date)


# Importing modules for mini project

import task10 as learning

learning.greeting_function()
learning.display_menu()

# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# This script demonstrates:
# 1. ✔ Built-in Modules – math, datetime for ready-to-use functionality
# 2. ✔ User-Defined Modules – Organize your code into multiple files
# 3. ✔ Importing Methods – import module_name or from module import function
# 4. ✔ Mini Project Use Case – Organize learning resources efficiently
# Happy coding!