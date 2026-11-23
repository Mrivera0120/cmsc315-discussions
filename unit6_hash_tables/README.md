# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Implementation

### 1. Insert Operations

An empty dictionary is created and populated with five student records.

```python
student_scores = {}

student_scores[1001] = 85
student_scores[1002] = 92
student_scores[1003] = 78
student_scores[1004] = 90
student_scores[1005] = 88
```

Each student ID is a unique key associated with a score.

### 2. Lookup Operations

The `get()` method retrieves the value associated with a specified key.

```python
score_1002 = student_scores.get(1002)
score_1004 = student_scores.get(1004)
```

**Results:**
- Student 1002: 92
- Student 1004: 90

These operations do not modify the dictionary.

### 3. Update Operations

Assigning a new value to an existing key replaces the previous value.

```python
student_scores[1003] = 86
```

**Result:** Student 1003's score changes from 78 to 86 without creating a duplicate key.

### 4. Delete Operations

The `pop()` method removes a specified key-value pair and returns its associated value.

```python
removed_score = student_scores.pop(1005)
```

**Result:** Student 1005 and their score of 88 are removed. The dictionary decreases from five entries to four.

## Edge Case Testing

### Edge Case 1: Missing Key Lookup

```python
missing_score = student_scores.get(9999)
```

**Result:** Returns `None` because student 9999 does not exist.

### Edge Case 2: Duplicate-Key Assignment

```python
original_length = len(student_scores)
student_scores[1002] = 97

print("Number of entries before:", original_length)
print("Number of entries after:", len(student_scores))
```

**Result:** Student 1002's score changes from 92 to 97, but the dictionary remains at four entries.

This demonstrates that dictionaries update existing keys rather than creating duplicates.

### Edge Case 3: Invalid Dictionary Key

```python
try:
    student_scores[[1006]] = 95
except TypeError as error:
    print("\nInvalid dictionary key:", error)
```

**Result:** Python raises a `TypeError` because lists are unhashable and cannot be used as dictionary keys.

The `try-except` block catches the exception and prevents the program from terminating unexpectedly.

## Real-World Application: Student Grade Management

A school can use a dictionary to store student grades, using student IDs as unique identifiers.

The program demonstrates retrieving, updating, and verifying a student's grade.

```python
student_id = 1001
current_grade = student_scores.get(student_id)

print("Student", student_id, "current grade:", current_grade)

student_scores[student_id] = 93

updated_grade = student_scores.get(student_id)

print("Student", student_id, "updated grade:", updated_grade)
print("Total student records:", len(student_scores))
```

**Expected output:**

```text
Student 1001 current grade: 85
Student 1001 updated grade: 93
Total student records: 4
```

This demonstrates how dictionaries can support efficient student record management.

## Hash Table Concepts

Python dictionaries use hash tables internally to support efficient key-value operations.

- **Hash Function:** Produces a hash value used to help locate a key.
- **Collision:** Occurs when different keys map to the same hash table location.
- **Collision Handling:** Resolves collisions so different keys can coexist.
- **Average Time Complexity:** O(1) for insertion, lookup, and deletion.
- **Worst-Case Time Complexity:** O(n) when operations require examining many entries.

## How to Run

1. Open the project in IntelliJ IDEA or another Python-compatible IDE.
2. Open `unit6_discussion.py`.
3. Run the program using Python.
4. Review the console output for each dictionary operation and edge case.

## Conclusion

Throughout this assignment, I gained a better understanding of how Python dictionaries function as hash tables and how key-value pairs can be used to organize information efficiently. I practiced inserting, retrieving, updating, and deleting student records using unique student IDs. One concept I found particularly interesting was how assigning a new value to an existing key updates the record without creating a duplicate entry.&nbsp;

One challenge was understanding how dictionaries handle unexpected inputs. While testing edge cases, I explored what happens when a key doesn't exist and why a list can't be used as a dictionary key. Using a try-except block helped me understand how to handle a TypeError without causing the program to stop.&nbsp;

I also learned that hash tables use hash functions to determine where information is stored. A collision occurs when different keys map to the same bucket, requiring a collision-handling technique such as chaining or probing. Hash tables can improve efficiency by allowing fast retrieval, insertion, and deletion, typically in O(1) average time. This makes dictionaries useful for managing information such as student records.&nbsp;