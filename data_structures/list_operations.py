"""
Lists and Linked Lists in Python
================================

This example shows how to use two important data structures in Python: 
- **Lists** (built-in) 
- **Linked Lists** (custom implementation)

🔹 Python Lists:
----------------
A Python list is like a flexible container where you can store different kinds of items 
(numbers, strings, etc.). You can easily get, change, add, or remove items using simple commands.

**Why use lists?**
- Store a collection of items.
- Quickly access or change elements using their position (called an index).
- Great for small to medium amounts of data.

Examples:
    >>> lst = [1, 2, 3, "four"]
    >>> lst[0] = 35.7
    >>> lst[:3]
    [35.7, 2, 3]

🔹 Linked Lists:
----------------
A linked list is a data structure where each item (called a "node") holds:
- The actual data.
- A link (or pointer) to the next item.

Unlike Python lists, linked lists aren't built-in—you create them using classes. 
They're slower to search but better for adding/removing items from anywhere in the list.

**Why use linked lists?**
- Good for situations where data changes a lot (frequent insertions/deletions).
- Memory-efficient for large or growing datasets.

Operations included in this demo:
- Adding elements to the front (prepend) or back (append).
- Deleting an element by value.
- Printing out all the values in the list in order.

"""

# Example list operations
if __name__ == "__main__":
    # Initialize a list with mixed data types
    example_list = [1, 2, 3, "four"]
    print("Original list:", example_list)
    
    # Modify an element using indexing
    example_list[0] = 35.7
    print("After modifying index 0:", example_list)
    
    # Slice the list to get the first three elements
    print("First three elements:", example_list[:3])
    
    # Reverse the list using slicing
    print("Reversed list:", example_list[::-1])
    
    # Sort a numeric list
    numeric_list = [64, 34, 25, 12]
    numeric_list.sort()
    print("Sorted numeric list:", numeric_list)


# Linked List Implementation
class Node:
    """
    Represents a single node in a linked list.
    
    Attributes:
        data: The actual data stored in this node.
        next_node: A pointer to the next node (or None if this is the last node).
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """
    Custom class for a singly linked list (one-directional).
    
    Methods:
        - append(data): Add item to the end.
        - prepend(data): Add item to the beginning.
        - delete_with_value(data): Remove the first item that matches the value.
        - display(): Print the list in order from head to tail.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def prepend(self, data):
        """Add a node to the start of the list."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete_with_value(self, data):
        """Delete the first node that contains the given value."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next_node
            return
        current_node = self.head
        while current_node.next_node:
            if current_node.next_node.data == data:
                current_node.next_node = current_node.next_node.next_node
                return
            current_node = current_node.next_node

    def display(self):
        """Print out all elements in the list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")


# Example linked list operations
if __name__ == "__main__":
    print("\nLinked List Operations:")
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)
    print("Linked list after appending and prepending:")
    linked_list.display()

    linked_list.delete_with_value(2)
    print("Linked list after deleting value 2:")
    linked_list.display()
