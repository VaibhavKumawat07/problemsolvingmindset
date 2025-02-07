# Learning topics ki list par for loop chalayein aur har topic ko print karein.

# defining the list of topics

def working_loop():
    basic_python_topics = [
        "Variables and Data Types",
        "Operators",
        "Control Flow Statements",
        "Functions",
        "Lists",
        "Tuples",
        "Dictionaries",
        "Sets",
        "String Manipulation",
        "File Handling",
        "Exception Handling",
        "Modules and Packages",
        "List Comprehensions",
        "Lambda Functions",
        "Object-Oriented Programming",
        "Regular Expressions",
        "Decorators",
        "Generators"
    ]
    # Iterating over topics
    for topics in basic_python_topics:
        print(topics)


# 2.Mini project ke liye topics ke iteration ko implement karein.

def display_learning_roadmap():
    print("\n🚀 Welcome to Problem Solving Mindset Learning Roadmap 🚀\n")
    python_topics = ["1. Variables and Data Types", "2. Operators", "3. Control Flow Statements", "4. Functions",
                     "5. Lists", "6. Tuples",
                     "7. Dictionaries", "8. Sets", "9. String Manipulation", "10. File Handling",
                     "11. Exception Handling",
                     "12. Modules and Packages", "13. List Comprehensions", "14. Lambda Functions",
                     "15. Object-Oriented Programming",
                     "16. Regular Expressions", "17. Decorators", "18. Generators"]

    print("📚 You have to follow each step to learn python :\n")

    for topic in python_topics:
        print("✅", topic)

    print("\n🎯 If you complete this topic you will be the master of python!\n")


display_learning_roadmap()
