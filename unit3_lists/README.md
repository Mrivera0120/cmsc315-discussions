# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Implementation Documentation 
### List Insertion
I created an `insert_at()` function to insert a value into a list at a specified index. I used Python's `insert()` method to add elements without replacing existing values. 

I tested insertion at the beginning, middle, and end of a keyboard collection. I also displayed the updated list after each insertion to demonstrate how existing elements shift to the right when a new value is added. 

### List Deletion
I created a `delete_at()` function to remove and return an element from a specified index. I used an `if` statement o validate the index before using Python's `pop()` method. 

If the index was invalid, the function returned `None` instead of causing an error. 
I tested deletion at the beginning, middle, and end of a list and displayed both the removed keyboard and the update collection. 

### Linear Search 
I created a `delete_at()` function to remove and return an element from a specified index. I used an `if` statement to validate the index before using Python's `pop()` method. 

If the index was invalid, the function returned `None` instead of causing an error. I tested deletion at the beginning, middle, and end of a list and displayed both the removed keyboard and the updated collection. 

### Testing 
I complete the `main()` function by creating separate keyboard lists to demonstrate insertion, deletion, and searching operations. 

For insertion and deletion, I tested operations at different positions and displayed the results after each modification. 
For searching, I verified that the function correctly identified an existing value and handled a missing value. 

I ran the program in IntelliJ IDEA and reviewed teh console output to verify that the operations produced the expected results. 

### Edge Case Testing
I tested four edge cases to demonstrate how the program handled unusual situations. 

First, I attempted to delete an element using an invalid index of `10`. The function returned `None`, and the original list remained unchanged.
Next, I searched for a keyboard that was not in the collection. The function returned `-1`, indicating that no matching value was found.
I also tested inserting a keyboard into an empty list. The program successfully added `Redragon` without requiring any existing elements to shift. 

Finally, I attempted to delete an element from an empty list. The function returned `None` without causing an error. 

### Performance Analysis
This program demonstrated how the position of an element can affect the performance of list operations. 

Inserting or deleting an element at the beginning or middle of a list may require other elements to shift positions, 
resulting in O(n) time complexity. Inserting at the end typically takes O(1) amortized time. 

Linear searching has O(n) worst-case time complexity because the program may need to examine every element
before finding a match or determining that the value doesn't exist. 

### Real-World Application 
This program demonstrated how Python list operations could be used in a mechanical keyboard inventory or collection management application. 

Insertion could be used to add new keyboards to a collection, while deletion could remove keyboards that were sold or no longer owned. Searching could help locate a specific 
keyboard within the inventory. 

These operations demonstrated how lists can be used to organize and update information while considering the performance of different operations. 
