# ============================================================
#          STUDENT RECORD SEARCHING SYSTEM
#                 USING BINARY SEARCH
# ============================================================

import random


# ============================================================
# GENERATE STUDENT RECORDS
# ============================================================

def generate_students(number_of_students):

    students = []

    for i in range(number_of_students):

        student = {
            "roll": 1001 + i,
            "name": f"Student_{i + 1}",
            "branch": random.choice(
                ["CSE", "ECE", "IT", "EEE", "MECH"]
            ),
            "marks": random.randint(50, 100)
        }

        students.append(student)

    return students


# ============================================================
# BINARY SEARCH
# ============================================================

def binary_search(students, target_roll):

    low = 0
    high = len(students) - 1
    operations = 0

    while low <= high:

        operations += 1

        mid = (low + high) // 2

        if students[mid]["roll"] == target_roll:

            return students[mid], operations

        elif students[mid]["roll"] < target_roll:

            low = mid + 1

        else:

            high = mid - 1

    return None, operations


# ============================================================
# CREATE 10,000 STUDENT RECORDS
# ============================================================

NUMBER_OF_STUDENTS = 10000

print("=" * 70)
print("          STUDENT RECORD SEARCHING SYSTEM")
print("                 USING BINARY SEARCH")
print("=" * 70)

print("\nGenerating student records...")

students = generate_students(NUMBER_OF_STUDENTS)

# Binary Search requires sorted records
students.sort(key=lambda student: student["roll"])

print(
    f"{NUMBER_OF_STUDENTS} student records generated successfully!"
)

print(
    f"Roll Number Range: "
    f"{students[0]['roll']} - {students[-1]['roll']}"
)


# ============================================================
# CONTINUOUS MULTIPLE SEARCH
# ============================================================

while True:

    print("\n")

    number_of_searches = int(
        input("Enter number of roll numbers to search: ")
    )

    # Enter 0 to exit
    if number_of_searches == 0:

        print("\nProgram ended.")
        break

    # Check for invalid negative number
    if number_of_searches < 0:

        print("\nPlease enter a positive number.")
        continue


    # ========================================================
    # OPERATION TRACKING
    # ========================================================

    total_operations = 0

    successful_searches = 0

    failed_searches = 0

    operation_counts = []


    # ========================================================
    # SEARCH RESULT TABLE
    # ========================================================

    print("\n" + "-" * 70)

    print(
        f"{'Roll Number':<15}"
        f"{'Result':<15}"
        f"{'Name':<20}"
        f"{'Operations'}"
    )

    print("-" * 70)


    # ========================================================
    # SEARCH MULTIPLE ROLL NUMBERS
    # ========================================================

    for i in range(number_of_searches):

        target_roll = int(
            input(f"Enter roll number {i + 1}: ")
        )

        result, operations = binary_search(
            students,
            target_roll
        )

        # Store operation count
        operation_counts.append(operations)

        # Add to total
        total_operations += operations


        # ----------------------------------------------------
        # STUDENT FOUND
        # ----------------------------------------------------

        if result:

            successful_searches += 1

            print(
                f"{target_roll:<15}"
                f"{'Found':<15}"
                f"{result['name']:<20}"
                f"{operations}"
            )


        # ----------------------------------------------------
        # STUDENT NOT FOUND
        # ----------------------------------------------------

        else:

            failed_searches += 1

            print(
                f"{target_roll:<15}"
                f"{'Not Found':<15}"
                f"{'-':<20}"
                f"{operations}"
            )


    # ========================================================
    # CALCULATE OPERATION STATISTICS
    # ========================================================

    average_operations = (
        total_operations / number_of_searches
    )

    minimum_operations = min(operation_counts)

    maximum_operations = max(operation_counts)


    # ========================================================
    # DISPLAY SEARCH ANALYSIS
    # ========================================================

    print("-" * 70)

    print("\nSEARCH OPERATION COMPARISON")

    print("-" * 70)

    print(
        f"Total Student Records          : "
        f"{NUMBER_OF_STUDENTS}"
    )

    print(
        f"Total Roll Number Searches     : "
        f"{number_of_searches}"
    )

    print(
        f"Successful Searches            : "
        f"{successful_searches}"
    )

    print(
        f"Failed Searches                : "
        f"{failed_searches}"
    )

    print(
        f"Total Binary Search Operations : "
        f"{total_operations}"
    )

    print(
        f"Average Operations per Search  : "
        f"{average_operations:.2f}"
    )

    print(
        f"Minimum Operations             : "
        f"{minimum_operations}"
    )

    print(
        f"Maximum Operations             : "
        f"{maximum_operations}"
    )

    print("-" * 70)

    # The program automatically returns
    # to "Enter number of roll numbers to search:"
