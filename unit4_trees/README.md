# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## CMSC 315 -- Unit 4 Discussion: Binary Search Trees (BST)
### Project Overview
This project demonstrates the implementation of a Binary Search Tree (BST) using Python. 
The program uses recursive methods to insert and search for values while maintaining the BST's ordering properties. 
It also demonstrates in-order traversal and tests several edge cases 

The purpose of this assignment was to better understand how binary search trees organize information and how recursion 
can be used to navigate a tree structure.

### Binary Search Tree Implementation
This program contains two primary classes: 
#### Node 
- stores an individual value within the tree
- maintains references to the left and right child nodes 
- initializes child references to `None` until nodes are inserted 
#### BST 
- initializes an empty tree using a root reference 
- uses recursive methods to insert and search for values 
- performs in-order traversal to retrieve values in ascending order 
### Insertion 
The `insert()` method calls `_insert_recursive()` to determine where a new value belongs. 
- values smaller than the current node are inserted into the left subtree
- values larger than the current node are inserted into the right subtree 
- duplicate values are ignored in this implementation 

This ordering ensures that the BST maintains its structure as new values are added. 
### Searching 
The `search()` method calls `_search-recursive()` to locate a value. 
- returns `True` when the requested calue is found 
- returns `False` when the value does not exist 
- searches the left or right subtree depending on the comparison 

A balanced BSt can search In **O(log n)** time because each comparison eliminates part of the remaining search space. 
However, an unbalanced BST may require **O(n)** time. 
### In-Order Traversal
The `inorder_traversal()` method visits nodes in the following order: 
1. Left subtree
2. Current node
3. Right subtree

Because smaller values are stored on the left and larger values on the right, in-order traversal produces values in
ascending order. 
### Program Demonstration and Testing
The BST was constructed using the following values: `[50, 30, 70, 20, 40, 60, 80]`
The root node is `50`.
#### In-Order Traversal Result
`[20, 30, 40, 50, 60, 70, 80]`
### Search Tests
| Value | Expected Result | Explanation |
|---|---|---|
| 30 | True | Value exists in the left subtree. |
| 70 | True | Value exists in the right subtree. |
| 25 | False | Value does not exist in the tree. |
| 90 | False | Value does not exist in the tree. |
### Edge Cases 
The program demonstrates several edge cases: 
- **Searching an empty tree**: returns `False` because no nodes exist 
- **Traversing an empty tree**: returns an empty list 
- **Inserting a duplicate value**: the duplicate is ignored, preserving the existing values 
- **Single-node tree**: the root is also a leaf, and traversal returns the single value 

These examples demonstrate how the program handles different tree conditions without producing errors. 
### Real-World Application 
A possible real-world application of a Binary Search Tree is organizing a collection of student identification numbers. 

Each identification number can be inserted according to its numerical vale. Smaller numbers are placed in the left subtree, 
while larger numbers are placed in the right subtree. 

When searching for a specific identification number, the BSt can use comparisons to determine which subtree to explore 
rather than checking every entry sequentially. In a balanced tree, this can make searching more efficient than a linear search. 

An in-order traversal could also display the identification numbers in ascending order. 
### Challenges and Lessons Learned 
One challenge during this assignment was implementing recursive operations correctly. Each recursive method needed 
an appropriate stopping condition and had to preserve the connections between nodes.

I also encountered an issue when the program attempted to call `inorder_traversal()`, which was not initially include in
the BST class. Adding the traversal method and its recursive helper resolved the error.

this experience helped me better understand how recursion supports tree operations and why testing each method is important
when developing a program. 
### Running the Program
1. Open the project in IntelliJ IDEA or another Python-compatible IDE
2. Open `unit4_discussion.py`
3. Ensure Python is configured correctly 
4. Run the program 
5. Review the console output for tree construction, in-order traversal, search results, and edge cases
### Conclusion 
This assignment strengthened my understanding of Binary Search Trees and their ability to organize and retrieve information 
using comparisons. By implementing recursive insertion, searching, and in-order traversal, I gained practical experience 
working with hierarchical data structures. 

The testing process also reinforced the importance of verifying program behavior, including situations involving
empty trees, duplicate values, and single-node trees. 
