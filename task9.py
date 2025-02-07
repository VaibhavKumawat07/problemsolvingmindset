# Learning Implementation of while loop

def while_loop_working():
    # Declare Count Variable
    count = 1

    while True:
        user_input = input(f"({count}) Enter values (type 'exit' to stop): ")

        if user_input.lower() == "exit":
            print("Loop stop successfully! ✅")
            break  # we are using break to stop the loop

        print(f"You entered: {user_input}")
        count += 1  # Increasing the value of count


# while_loop_working()


# Implementing the mini project


def learning_roadmap():
    print("\n🚀 Welcome to Problem Solving Mindset Learning Menu 🚀\n")

    python_topics = ["1. Variables and Data Types", "2. Operators", "3. Control Flow Statements", "4. Functions",
                     "5. Lists", "6. Tuples",
                     "7. Dictionaries", "8. Sets", "9. String Manipulation", "10. File Handling",
                     "11. Exception Handling",
                     "12. Modules and Packages", "13. List Comprehensions", "14. Lambda Functions",
                     "15. Object-Oriented Programming",
                     "16. Regular Expressions", "17. Decorators", "18. Generators"]

    while True:
        print("\n📚 Choose a topic to learn :")
        for topic in python_topics:
            print(topic)

        choice = input(f"\nEnter your choice (1-{len(python_topics)}) or 0 to exit: ")

        if choice == "0":
            print("\n👋 Thank you for using Problem Solving Mindset! Goodbye!\n")
            break
        elif choice in [str(i) for i in range(1, len(python_topics) + 1)]:  # Here we are creating a list that contain
            # number from start to end of the topics using list comprehensions
            print(f"\n📖 You selected: {python_topics[int(choice) - 1]}")
            break
        else:
            print(f"⚠ Invalid choice! Please enter a number between 1-{len(python_topics)} or 0 to exit.")


# Function call to run the menu
learning_roadmap()

# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# This script demonstrates:
# 1. Using of while loop and break statement
# 2. Using learning_roadmap function user can select specific topics to learn
# Happy coding!
