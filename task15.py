# In this task we will learn about IO operation in file
# Function to save student progress in a file
def save_student_progress(student_name, topic, status):
    with open("student_progress.txt", "a") as file:
        file.write(f"{student_name},{topic},{status}\n")
    print("Progress saved successfully!\n")


# Function to read and display student progress
def read_student_progress():
    try:
        with open("student_progress.txt", "r") as file:
            print("\nStudent Progress Report:")
            print("-------------------------------")
            for line in file:
                student_name, topic, status = line.strip().split(",")
                print(f"Student: {student_name}, Topic: {topic}, Status: {status}")
    except FileNotFoundError:
        print("No progress data found. Start learning!\n")


# Mini Project  – Tracking Learning Progress
def student_progress_tracker():
    while True:
        print("\nStudent Progress Tracker")
        print("1. Save Progress")
        print("2. View Progress")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_name = input("Enter your name: ")
            topic = input("Enter the topic you learned: ")
            status = input("Enter completion status (Completed/In Progress): ")
            save_student_progress(student_name, topic, status)
        elif choice == "2":
            read_student_progress()
        elif choice == "3":
            print("Exiting Student Progress Tracker. Happy Learning! 😊")
            break
        else:
            print("Invalid choice! Please enter a valid option.\n")



student_progress_tracker()

# -----------------------------------------------------
# Summary:
# -----------------------------------------------------
# ✔ Writing data to a file: Save student progress.
# ✔ Reading data from a file: Display learning status.
# ✔ Mini Project Use Case: Track student progress using File I/O.
# ✔ Error Handling: FileNotFoundError is handled if no progress file exists.
# Happy coding!
