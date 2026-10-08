# Student Grade Manager
# ---------------------

students = {}


def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    if name in students:
        print("Warning: Student already exists.")
        return

    while True:
        try:
            mark = float(input("Enter mark (0-100): "))

            if mark < 0 or mark > 100:
                print("Error: Mark must be between 0 and 100.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")

    grade = calculate_grade(mark)

    students[name] = {
        "mark": mark,
        "grade": grade
    }

    print(f"Student '{name}' added successfully!")


def display_students():
    if not students:
        print("No students available.")
        return

    print("\n" + "=" * 45)
    print(f"{'Name':<20}{'Mark':<10}{'Grade':<10}")
    print("-" * 45)

    for name, details in students.items():
        print(
            f"{name:<20}"
            f"{details['mark']:<10.2f}"
            f"{details['grade']:<10}"
        )

    print("=" * 45)


def show_statistics():
    if not students:
        print("No student data available.")
        return

    marks = [details["mark"] for details in students.values()]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("\nClass Statistics")
    print("-" * 30)
    print(f"Class Average : {average:.2f}")
    print(f"Highest Mark  : {highest:.2f}")
    print(f"Lowest Mark   : {lowest:.2f}")


def main():
    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Show Class Statistics")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            show_statistics()

        elif choice == "4":
            print("Thank you for using Student Grade Manager!")
            break

        else:
            print("Error: Invalid choice. Please select 1-4.")


# Start the program
main()