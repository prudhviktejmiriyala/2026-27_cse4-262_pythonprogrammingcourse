```python
# University Scholarship Allocation System

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_FAMILY_INCOME = 250000

SUBJECTS = ["Mathematics", "Physics", "Chemistry"]


def evaluate_student(name, marks, attendance, income):
    # Calculate aggregate percentage
    aggregate = sum(marks) / (len(marks) * 100) * 100

    # Check eligibility criteria
    eligible = (
        aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARK for mark in marks)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_FAMILY_INCOME
    )

    return {
        "name": name,
        "marks": marks,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "eligible": eligible
    }


def main():
    students = []

    n = int(input("Enter number of applicants: "))

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}")

        name = input("Student name: ")

        marks = []
        for subject in SUBJECTS:
            mark = float(input(f"Marks in {subject} (out of 100): "))
            marks.append(mark)

        attendance = float(input("Attendance percentage: "))
        income = float(input("Annual family income (Rs.): "))

        student = evaluate_student(
            name, marks, attendance, income
        )
        students.append(student)

    # Filter eligible students
    eligible_students = [
        student for student in students
        if student["eligible"]
    ]

    # Rank by aggregate descending, attendance descending,
    # income ascending, and name alphabetically.
    eligible_students.sort(
        key=lambda student: (
            -student["aggregate"],
            -student["attendance"],
            student["income"],
            student["name"].casefold()
        )
    )

    print("\n========== SCHOLARSHIP RESULTS ==========")

    if not eligible_students:
        print("No students are eligible for the scholarship.")
    else:
        print("Eligible Students (Ranked):\n")

        for rank, student in enumerate(
            eligible_students, start=1
        ):
            print(f"Rank: {rank}")
            print(f"Name: {student['name']}")
            print(
                f"Aggregate: {student['aggregate']:.2f}%"
            )
            print(
                f"Attendance: {student['attendance']:.2f}%"
            )
            print(
                f"Annual Family Income: Rs. "
                f"{student['income']:.2f}"
            )
            print("-" * 35)

    # Display ineligible students
    ineligible_students = [
        student for student in students
        if not student["eligible"]
    ]

    print("\nIneligible Students:")

    if not ineligible_students:
        print("None")
    else:
        for student in ineligible_students:
            print(
                f"{student['name']} - "
                f"Aggregate: {student['aggregate']:.2f}%"
            )


if __name__ == "__main__":
    main()
```
