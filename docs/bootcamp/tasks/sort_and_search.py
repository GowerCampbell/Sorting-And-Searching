# sort_and_search.py

# Learning Objectives:
# - Implement an appropriate search algorithm for an unsorted list.
# - Apply the Insertion Sort algorithm to sort the list.
# - Use a different search algorithm on the sorted list.
# - Reflect on algorithm choices and real-world applications.

# Written By Gower Campbell

# Original List
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Linear Search Algorithm
def linear_search(array, target):
    """
    Search for a target value by finding the first value in order.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1

# Insertion Sort Algorithm
def insertion_sort(array):
    """
    Sort an array using Insertion Sort.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Binary Search Algorithm (for sorted list)
def binary_search(array, target):
    """
    Search for a target value using Binary Search.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Search for the number 9 using Linear Search
index_linear = linear_search(numbers, 9)

# Sort the list using Insertion Sort
sorted_numbers = insertion_sort(numbers.copy())

# Search for the number 9 using Binary Search
index_binary = binary_search(sorted_numbers, 9)

# Results
print("Original List:", numbers)
print("Sorted List:", sorted_numbers)
print("Index of 9 (Linear Search):", index_linear)
print("Index of 9 (Binary Search):", index_binary)

# <---- Reflection ---->
# I decided to use a Linear Search because it works efficiently with small lists 
# and doesn't demand much processing power, making it a simple and practical
# choice for this task.

# Through my research into Insertion Sort, I found that it is effective for 
# small datasets. However, its "time complexity is O(n²) in the worst case, which
# can lead to slower performance as the size of the dataset increases 
# (GeeksforGeeks).

# After sorting the list, I applied a Binary Search to locate the index, as 
# I know how valuable it can be for quickly finding films or TV shows based on
# their IMDb ratings in large databases."

# <----- Bibliography ----->
"""
- GeeksforGeeks: Linear Search Algorithm
  https://www.geeksforgeeks.org/linear-search/
- GeeksforGeeks: Insertion Sort Algorithm
  https://www.geeksforgeeks.org/insertion-sort/
- GeeksforGeeks: Binary Search Algorithm
  https://www.geeksforgeeks.org/binary-search/
- Python Documentation: Lists and Control Structures
  https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
"""
