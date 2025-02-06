# Ek list banayein jisme alag-alag learning topics store hon (e.g., "Variables", "Data Types", "Control Flow", etc.).

# -----------------List----------------
"""We are using list to store different types of value or data so that we can easily access different values
using indexing"""

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
print(basic_python_topics, end="\n\n")

#Tuple aur dictionary create karein jo mini project ke elements ko represent karein (jaise, feedback: { "topic": "Variables", "status": "Not Started" }).

# ---------------Tuples--------------
# Tuple containing project elements and it is not contain any duplicate element
projectElements = (
    "Project Name",
    "Team Members",
    "Start Date",
    "End Date",
    "Tasks"
)

# Dictionary containing current status on project tasks, and it stores the value in key and value pairs
current_status = {
    "Variables": {"status": "Not Started"},
    "Operators": {"status": "In Progress"},
    "Control Flow Statements": {"status": "Completed"},
    "Functions": {"status": "Not Started"},
    "Lists": {"status": "Completed"}
}

print("Project Elements:", projectElements,end="\n\n")
print("Status on Project Tasks:", current_status)

