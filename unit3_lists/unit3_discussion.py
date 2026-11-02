"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """ Insert a value into the list at the specified index """
    lst.insert(index, value)


def delete_at(lst, index):
   """
   Remove and return an element at a valid index
   Return None if the index is invalid
   """
   if 0 <= index < len(lst) :
       return lst.pop(index)

   return None


def search_value(lst, value):
    """
    Search for a value within the list.
    Return its index if found, or -1 if not found
    """
    # Check each index in the list, starting at 0
    for index in range(len(lst)) :
        # If the current element matches, return its index
        if lst[index] == value :
            return index

    # If no match was found, return -1
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    print("\n=== INSERTION TESTS ===")
    # 1. Create a list containing several values.
    keyboards = ["Aula", "Epomaker", "Varmillo"]
    # 2. Display the original list.
    print("Original list: ", keyboards)
    # Insert a keyboard at the beginning of the list
    insert_at(keyboards, 0, "Redragon")
    print("After beginning insertion: ", keyboards)
    # Insert a keyboard in the middle of the list
    # Elements at index 2 and beyond shift to the right
    insert_at(keyboards, 2, "KiiBOOM")
    print("After middle insertions: ", keyboards)
    # Insert a keyboard at the end of the list
    # Existing elements don't need to shift
    insert_at(keyboards, len(keyboards), "Dareu")
    print("After end insertion: ", keyboards)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #

    print("\n=== DELETION TESTS ===")
    # Create a list of keyboards to demonstrate deletion
    delete_keyboards = ["Redragon", "Aula", "KiiBOOM", "Epomaker", "Varmillo"]
    print("Original list: ", delete_keyboards)
    # Delete the first keyboard in the list
    # All remaining elements shift one position to the left
    removed = delete_at(delete_keyboards, 0)
    print("Removed from beginning: ", removed)
    print("After beginning deletion: ", delete_keyboards)
    # Delete a keyboard from the middle of the list
    # Elements after the deleted position shift to the left
    removed = delete_at(delete_keyboards, 2)
    print("Removed from middle: ", removed)
    print("After middle deletion: ", delete_keyboards)

    # Delete the last keyboard in the list
    # No remaining elements need to shift positions
    removed = delete_at(delete_keyboards, len(delete_keyboards) - 1)
    print("Removed from end: ", removed)
    print("After end deletion: ", delete_keyboards)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")
    # Creat a list of keyboards to demonstrate searching
    search_keyboards = ["Aula", "Epomaker", "Varmillo", "Redragon", "KiiBOOM"]
    print("Keyboard collection: ", search_keyboards)
    # Search for a keyboard that exists in the list
    # Linear search checks each element sequentially until a match is found
    existing_keyboard = "Varmillo"
    result = search_value(search_keyboards, existing_keyboard)
    # Display the index where the keyboard was found
    print("Searching for: ", existing_keyboard)
    print("Found at index: ", result)
    # Search for a keyboard that doesn't exist in the list
    # The function returns -1 after checking every element
    missing_keyboard = "Dareu"
    result = search_value(search_keyboards, missing_keyboard)
    # Display an explanation when the keyboard is not found
    print("Searching for: ", missing_keyboard)
    if result == -1 :
        print("Keyboard not found in the collection.")
    else:
        print("Found at index: ", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge Case 1: Delete using an invalid index
    # The index is outside the list's range, so the function returns None without changing the original list
    edge_keyboards = ["Aula", "Epomaker", "Varmillo"]
    print("Original list:", edge_keyboards)

    removed = delete_at(edge_keyboards, 10)
    print("Delete at invalid index 10: ", removed)
    print("List after invalid deletion: ", edge_keyboards)

    # Edge Case 2: Search for a missing keyboard
    # The function checks all elements ad returns -1 when the requested value can't be found
    print("Search for missing keyboard 'Dareu':", result)

    # Edge Case 3: Insert into an empty list
    # An empty list has no existing elements to shift
    empty_keyboards = []
    print("Empty list after insertion: ", empty_keyboards)

    insert_at(empty_keyboards, 0, "Redragon")
    print("Empty list after inssertion: ", empty_keyboards)

    # Edge Case 4: Delete from an empty list
    # No valid index exists, so the function safely returns None
    empty_keyboards = []
    removed = delete_at(empty_keyboards, 0)

    print("Delete from empty list: ", removed)
    print("Empty list after deletion:", empty_keyboards)


if __name__ == "__main__":
    main()