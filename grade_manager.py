
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


def add_student(students):
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    try:
        mark = float(input("Enter student mark (0-100): "))

        if not 0 <= mark <= 100:
            print("Error: Mark must be between 0 and 100.")
            return

    except ValueError:
        print("Error: Please enter a valid numeric mark.")
        return

    student = {
        "name": name,
        "mark": mark,
        "grade": calculate_grade(mark)
    }

    students.append(student)

    print(f"Student '{name}' added successfully!")


def show_students(students):
    if not students:
        print("\nNo student records available.")
        return

    print("\n" + "=" * 55)
    print("                 STUDENT GRADE REPORT")
    print("=" * 55)

    print(f"{'No.':<6}{'Name':<25}{'Mark':>10}{'Grade':>12}")
    print("-" * 55)

    for index, student in enumerate(students, start=1):
        print(
            f"{index:<6}"
            f"{student['name']:<25}"
            f"{student['mark']:>10.2f}"
            f"{student['grade']:>12}"
        )

    print("-" * 55)

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"\nTotal Students : {len(students)}")
    print(f"Class Average : {average:.2f}")
    print(f"Highest Mark  : {highest:.2f}")
    print(f"Lowest Mark   : {lowest:.2f}")

    print("=" * 55)


def main():
    students = []

    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            print("\nThank you for using Student Grade Manager!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
