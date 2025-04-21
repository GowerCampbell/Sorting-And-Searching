"""
Stack Implementations in Python
===============================

This module demonstrates two stack implementations:
1. **Simple Stack using a Python list** (for ease of use and small data)
2. **Advanced Stack using a Linked List** (for better memory management and flexibility)

🟢 What is a Stack?
-------------------
A stack is a data structure that follows the **LIFO** principle:
**Last In, First Out** — the last item added is the first one removed.

📦 Use Cases for Stacks:
-------------------------
- Undo/Redo functionality in text editors
- Backtracking (e.g., maze solving, recursive algorithms)
- Browser history tracking
- Expression evaluation (e.g., parsing math expressions)

"""

# ✅ Basic Stack using Python List
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


# 🚀 Advanced Stack using Linked List (Node-based)
class Node:
    """Node for the linked list stack."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    """
    Stack implementation using a singly linked list.
    
    Pros:
    - No size limit (more memory efficient than lists for large stacks)
    - Dynamic memory usage

    Methods:
    - push(data): Add item to top.
    - pop(): Remove and return top item.
    - peek(): View top item without removing.
    - is_empty(): Check if stack is empty.
    - size(): Return number of elements.
    """
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """Insert an item on top of the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_data

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        """Check whether the stack is empty."""
        return self.top is None

    def size(self):
        """Return the number of items in the stack."""
        return self._size


# 🧪 Example usage
if __name__ == "__main__":
    print("List-based Stack:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack size:", stack.size())
    print("Top item:", stack.peek())
    print("Popped item:", stack.pop())
    print("Stack size after pop:", stack.size())

    print("\nLinked List-based Stack:")
    ll_stack = LinkedListStack()
    ll_stack.push("a")
    ll_stack.push("b")
    ll_stack.push("c")
    print("Stack size:", ll_stack.size())
    print("Top item:", ll_stack.peek())
    print("Popped item:", ll_stack.pop())
    print("Stack size after pop:", ll_stack.size())
