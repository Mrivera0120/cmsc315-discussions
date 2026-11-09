"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the value assigned to this node.
        self.value = value
        # A new node starts without any children
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Intialize an empty BST with no root node
        self.root = None

    def insert(self, value):
        # Start at the root and let the recursive helper
        # find the appropriate position for the value.
        # Smaller values belong on the left, while
        # larger values belong on the right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # When an empty position is found, create a node.
        if node is None:
            return Node(value)
        # Smaller values belong in the left subtree
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        #Larger values belong in the right subtree
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Duplicate values are ignored in this implementation.
        # Return the node so parent-child links are preserved
        return node

    def search(self, value):
        # Begin searching at the root node
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        # An empty position means the value was not found
        if node is None:
            return False
        # If the values match, the search is successful
        if value == node.value:
            return True
        # Smaller values can only be in the left subtree
        if value < node.value:
            return self._search_recursive(node.left, value)
        # Larger values can only be in the right subtree
        return self._search_recursive(node.right, value)

    def inorder(self):
        values = []
        # Visit all nodes using the recursive helper
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node is not None:
            # Visit smaller values first
            self._inorder_recursive(node.left, values)
            # Visit the current node
            values.append(node.value)
            # Visit larger values last
            self._inorder_recursive(node.right, values)

    def inorder_traversal(self):
        # Create a list to store the visited values
        values = []
        # Start the traversal from the root
        self._inorder_recursive(self.root, values)
        # Return the values in ascending order
        return values

    def _inorder_recursive(self, node, values):
        # Stop when there are no more nodes to visit.
        if node is None:
            return
        # Visit the left subtree first.
        self._inorder_recursive(node.left, values)
        # Add the current node's value.
        values.append(node.value)
        # Visit the right subtree last.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    print("\n=== TREE CONSTRUCTION ===")
    # Create an empty Binary Search Tree
    tree = BST()
    # Insert multiple values into the tree.
    # Values smaller than the current node move left.
    # Values larger than the current node move right.
    numbers = [50, 30, 70, 20, 40, 60, 80]
    for number in numbers:
        tree.insert(number)
    print("Inserted values:", numbers)
    print("Root node:", tree.root.value)

    print("\n=== IN-ORDER TRAVERSAL ===")
    # In-order traversal visits the left subtree,
    # the current node, and then the right subtree.
    #
    # Because smaller values are stored on the left
    # and larger values on the right, this traversal
    # produces values in ascending order.
    sorted_values = tree.inorder_traversal()
    print("In-Order Traversal:", sorted_values)
    print("The BST values are display in sorted order.")

    print("\n=== SEARCH TESTS ===")
    # Search for two values that exist in the BST
    existing_values = [30, 70]
    # Search for two values that do not exist
    missing_values = [25, 90]
    # BST searching can be more efficient than linear
    # searching because each comparison determines
    # which subtree to explore.
    #
    # In a balanced BST, search takes 0(log n) time.
    # In an unbalanced BST, searching may tak O(n) time.
    for value in existing_values:
        print(f"Search for {value}: {tree.search(value)}")
    for value in missing_values:
        print(f"Search for {value}: {tree.search(value)}")

    print("\n=== EDGE CASES ===")
    # Edge Case 1: Searching an empty tree.
    # Because there are no nodes, searching returns false
    empty_tree = BST()
    print("Search empty tree for 10:", empty_tree.search(10))
    # Edge Case 2: Traversing an empty tree.
    # The result is an empty list because no nodes exist
    print("Empty tree traversal:", empty_tree.inorder_traversal())
    # Edge Case 3: Inserting a duplicate value
    # Duplicate values are ignored, preventing repeated
    # entries in this implementation
    tree.insert(3)
    print("Traversal after inserting duplicate 30:", tree.inorder_traversal())
    # Edge Case 4: A tree containing only 9one node.
    # The root is also a leaf because it has no children
    single_tree = BST()
    single_tree.insert(100)
    print("Single-node traversal:", single_tree.inorder_traversal())

if __name__ == "__main__":
    main()