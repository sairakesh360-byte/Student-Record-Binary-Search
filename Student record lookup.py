# ============================================================
#          STUDENT RECORD LOOKUP SYSTEM
#                 USING BINARY SEARCH
# ============================================================

import random


# ------------------------------------------------------------
# GENERATE STUDENT RECORDS
# ------------------------------------------------------------

def generate_students(number_of_students):

    students = []

    branches = ["CSE", "ECE", "IT", "EEE", "MECH"]

    for i in range(number_of_students):

        student = {
            "roll": 1001 + i,
            "name": f"Student_{i + 1}",
            "branch": random.choice(branches),
            "marks": random.randint(50, 100)
        }

        students.append(student)

    return students


# ------------------------------------------------------------
# BINARY SEARCH
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# CREATE STUDENT RECORDS
# ------------------------------------------------------------

NUMBER_OF_STUDENTS = 10000

print("=" * 70)
print("             STUDENT RECORD LOOKUP SYSTEM")
print("                    USING BINARY SEARCH")
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


# ------------------------------------------------------------
# CONTINUOUS MULTIPLE SEARCH
# ------------------------------------------------------------

while True:

    print("\n" + "=" * 70)

    number_of_searches = int(
        input("Enter number of roll numbers to search (0 to exit): ")
    )

    # Exit condition
    if number_of_searches == 0:

        print("\nThank you! Program ended.")
        break

    if number_of_searches < 0:

        print("\nPlease enter a positive number.")
        continue


    # --------------------------------------------------------
    # OPERATION ANALYSIS VARIABLES
    # --------------------------------------------------------

    total_operations = 0
    successful_searches = 0
    failed_searches = 0


    # --------------------------------------------------------
    # SEARCH MULTIPLE ROLL NUMBERS
    # --------------------------------------------------------

    for i in range(number_of_searches):

        print("\n" + "-" * 70)

        target_roll = int(
            input(f"Enter roll number {i + 1}: ")
        )

        result, operations = binary_search(
            students,
            target_roll
        )

        total_operations += operations


        # ----------------------------------------------------
        # STUDENT FOUND
        # ----------------------------------------------------

        if result:

            successful_searches += 1

            print("\n" + "=" * 70)
            print("                    STUDENT FOUND")
            print("=" * 70)

            print(f"Roll Number : {result['roll']}")
            print(f"Name        : {result['name']}")
            print(f"Branch      : {result['branch']}")
            print(f"Marks       : {result['marks']}")
            print(f"Operations  : {operations}")

            print("=" * 70)


        # ----------------------------------------------------
        # STUDENT NOT FOUND
        # ----------------------------------------------------

        else:

            failed_searches += 1

            print("\n" + "=" * 70)
            print("                  STUDENT NOT FOUND")
            print("=" * 70)

            print(f"Roll Number : {target_roll}")
            print(f"Operations  : {operations}")

            print("=" * 70)


    # --------------------------------------------------------
    # CALCULATE AVERAGE
    # --------------------------------------------------------

    average_operations = (
        total_operations / number_of_searches
    )


    # --------------------------------------------------------
    # SEARCH ANALYSIS
    # --------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("                    SEARCH ANALYSIS")
    print("=" * 70)

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

    print("=" * 70)

    print("\nBinary Search Complexity:")
    print("Best Case    : O(1)")
    print("Average Case : O(log n)")
    print("Worst Case   : O(log n)")
    print("Space        : O(1)")

    print("=" * 70)

    print("\nYou can search again.")
