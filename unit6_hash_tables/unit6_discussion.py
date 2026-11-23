"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    print("\n=== INSERT OPERATIONS ===")
    # Creating an empty dictionary to store student scores.
    student_scores = {}
    # Adding five student IDs (keys) and their scores (values).
    student_scores[1001] = 85
    student_scores[1002] = 92
    student_scores[1003] = 78
    student_scores[1004] = 90
    student_scores[1005] = 88
    # Python dictionaries use hashing to organize key-value pairs. Each unique key is associated with a value, allowing
    # efficient retrieval without searching every entry.

    # Displaying all student IDs and their corresponding scores.
    print("Student scores:", student_scores)

    print("\n=== LOOKUP OPERATIONS ===")
    # Retrieve the scores for two existing student IDs.
    # The get() method searches for a key and returns its associated value
    score_1002 = student_scores.get(1002)
    score_1004 = student_scores.get(1004)

    # Displaying the results of both successful lookups.
    print("Student 1002's score:", score_1002)
    print("Student 1004's score:", score_1004)

    print("\n=== UPDATE OPERATIONS ===")
    # Display the dictionary before updating a student' score.
    print("Before update:", student_scores)
    # Update student 1003's score from 78 to 86. Assigning a new value to an existing key replaces the old value.
    # The dictionary doesn't create a duplicate key.
    student_scores[1003] = 86

    # Displaying the dictionary after updating the student's score.
    print("After update:", student_scores)

    print("\n=== DELETE OPERATIONS ===")
    # Display the dictionary before removing a student record.
    print("Before deletion:", student_scores)
    # Remove student 1005 and their associated score. The pop() method removes the specified key-value pair and
    # returns the value that was stored under that key.
    removed_score = student_scores.pop(1005)

    # Displaying the removed score and the updated dictionary.
    print("Removed student 1005 with score:", removed_score)
    print("After deletion:", student_scores)

    print("\n=== EDGE CASES ===")
    # Edge Case 1: Look up a student ID that doesn't exist. The get() method returns None when the key is missing.
    missing_score = student_scores.get(9999)
    print("Missing student 9999 lookup:", missing_score)
    # Edge Case 2: Assign a new value to an existing key. A dictionary can't contain duplicate keys, so the existing
    # value changes without increasing its size.
    print("\nBefore duplicate key assignment:", student_scores)
    original_length = len(student_scores)

    student_scores[1002] = 97

    print("After duplicate key assignment:", student_scores)
    print("Number of entries before:", original_length)
    print("Number of entries after:", len(student_scores))

    # Edge Case 3: Attempt to use a list as a dictionary key. Lists are mutable and unhashable, so Python raises
    # a TypeError. The try-except block handles the error without stopping the program.
    try:
        student_scores[[1006]] = 95
    except TypeError as error:
        print("\nInvalid dictionary key:", error)

    print("\n=== REAL-WORLD SCENARIO: STUDENT GRADE MANAGEMENT ===")
    # Retrieve a student's current grade using their student ID.
    student_id = 1001
    current_grade = student_scores.get(student_id)
    print("Student", student_id, "current grade:", current_grade)
    # Update the grade after the teacher reviews an assignment.
    student_scores[student_id] = 93
    # Verify that the updated grade was saved successfully.
    updated_grade = student_scores.get(student_id)
    print("Student", student_id, "updated grade:", updated_grade)
    # Display the total number of student records.
    print("Total students records:", len(student_scores))

if __name__ == "__main__":
    main()