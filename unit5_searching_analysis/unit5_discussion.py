"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Search the list from beginning to end. Return the index if the target is found.
    Return -1 if the target is not found.
    """
    # Examine each element starting at index 0
    for i in range(len(lst)):
        # Check whether the current element matches the target
        if lst[i] == target:
            return i
    # If no element matches, return -1
    return -1


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    Assumes the list is already sorted. Returns the index if the target is found.
    Returns -1 if the target is not found.
    """
    # Set the boundaries of the search space.
    low = 0
    high = len(lst) - 1
    # Continue searching while the search space is valid.
    while low <= high:
        # Find the middle index of the current search space.
        mid = (low + high) // 2
        # If the middle element matches, return its index
        if lst[mid] == target:
            return mid
        # If the target is larger, eliminate the left half
        elif lst[mid] < target:
            low = mid + 1
        # If the target is smaller, eleiminate the right half
        else:
            high = mid - 1
    # Return -1 if the target is not found
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # Create a small sorted dataset of student scores
    scores =[65, 72, 81, 90, 95]
    # Select a score that exists and one that doesn't
    existing_score = 81
    missing_score = 85
    # Display the dataset being searched
    print("Student scores:", scores)
    # Test linear search with an existing score.
    # Linear search checks each score from beginning to end.
    print("\nLinear Search:")
    print("Existing score (81):", linear_search(scores, existing_score))
    # Test linear search with a missing score
    # Returns -1 after checking the entire list.
    print("Missing score (85):", linear_search(scores, missing_score))
    # Test binary search with an existing score
    # Binary search checks the middle and eliminates half of the remaining sorted scores after each comparison
    print("\nBinary Search:")
    print("Existing score (81):", binary_search(scores,existing_score))
    # Test binary search with a missing score.
    # Returns -1 when no search space remains.
    print("Missing score (85):", binary_search(scores, missing_score))

    print("\n=== LARGE DATASET TEST ===")
    # Create a large sorted dataset containing 10,000 scores.
    # range() generates values from 1 through 10,000
    large_scores = list(range(1, 10001))
    # Choose one existing value and one missing value.
    existing_score = 9999
    missing_score = 10001
    #Display the dataset size rather than all 10,000 values
    print("Dataset size:", len(large_scores))
    # Test linear search with an existing value
    # Linear search checks values sequentially
    print("\nLinear Search:")
    print("Existing score (9999):", linear_search(large_scores, existing_score))
    print("Missing score (10001):", linear_search(large_scores, missing_score))
    # Test binary search with an existing value.
    # Binary search repeatedly eliminates half of the remaining sorted elements.
    print("\nBinary Search:")
    print("Existing score (9999):", binary_search(large_scores, existing_score))
    # Test binary search with a missing value.
    # Returns -1 when the search space becomes empty
    print("Missing score (10001):", binary_search(large_scores, missing_score))
    # Compare the worst-caSE TIME COMPLEXITIES
    print("\nPerformance Comparison:")
    print("Linear Search: O(N)")
    print("Binary Search: O(log N)")
    # Binary search scales better for large sorted datasets because it eliminates about half the search space
    # after each unsuccessful comparison

    print("\n=== EDGE CASE TESTS ===")
    # Edge Case 1: Empty List
    # Neither algorithm can find a value in an empty list. Both should return -1 without causing an error
    empty_scores = []

    print("\nEdge Case 1: Empty List")
    print("Linear Search:", linear_search(empty_scores, 81))
    print("Binary Search:", binary_search(empty_scores, 81))
    # Edge Case 2: Single-Element List
    # Both algorithms should find the only socre at index 0
    single_score = [81]

    print("\nEdge Case 2: Single-Element List")
    print("Linear Search:", linear_search(single_score, 81))
    print("Binary Search:", binary_search(single_score, 81))
    # Edge Case 3: First Element
    # Linear search finds the target immediately. Binary search narrows its search to the left half.
    sorted_scores = [65, 72, 81, 90, 95]

    print("\nEdge Case 3: First Element")
    print("Linear Search:", linear_search(sorted_scores, 65))
    print("Binary Search:", binary_search(sorted_scores, 65))
    # Edge Case 4: Last Element
    # Linear search checks every element before finding it. Binary search repeatedly narrows the search to the right.
    print("\nEdge Case 4: Last Element")
    print("Linear Search:", linear_search(sorted_scores, 95))
    print("Binary Search:", binary_search(sorted_scores, 95))

    # ===============================
    # REAL-WORLD APPLICATION
    # ===============================
    print("\n=== REAL-WORLD APPLICATION ===")

    # A school stores student ID numbers in a sorted list. Each ID represents a student record in the system.
    student_ids = [1001, 1005, 1010, 1015, 1020, 1025, 1030]
    # Search for a student ID that exists
    target_id = 1020

    print("Student IDs:", student_ids)
    print("Searching for student ID:", target_id)
    # Linear search checks student IDs one at a time
    print("Linear Search Result:", linear_search(student_ids, target_id))
    # Binary search uses the sorted order to eliminate half of the remaining IDs after each comparison
    print("Binary Search Result:", binary_search(student_ids, target_id))

    # Both methods return index 4. Binary search is generally more efficient for large sorted datasets, while linear
    # search also works when records aren't sorted.


if __name__ == "__main__":
    main()