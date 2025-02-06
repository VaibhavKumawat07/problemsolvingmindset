# python_operators.py
# Practicing Arithmetic, Assignment, Comparison, and Logical Operators

# -----------------------------------------------------
# 1. Arithmetic Operators
# -----------------------------------------------------

# Arithmetic operators for basic mathematics  operations like addition, subtraction etc
num1 = 15
num2 = 4

# Performing arithmetic operations
addition = num1 + num2         # Addition: 15 + 4
subtraction = num1 - num2      # Subtraction: 15 - 4
multiplication = num1 * num2   # Multiplication: 15 * 4
division = num1 / num2         # Division: 15 / 4
floor_division = num1 // num2  # Floor Division: 15 // 4 (integer result)
modulus = num1 % num2          # Modulus: 15 % 4 (remainder)
exponentiation = num1 ** num2  # Exponentiation: 15 ** 4

print("Arithmetic Operations:")
print("Addition:", addition)               # Output: 19
print("Subtraction:", subtraction)         # Output: 11
print("Multiplication:", multiplication)   # Output: 60
print("Division:", division)               # Output: 3.75
print("Floor Division:", floor_division)   # Output: 3
print("Modulus:", modulus)                 # Output: 3
print("Exponentiation:", exponentiation)   # Output: 50625

print("\n----------------------------------------\n")

# -----------------------------------------------------
# 2. Assignment Operators
# -----------------------------------------------------

# Assignment operators to assign and update values and it is shorthand for assigning value to a same variable
score = 45
print("Initial Score:", score)

score += 10  # Equivalent to score = score + 10
print("Score after += 10:", score)  # Output: 55

score -= 5   # Equivalent to score = score - 5
print("Score after -= 5:", score)  # Output: 50

score *= 2   # Equivalent to score = score * 2
print("Score after *= 2:", score)  # Output: 100

score /= 4   # Equivalent to score = score / 4
print("Score after /= 4:", score)  # Output: 25.0

print("\n----------------------------------------\n")

# -----------------------------------------------------
# 3. Comparison Operators
# -----------------------------------------------------

# Comparison operators are used to compare two values
student_score = 68
passing_score = 50

# Checking if student score is greater than passing score
is_pass = student_score > passing_score

print("Comparison Operators:")
print("Student Score:", student_score)
print("Passing Score:", passing_score)
print("Is student score greater than passing score?", is_pass)  # Output: True

# Other comparison examples
print("Is student score equal to passing score?", student_score == passing_score)     # Output: False
print("Is student score not equal to passing score?", student_score != passing_score) # Output: True
print("Is student score less than passing score?", student_score < passing_score)     # Output: False

print("\n----------------------------------------\n")

# -----------------------------------------------------
# 4. Logical Operators
# -----------------------------------------------------

# Logical operators to combine multiple conditions
student_score = 68
attendance = 80  # percentage

# Checking if student score and attendance are sufficient
if student_score > 50 and attendance > 75:
    print("Logical Operators:")
    print("Condition: Student score and attendance are sufficient.")
    print("Result: Pass")  # Output: Pass
else:
    print("Logical Operators:")
    print("Condition: Either student score or attendance is insufficient.")
    print("Result: Fail")

# Another example using 'or'
extra_credit_completed = False
if student_score > 90 or extra_credit_completed:
    print("\nResult: Excellent")  # Output: Needs Improvement
else:
    print("\nResult: Needs Improvement")

# Using 'not' operator to invert condition
print("\nUsing 'not' operator:")
if not (student_score < 50):
    print("Student did not score less than 50.")  # Output: Student did not score less than 50.
else:
    print("Student scored less than 50.")

# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# This script demonstrates:
# 1. Proper understanding of arithmetic operations (addition, subtraction, multiplication, division, etc.).
# 2. Using assignment operators to update variables.
# 3. Comparing values using comparison operators and getting boolean results.
# 4. Combining multiple conditions using logical operators and making decisions based on them.
# Happy coding!
