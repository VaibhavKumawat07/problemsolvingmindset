# Learning how we ca handle error using try-except

# Basic try-catch

def basic_try_except():
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Invalid input! Please enter a valid number.")


# In this we learn about how to handle multiple errors

def handle_multiple_exception():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2  #
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


# In this we learn about finally

def try_except_finally():
    try:
        file = open("sample.txt", "r")  # Trying to open a file
        content = file.read()
        print(content)

    except FileNotFoundError:
        print("Error: File not found.")

    finally:
        print("Execution completed.")  # This will always run


# Implementing in mini project by taking student feedback

def student_feedback():
    student_name = input("Enter your name: ")
    college_name = input("Enter your college name: ")

    while True:
        try:
            rating = int(input("Rate your learning experience (1-5): "))
            if 1 <= rating <= 5:
                break  # Exit loop if rating is valid
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid rating. Please enter a number between 1 and 5.")

    feedback_text = input("Enter your feedback: ")

    feedback_data = {
        "name": student_name,
        "college": college_name,
        "rating": rating,
        "feedback": feedback_text
    }
    return feedback_data

# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# This script demonstrates:
# 1. ✔ Basic try-except: Handling invalid user inputs.
# 2. ✔ Multiple exception handling: Managing different types of errors.
# 3. ✔ try-except-finally: Ensuring execution of important cleanup code.
# 4. ✔ Mini Project Use Case: Implementing error handling in a student feedback system.
# Happy coding!