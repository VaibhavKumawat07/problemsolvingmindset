# - Ek program likhe jisme student ke performance ke basis par different messages display ho (e.g.,
# “Needs Improvement”, “Good”, “Excellent”).

# Understanding conditional statements with hel of example

# Initialize score variable with None
score = None
try:
    # Taking value from the user
    score = int(input("Enter student score between 1 to 100 : "))
    print(score)
except ValueError:
    # If the input is not a valid integer, print an error message
    print("Invalid input❌.")

# Check if the score is within the valid range
if 100 >= score >= 1:
    if score == 100:
        # If the score is exactly 100, print "Excellent"
        print("Excellent💯.")
    elif score >= 90:
        # If the score is 90 or more but less than 100, print "Very Good"
        print("Very Good💥.")
    elif score >= 75:
        # If the score is 75 or more but less than 90, print "Good"
        print("Good😊")
    else:
        # If the score is less than 75, print "Bad"
        print("Bad🥺.")
else:
    # If the score is not within the valid range, ask the user to enter a valid score
    print("Please insert valid score ❌.")

# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# This script demonstrates:
# 1. When to use nested conditional statements.
# 2. when and how to handle multiple conditions.
# Happy coding!

