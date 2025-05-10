# q6.py
# Problem: Functions, Lists, and Dictionaries - Find Max Score
# You are given a list of dictionaries, where each dictionary represents a student
# with a 'name' (string) and a 'score' (integer).
# Write a Python function called `find_top_student` that takes this list
# as input and returns the name of the student with the highest score.
# If multiple students have the same highest score, return the name of the first one encountered.
# If the list is empty, return None.

def find_top_student(students_data):
    """
    Finds the student with the highest score from a list of student dictionaries.

    Args:
        students_data (list of dict): A list where each dictionary has
                                      'name' (str) and 'score' (int) keys.

    Returns:
        str or None: The name of the student with the highest score,
                     or None if the list is empty or invalid.
    """
    if not students_data: # Check if the list is empty
        print("The list of students is empty.")
        return None

    # Initialize with the first student, assuming the list is not empty
    # and has at least one valid student entry.
    top_student_name = None
    max_score = -1 # Initialize with a score lower than any possible score

    found_valid_student = False
    for student in students_data:
        # Basic validation for dictionary structure and types
        if not isinstance(student, dict) or 'name' not in student or 'score' not in student:
            print(f"Skipping invalid student data: {student}")
            continue
        if not isinstance(student['name'], str) or not isinstance(student['score'], int):
            print(f"Skipping student with invalid data types: {student}")
            continue

        found_valid_student = True
        # Compare current student's score with the current max_score
        if student['score'] > max_score:
            max_score = student['score']
            top_student_name = student['name']

    if not found_valid_student: # If no valid students were processed
        print("No valid student data found in the list.")
        return None

    return top_student_name

if __name__ == "__main__":
    print("--- Find Top Student ---")

    students1 = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78},
        {'name': 'David', 'score': 92} # Bob should be returned as he is encountered first
    ]
    top1 = find_top_student(students1)
    print(f"Students: {students1}")
    print(f"Top student: {top1}\n") # Expected: Bob

    students2 = [
        {'name': 'Eve', 'score': 99},
        {'name': 'Frank', 'score': 95}
    ]
    top2 = find_top_student(students2)
    print(f"Students: {students2}")
    print(f"Top student: {top2}\n") # Expected: Eve

    students3 = []
    top3 = find_top_student(students3)
    print(f"Students: {students3}")
    print(f"Top student: {top3}\n") # Expected: None (with "list is empty" message)

    students4 = [
        {'name': 'Grace', 'score': 70}
    ]
    top4 = find_top_student(students4)
    print(f"Students: {students4}")
    print(f"Top student: {top4}\n") # Expected: Grace

    students5 = [
        {'name': 'Ivy', 'score': 'ninety'}, # Invalid score type
        {'name': 'Jack'}, # Missing score
        {'score': 80} # Missing name
    ]
    top5 = find_top_student(students5)
    print(f"Students: {students5}")
    print(f"Top student: {top5}\n") # Expected: None (with skip/invalid messages)

    students6 = [
        {'name': 'Ken', 'score': 88},
        {'name': 'Liam', 'score': 95},
        "Not a dictionary", # Invalid entry
        {'name': 'Mia', 'score': 99}
    ]
    top6 = find_top_student(students6)
    print(f"Students: {students6}")
    print(f"Top student: {top6}\n") # Expected: Mia (with skip message for invalid entry)

# Test Cases:
# 1. [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 95}] -> 'B'
# 2. [{'name': 'C', 'score': 95}, {'name': 'D', 'score': 90}] -> 'C'
# 3. [{'name': 'E', 'score': 80}] -> 'E'
# 4. [] -> None
# 5. [{'name': 'F', 'score': 100}, {'name': 'G', 'score': 100}] -> 'F'
