# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Implementation Overview 
I implemented a Stack and Queue in Python to demonstrate how two linear data structures store and remove information differently. 

The Stack used a Python list and included `push()`, `pop()`, `peek()`, and `is_empty()` methods. It followed Last In, First Out (LIFO) behavior. 

The Queue used `collections.deque` and include `enqueue()`, `dequeue()`, `front()`, and `is_empty()` methods. It followed First In, First Out (FIFo) ebhavior 

Both implementations returned `None` when attempting to remove or view an item from an empty collection. 

### Testing
I tested both data structures by adding six values and removing them to demonstrate LIFO and FIFO behavior. 

Additional test include: 
- removing an item from an empty stack/queue
- viewing an item in an empty stack/queue
- removing the only item from a collection and verifying that it became empty 

### Real-World Application
I demonstrated a content creation workflow using both data structures. 

**Stack**: A video-editing undo history removed the most recent editing action first. 
**Queue**: A video-processing system handled videos in the order they were submitted, beginning with "RGB Upgrade", followed by "Week 2 Hair Update", and then "Keyboard Galore!."