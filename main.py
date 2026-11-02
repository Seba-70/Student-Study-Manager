courses = []
tasks = []


# 1. Show Main Menu
def show_menu():
    print("\n===== Student Study Manager =====")
    print("1. Add Course")
    print("2. View Courses")
    print("3. Add Task")
    print("4. View Tasks")
    print("5. Update Task Status")
    print("6. Exit")


# 2. Add Course
def add_course():
    course_name = input("Enter course name: ").strip()

    if not course_name:
        print("Course name cannot be empty.")

    elif course_name in courses:
        print("This course already exists.")

    else:
        courses.append(course_name)
        print("Course added successfully!")


# 3. View Courses
def view_courses():
    if not courses:
        print("No courses added yet.")

    else:
        print("\nYour Courses:")

        for course in courses:
            print("-", course)


# 4. Add Task
def add_task():
    if not courses:
        print("Please add a course first.")

    else:
        print("\nAvailable Courses:")

        for i, course in enumerate(courses, 1):
            print(f"{i}. {course}")

        course_choice = input("Choose a course number: ")

        if not course_choice.isdecimal() or not 1 <= int(course_choice) <= len(courses):
            print("Invalid course number.")

        else:
            task_name = input("Enter task name: ").strip()

            if not task_name:
                print("Task name cannot be empty.")

            else:
                task = {
                    "name": task_name,
                    "course": courses[int(course_choice) - 1],
                    "status": "To Do"
                }

                tasks.append(task)

                print("Task added successfully!")


# 5. View Tasks
def view_tasks():
    if not tasks:
        print("No tasks added yet.")

    else:
        print("\nYour Tasks:")

        for i, task in enumerate(tasks, 1):
            print(f"\nTask {i}")
            print("Name:", task["name"])
            print("Course:", task["course"])
            print("Status:", task["status"])


# 6. Update Task Status
def update_task_status():
    if not tasks:
        print("No tasks available to update.")

    else:
        print("\nYour Tasks:")

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']} - {task['status']}")

        task_choice = input("Choose a task number: ")

        if not task_choice.isdecimal() or not 1 <= int(task_choice) <= len(tasks):
            print("Invalid task number.")

        else:
            print("\nSelect New Status:")
            print("1. To Do")
            print("2. In Progress")
            print("3. Completed")

            status_choice = input("Choose status (1-3): ")

            statuses = {
                "1": "To Do",
                "2": "In Progress",
                "3": "Completed"
            }

            if status_choice in statuses:
                selected_task = tasks[int(task_choice) - 1]

                selected_task["status"] = statuses[status_choice]

                print("Task status updated successfully!")

            else:
                print("Invalid status.")


# Main Program
while True:

    show_menu()

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_course()

    elif choice == "2":
        view_courses()

    elif choice == "3":
        add_task()

    elif choice == "4":
        view_tasks()

    elif choice == "5":
        update_task_status()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1-6.")