# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Unit 5 Discussion: Search Algorithms 
### Overview
This assignment compares linear search and binary search using Python. Both algorithms were implemented and tested with 
different dataset sizes to demonstrate their behavior, efficiency, and limitations. 

### Learning Objectives
- Implement linear search and binary search. 
- Compare algorithm performance. 
- Understand time complexity. 
- Test edge cases and boundary conditions. 
- Apply searching algorithms to real-world scenarios 

## Implementation 
### Linear Search 
Linear search examines each element sequentially until the target is found or the list ends. 
- Returns the index when the target exists. 
- Returns -1 when the target is missing. 
- Time Complexity: O(N)
- Works with sorted and unsorted lists. 

### Binary Search 
Binary search examines the middle element of a sorted list and repeatedly eliminates half of the remaining search space.
- Returns the index when the target exists. 
- Returns -1 when the target is missing. 
- Time Complexity: O(log N).
- Requires sorted data.

## Testing and Results 
### Small Dataset
Dataset: [65, 72, 81, 90, 95]
- Both algorithms found 81 at index 2.
- Both algorithms returned -1 for 85.
### Large Dataset
Dataset: 10,000 sorted integers (1-10,000)
- Both algorithms found 9999 at index 9998.
- Both algorithms returned -1 for 10001.
- Linear search has O(N) time complexity. 
- Binary search has O(log N) time complexity. 

These results confirm that both algorithms return the correct indices. The complexity analysis shows why binary search 
scales more efficiently for large sorted datasets. 

## Edge Case Testing
Four edge cases were tested: 
1. Empty List: both algorithms returned -1
2. Single-Element List: both returned index 0
3. First Element: both returned index 0 
4. Last Element: both returned index 4

All tests produced the expected results. 

## Real-World Application
A student information system was simulated using a sorted list of student IDs: 
[1001, 1005, 1010, 1015, 1020, 1025, 1030]
Both algorithms successfully located student ID 1020 at index 4. 
Linear search can be useful for small or unsorted datasets, while binary search is more efficient for large sorted 
datasets.

## Conclusion
Both algorithms successfully located existing values and handled missing values and edge cases. Linear search is simpler
to implement and doesn't require sorted data. Binary search requires sorted data but reduces the number of comparisons
as the dataset grows. The assignment demonstrated how algorithm selection affects search efficiency and why testing
different input conditions is important. 
