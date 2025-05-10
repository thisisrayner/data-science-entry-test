# q2.py
# Problem: Conditional Logic - Grade Classifier
# Write a Python script that asks the user for a numerical score (0-100) and
# prints the corresponding letter grade based on the following criteria:
# 90-100: A
# 80-89:  B
# 70-79:  C
# 60-69:  D
# 0-59:   F
# Handle invalid scores (e.g., less than 0 or greater than 100).

def classify_grade():
    """
    Asks for a numerical score and prints the corresponding letter grade.
    """
    print("--- Grade Classifier ---")

    try:
        score_str = input("Enter the numerical score (0-100): ")
        score = float(score_str)
    except ValueError:
        print("Invalid input. Score must be a number.")
        return

    # Check for valid score range
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    # Determine the grade using if-elif-else statements
    elif score >= 90:
        grade = "A"
        print(f"The score {score} corresponds to grade: {grade}")
    elif score >= 80: # score is between 80 and 89 (inclusive)
        grade = "B"
        print(f"The score {score} corresponds to grade: {grade}")
    elif score >= 70: # score is between 70 and 79 (inclusive)
        grade = "C"
        print(f"The score {score} corresponds to grade: {grade}")
    elif score >= 60: # score is between 60 and 69 (inclusive)
        grade = "D"
        print(f"The score {score} corresponds to grade: {grade}")
    else: # score is between 0 and 59 (inclusive)
        grade = "F"
        print(f"The score {score} corresponds to grade: {grade}")


if __name__ == "__main__":
    classify_grade()

# Test Cases:
# 1. Score = 95   -> Expected: A
# 2. Score = 82   -> Expected: B
# 3. Score = 70   -> Expected: C
# 4. Score = 69.5 -> Expected: D
# 5. Score = 50   -> Expected: F
# 6. Score = 101  -> Expected: "Invalid score..."
# 7. Score = -5   -> Expected: "Invalid score..."
# 8. Score = "xyz"-> Expected: "Invalid input..."
