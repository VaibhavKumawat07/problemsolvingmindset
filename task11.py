# Implementing Function to Add Two Numbers (Parameters & Return Value)
def add(a, b):
    return a + b


# Function Call
# result = add(5, 10)
# print("Sum:", result)


# Understanding the concept Local vs Global Scope with the help of an example

global_var = "I am global variable"


def check_variable_scope():
    local_var = "I am local variable"
    print(local_var)  # Accessible inside the function
    print(global_var)  # Accessible inside the function


# check_variable_scope()

# print(local_var)  # ❌ Error: local_var is not defined outside the function
# print(global_var)  # ✅ Accessible outside


# Implementing function for mini-project (Processing User Score)

# Global variable to store total progress score
total_score = 0


def update_student_score(points):
    global total_score  # Using the global variable
    total_score += points
    return total_score


# Function Calls
print("Initial Score of student:", total_score)
print("Score after completing 'Lambda Function':", update_student_score(10))
print("Score after completing 'File Handling':", update_student_score(15))


# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# This script demonstrates:
# 1. ✔ Function with parameters (a, b)
# 2. ✔ Return value (a + b)
# 3. ✔ Local Variable: Defined inside a function, cannot be used outside.
# 4. ✔ Global Variable: Defined outside a function, accessible everywhere.
# Happy coding!
