# A lambda function is an anonymous function (without a name) that can take multiple inputs but has only one expression.
#  Syntax :
#  lambda arguments: expression
# Understanding basic function of lambda function

# Normal function to square a number
def square(x):
    return x * x


print(square(5))

# Equivalent Lambda function

square_lambda = lambda x: x * x
print(square_lambda(5))

# Implementing lambda function in mini project

# List of completed topics
completed_topics = ["Variables", "Operators", "Functions", "Tuples"]
total_topics = 18  # Assume we have 18 topics in total

# Calculate progress of a student using lambda function
progress_percentage = lambda completed, total: (len(completed) / total) * 100

print(f"Learning Progress of a student 🧑‍🎓: {progress_percentage(completed_topics, total_topics):.2f}%")


# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# This script demonstrates:
# 1. ✔ lambda keyword is required for implementing lambda function
# 2. ✔ we don't need to use return keyword, it automatically returns the value
# 3. ✔ Used for shorthand and  simple operations
# Happy coding!

