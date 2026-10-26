"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # Prevent an error when attempting to pop from an empty stack
        if not self.items:
            return None

        # Remove and return the top item, following LIFO behavior
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Return None if the stack is empty
        if not self.items:
            return None

        # View the top item without removing it from teh stack
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self.items

class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Return None if the queue has no items to remove
        if not self.items:
            return None

        # Remove and return the oldest item, following FIFO behavior
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Return None if the queue is empty
        if not self.items:
            return None

        # Return the first item without removing if from the queue
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self.items


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.S
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK DEMO ===")
    # Create a stack and add (at least) 4 values
    print("=== Creating a stack with at least 4 values ===")
    stack = Stack()

    stack.push(21)
    stack.push(45)
    stack.push(70)
    stack.push(3)
    stack.push(7)
    stack.push(65)

    print("Just added: 21, 45, 70, 3, 7, 65.")
    print("Top Item: ", stack.peek())

    #Demonstrating LIFO behavior
    print("=== Demostrating How LIFO Behavior Works ===")
    print("Removing the items in the list in LIFO order: ")
    print("Removed: ", stack.pop())
    print("Removed: ", stack.pop())
    print("Removed: ", stack.pop())
    print("Removed: ", stack.pop())
    print("Removed: ", stack.pop())
    print("Removed: ", stack.pop())

    # Test operations on an empty stack
    print("=== Testing Operations on an Empty Stack ===")
    print("Is the stack empty?", stack.is_empty())
    print("Pop from empty stack: ", stack.pop())
    print("Peek at empty stack: ", stack.peek())

    # Testing with one item
    print("=== Testing with a Single Item ===")
    single_stack = Stack()
    single_stack.push(100)

    print("Single-item Stack Before Removal: ", single_stack.peek())
    print("Removed single item: ", single_stack.pop())
    print("Is single-tem stack empty?", single_stack.is_empty())
# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO ===")
    print("=== Creating a Queue with at least 4 Values ===")
    # Creating the Queue
    queue = Queue()

    queue.enqueue(29)
    queue.enqueue(35)
    queue.enqueue(45)
    queue.enqueue(60)
    queue.enqueue(87)
    queue.enqueue(83)

    print("Just added: 29, 35, 45, 60, 87, 83")
    print("Front Item: ", queue.front())

    # Demonstrating FIFO Behavior
    print("=== Demonstrating How FIFO behavior Works ===")
    print("Removing the items in the queue in LIFO order: ")

    print("Removed: ", queue.dequeue())
    print("Removed: ", queue.dequeue())
    print("Removed: ", queue.dequeue())
    print("Removed: ", queue.dequeue())
    print("Removed: ", queue.dequeue())
    print("Removed: ", queue.dequeue())

    # Testing operations on an empty queue
    print("=== Testing Operations on an Empty Queue ===")
    print("Is the queue empty: ", queue.is_empty())
    print("Deque from empty queue: ", queue.dequeue())

    # Demonstrating Operations on an Empty Queue
    print("=== Testing Viewing the Front of an Empty Queue,")
    print("Front of Empty Queue: ", queue.front())

    # Testing with a single item
    print("=== Verifying a Single-Item Queue Becomes Empty After Removal")
    single_queue = Queue()
    single_queue.enqueue(100)

    print("Single-Item Queue Before Removal: ", single_queue.front())
    print("Removed single item: ", single_queue.dequeue())
    print("Is single-item queue empty? ", single_queue.is_empty())

    # Real-World Application: Video Editing Undo History
    print("\nREAL WORLD APPLICATION")
    print("=== VIDEO EDITING : UNDO HISTORY ===")

    # Demonstrating my understanding of the Stack Operation
    edit_history = Stack()

    edit_history.push("Trim video clips")
    edit_history.push("Add background music")
    edit_history.push("Add captions")

    print("Most Recent Edit: ", edit_history.peek())
    print("Undo: ", edit_history.pop())
    print("Undo: ", edit_history.pop())
    print("Next edit to undo: ", edit_history.peek())

    # Real-World Application: Video Upload Processing
    print("\n=== VIDEO UPLOAD PROCESSING === ")

    # Demonstrating my understanding of the Queue Operation
    upload_queue = Queue()

    upload_queue.enqueue("RGB Upgrade")
    upload_queue.enqueue("Week 2 Hair Update")
    upload_queue.enqueue("Keyboard Galore!")

    print("First video waiting: ", upload_queue.front())

    print("Processing: ", upload_queue.dequeue())
    print("Processing: ", upload_queue.dequeue())
    print("Next video waiting: ", upload_queue.front())

if __name__ == "__main__":
    main()
