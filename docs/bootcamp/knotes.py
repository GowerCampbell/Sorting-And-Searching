# Sorting and Searching
# --------------------------
# WELCOME TO THE SORTING AND SEARCHING: Written By Gower Campbell
# The ability to efficiently search and sort through large
# volumes of information 
# Example: organising your email, searching
# through databases, or processing big data.

# ABSTRACT DATA TYPES
# ------------------- 
# A conceptual model for storing, accessing, and manipulating data,
# defining the allowed values, operations, and behaviours.

# Queues
# --------
# A Queue is part of the Python queue package, 
# and it follows the FIFO (First In, First Out) principle.

# This means the first item added to the queue is the first to be removed. 
# Example ATM queue: the first person in line is the first to use the machine.
# In Python, queues can be created using the Queue module.

from queue import Queue

# Creating a new Queue
students = Queue()

# Adding students to the queue
students.put("Kylie")
students.put("Julia")
students.put("Glitch")

# Iterate over all students in the queue
while not students.empty():
    # Get the current student (this removes the student from the queue)
    current_student = students.get()
    print(current_student)

# Output:
# Kylie
# Julia
# Glitch

# Stacks
# --------
# A stack follows the LIFO (Last In, First Out)
# principle, which means the last item added to the stack is the first 
# to be removed.
# Think of a stack of plates – the last plate is the first plate.

# Let's demonstrate a stack with a list of pets:
my_pets = []

# Add entries to the stack (using append to add to the stack)
my_pets.append("Dog")
my_pets.append("Cat")
my_pets.append("Ferret")

# Output the stack contents
print(my_pets)
# Output: ['Dog', 'Cat', 'Ferret']

# Remove items from the stack (using pop to remove the last added item)
my_pets.pop()
print(my_pets)
# Output: ['Dog', 'Cat']

# Graphs
# -------
# Shows the relationship between multiple elements.
# Think of social media platforms where, if you follow someone, you might 
# receive recommendations based on their connections.

# Here's an illustration of a graph with some people and their connections:
#    Vertex: Person (e.g., Alice, Bob, etc.) Listed
#    Edge: Is a line that shows a connection between two people 
#          (e.g., Alice follows Bob)

# Trees
# -------
# Family tree or business structure.
# Start with a 'node'; the parent node starting point of a tree.
# Does not have a previous generation.
# Parents are the original source of the data that extends.

# Trees then have children. Children are portions of data that grow off from
# the node. If two children stem from the same node, 
# they are then declared siblings.

# A leaf is the last set of data to appear in the tree. 
# And it doesn’t have children of its own.

# 'DATA STRUCTURES TO STORE ABSTRACT LISTS'

# Lists: Used to store a collection of data 
# Declaring a list (typed language) 
empty_list = []
# Variables can be interpreted at runtime and change as it executes.
# Enforces type constraints during operations to prevent unintended behaviour.

# Lists in Python do not need to be restricted to a single data type
example_list = [1, 2, 3, "4"]

# Finding the length of a list.
# -------
# Associated methods and attributes of an object
# Use the dir() function to inspect the list above.
print(dir(example_list))
# Listing all the methods and attributes.

# Using Special Methods (double underscores, dunder methods)
# Such as __len__ for advanced functionality. Using the built-in 
# Python function len() to get the length of the list.
print(len(example_list))

# List Indices
# -------
# To access list elements you can use an index. 
# Knowing that list indices range from 0 to len()
# example_list[index]
# example_list[1] represents the second element in the list.
# Used to retrieve data
# Accessing elements by index
element_0 = example_list[0] # Accesses the first element, 1
element_1 = example_list[1] # Accesses the second element, 2
element_2 = example_list[2] # Accesses the third element, 3
element_3 = example_list[3] # Accesses the fourth element, "4"

# Assigning values within a list
# -------
# example_list[index] = value
example_list[0] = 35.7
example_list[1] = 230
example_list[2] = 8.9
example_list[3] = 67.7

print(example_list)

# Slicing in lists
# -------
# Including negative indexing and slicing.
# Access specific portions of a list.

# Negative indices can be used to access from the end.
print(example_list[-1])  # Negative indexing outputs "67.7"
# example_list[first_element:last_element]

# First_element is inclusive.
# Last_element is exclusive.

print(example_list[1:3]) # Outputs [230, 8.9]

# By not specifying a first_element, simply start at the beginning of the list.

print(example_list[:3]) # Output [35.7, 230, 8.9]

# In Python lists can be extended by adding a step parameter to the syntax.
# Specifying how many elements to skip each time
# example_list[first_element:last_element:step]
print(example_list[::2]) # Outputs [35.7, 8.9]

# The slicing operation starts iterating from the beginning of the list
# (position 0) and jumps 2 steps each time.

# However, using a negative step allows for an easy reversal of the list.
print(example_list[::-1])
# Output: [67.7, 8.9, 230, 35.7]

'SORTING AND SEARCHING DATA'
# -------------------------
# Disorganized data does not always provide enough information.
# We need methods for arranging data logically, sorting it, and finding things.

# Retrieving specific elements or adding and removing data at specific points.

# For example inserting a surname into an alphabetical order.

# Algorithms
# -------
# Clearly defined ways to solve a problem.
# Set of instructions that can be repeated to solve similar problems.
# Coding is creating an algorithm - a set of instructions that solve stuff.

# Using a number of well-known algorithms that have been developed to solve problems
# In learning algorithms used to sort and search through data structures
# that contain a collection of data (e.g. a list). 

# BENEFITS
# Manipulate data in these data structures.
# Provide a model for writing good algorithms to analyze and learn.
# Tested by experienced developers (no need to write from scratch, just implement
# in a coding language).

'SORTING ALGORITHMS'
# -------------------------
# To make a set of numbers be placed into ascending order. 
# Scan through the set, finding the smallest number and putting it first.
# Then continue recursively until the largest number is placed.

# For a program, this is time-consuming and memory-intensive.

# Number of algorithms for sorting data:
# Selection Sort
# Shell Sort
# Bubble Sort
# Quicksort
# Merge Sort
# etc.

# Time complexity of algorithms expressed in BIG O notation.
# Real-world applications: used in databases and searching.

'BIG O notation'
# To evaluate and describe the efficiency of the code.
# Big O notation, also called the Landau symbol, is used in mathematics,
# complexity theory, and computer science.

# O refers to order to magnitude -
# refers to the rate of growth of a function dependent on its input.

'f(x) = O(g(x))'
#        Big - O
# Do not be intimidated.
"""
Excellent
O(log n), O(1) 
Stays the same regardless of how big the input to the
algorithms becomes.

Fair
O(n)

Below this value, the worse the complexity and efficiency.
For the largest input.
Bad
O(n log n) 

Horrible
O(n^2) 
O(2^n)
O(n!)

Sorting might work for small datasets or datasets
that are already largely ordered.

Keep the Big O complexity chart in mind and refer to it when sorting and
searching algorithms.
"""
# Each function below describes how an algorithm's complexity depends on the size of 
# the input to the algorithms. 

# Algorithm       :   Time Complexity
# ----------------------Best--------Average------Worst-----
# Quicksort        |Ω(n log(n)) |Ω(n log(n)) |     O(n^2) |
# Mergesort        |Ω(n log(n)) |Ω(n log(n)) |Ω(n log(n)) |
# Timsort          |    Ω(n)    |Ω(n log(n)) |Ω(n log(n)) |
# Heapsort         |Ω(n log(n)) |Ω(n log(n)) |Ω(n log(n)) |
# Bubble Sort      |    Ω(n)    |    O(n^2)  |    O(n^2)  |
# Insertion Sort   |    Ω(n)    |    O(n^2)  |    O(n^2)  |
# Selection Sort   |    Ω(n^2)  |    O(n^2)  |    O(n^2)  |
# Tree Sort        |Ω(n log(n)) |Ω(n log(n)) |    O(n^2)  |
# Shell Sort       |Ω(n log(n)) |O(n(log(n))^2|O(n(log(n))^2|

# Animated visual representation of the sorting methods:
#  https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

# Further understanding by creating a trace table of the examples working 
# with and will be brought up in interviews.

i = 0
j = 10

# WHILE i < j
#    i = i + 1
#    j = j - 1
# END WHILE

# OUTPUT(i)
# OUTPUT(j)

# The Most Popular Sorting Methods
# Open sortingmethods.py

# Bubble Sort
# -------
# Quick Sort
# -------
# Merge Sort
# -------
# Tim Sort
# -------

"SEARCHING ALGORITHMS"

# Two main algorithms for searching through elements in code.

'Linear Search'
# Example: How we as humans search by looking for something. 
#          Look through them all till we find it.

def sequential_search(target, items):
    # Iterate over the list. If we find the target item, return its index
    for index in range(len(items)):
        if items[index] == target:
            return index
    # If the target item is not found, return None
    return None

# Example Usage:
items_list = [50, 10, 40, 20, 32]
target_item = 32
result = sequential_search(target_item, items_list)

if result is not None:
    print(f"Item {target_item} found at index {result}.")
else:
    print(f"Item {target_item} not found in the list.")

'Binary Search'
# Example: Finding something in an ordered collection using a structured
#          search such as if we were looking: "To Kill a Mockingbird"

# We can start in the middle of the list and determine if our sought-for element
# is smaller than (on the left of) or bigger than (on the right of) that element.
# Halving the list until we either find it or all possibilities are eliminated.

def binary_search(target, items):
    low, high = 0, len(items) - 1

    # Keep iterating until low and high cross
    while high >= low:
        # Find midpoint
        mid = (low + high) // 2

        # If item is found at midpoint, return its index
        if items[mid] == target:
            return mid
        # Else, if item at midpoint is less than target,
        # search the second half of the list
        elif items[mid] < target:
            low = mid + 1
        # Else, search the first half
        else:
            high = mid - 1

    # Returns None if item not found
    return None

# Example usage:
sorted_items = [10, 30, 30, 40, 50]
target_item = 30
result = binary_search(target_item, sorted_items)

if result is not None:
    print(f"Item {target_item} found at index {result}.")
else:
    print(f"Item {target_item} not found in the list.")

# Sorting Algorithms: Simplified Explanation and Python Code
# ---------------------------------------------------------
# Sorting algorithms are methods used to arrange data in a specific order,
# either in ascending or descending order. Below are three popular sorting algorithms:
# Bubble Sort, QuickSort, and Merge Sort.

# Bubble Sort
# -------------------------
# Bubble Sort is a simple sorting algorithm where we repeatedly compare and 
# swap adjacent elements if they are in the wrong order.This continues until 
# no more swaps are needed, meaning the list is sorted.

def bubble_sort(items):
    # Traverse through all elements in the list
    for i in range(len(items) - 1, -1, -1):
        # Traverse the list from 1 to i
        for j in range(1, i + 1):
            # Swap if the element is greater than the next element
            if items[j - 1] > items[j]:
                items[j - 1], items[j] = items[j], items[j - 1]
    return items

# Example usage of Bubble Sort
example_list = [1, 3, 2, 6, 7, 4, 11, 5]
sorted_list_bubble = bubble_sort(example_list)
print("Bubble Sort Result:", sorted_list_bubble)


# QuickSort
# -------------------------
# QuickSort is a "divide and conquer" algorithm. It picks a "pivot" element 
# and partitions the array into two subarrays: one with elements smaller than 
# the pivot, and one with elements greater than the pivot. 
# It recursively sorts the subarrays.

def quick_sort(items, low, high):
    if low < high:
        # Partition the list and get the pivot index
        mid = partition(items, low, high)
        # Recursively sort the left partition
        quick_sort(items, low, mid - 1)
        # Recursively sort the right partition
        quick_sort(items, mid + 1, high)
    return items

def partition(items, low, high):
    # The pivot point is the first item in the sublist
    pivot = items[low]
    while low < high:
        # Move the high pointer down until a smaller element is found
        while low < high and items[high] >= pivot:
            high -= 1
        if low < high:
            items[low] = items[high]
        # Move the low pointer up until a larger element is found
        while low < high and items[low] <= pivot:
            low += 1
        if low < high:
            items[high] = items[low]
    items[low] = pivot
    return low

# Example usage of QuickSort
example_list_quick = [33, 10, 59, 26, 41, 58, 18]
sorted_list_quick = quick_sort(example_list_quick, 0, len(example_list_quick) - 1)
print("QuickSort Result:", sorted_list_quick)


# Merge Sort
# -------------------------
# Merge Sort is a "divide and conquer" algorithm where the list is split into 
# halves and recursively sorted, and then merged back in order.

def merge_sort(items):
    # If the list has more than one element, split and merge
    if len(items) > 1:
        mid = len(items) // 2  # Find the middle
        left_half = items[:mid]  # Divide the list into two halves
        right_half = items[mid:]

        # Recursively split each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves back together
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                items[k] = left_half[i]
                i += 1
            else:
                items[k] = right_half[j]
                j += 1
            k += 1

        # If there are remaining elements in left_half or right_half, add them to the list
        while i < len(left_half):
            items[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            items[k] = right_half[j]
            j += 1
            k += 1
    return items

# Example usage of Merge Sort
example_list_merge = [4, 3, 2, 8, 7, 5, 1]
sorted_list_merge = merge_sort(example_list_merge)
print("Merge Sort Result:", sorted_list_merge)


# Timsort
# -------------------------
# Timsort is a hybrid sorting algorithm that combines the strengths of Merge Sort 
# and Insertion Sort. It is adaptive, meaning it performs well when the data is 
# already partially sorted.

def insertion_sort(arr, left, right):
    # Sorting small chunks of the list using Insertion Sort
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    # Merging two sorted halves of the list
    n1 = mid - left + 1
    n2 = right - mid
    left_half = arr[left:left + n1]
    right_half = arr[mid + 1:mid + 1 + n2]
    
    i = j = k = 0
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

def timsort(arr):
    min_run = 32
    # Step 1: Sort small chunks using Insertion Sort
    for i in range(0, len(arr), min_run):
        insertion_sort(arr, i, min((i + min_run - 1), len(arr) - 1))
    
    # Step 2: Merge the sorted chunks using Merge Sort
    size = min_run
    while size < len(arr):
        for start in range(0, len(arr), 2 * size):
            mid = min(len(arr) - 1, start + size - 1)
            end = min((start + 2 * size - 1), (len(arr) - 1))
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2
    return arr

# Example usage of Timsort
example_list_timsort = [4, 3, 2, 8, 7, 5, 1]
sorted_list_timsort = timsort(example_list_timsort)
print("Timsort Result:", sorted_list_timsort)


"""
Recursion and Iteration Examples
================================

This Python file demonstrates the concepts of recursion, iteration, sorting, and searching algorithms.
Each section is explained with comments, and the corresponding code is provided for implementation.

Recursion
---------
Definition: A function that calls itself to solve a problem by breaking it down into smaller, similar sub-problems.
Examples: Factorial calculation, Fibonacci sequence, binary search.

Key Points:
- Base Case: The condition that stops the recursion.
- Recursive Case: The part where the function calls itself with a modified input.

Iteration
---------
Definition: Repeating a set of instructions multiple times until a specific condition is met.

Types:
1. Count-controlled Iteration: The number of repetitions is predetermined (e.g., for loops).
2. Sentinel-controlled Iteration: The loop continues until a specific value (sentinel) is encountered (e.g., reading input until -1 is entered).
3. Condition-controlled Iteration: The loop continues until a specific condition evaluates to false (e.g., while loops).

Stack Overflow
--------------
Definition: Occurs when a recursive function calls itself too many times, exhausting the call stack in memory.
Cause: Infinite recursion or recursion with a very large depth.
Prevention: Ensure a proper base case and limit recursion depth.

Data Structures and Algorithms
------------------------------
Data Structures:
- Definition: A specialized format for organizing, processing, retrieving, and storing data.
- Examples: Trees, Lists, Stacks, Queues.

Algorithms:
- Definition: A set of commands or steps to solve a problem or perform a computation.
- Examples: Sorting algorithms, searching algorithms.

Order of Complexity (Big-O Notation)
------------------------------------
Definition: Describes the performance of an algorithm as the size of its input grows.
Purpose: To compare the efficiency of different algorithms.

Common Complexities:
- O(1): Constant time.
- O(log n): Logarithmic time.
- O(n): Linear time.
- O(n log n): Linearithmic time.
- O(n²): Quadratic time.

Sorting Algorithms
------------------
Bubble Sort:
- How it works: Compares adjacent elements and swaps them if they are 
in the wrong order. Repeats until the list is sorted.
- Time Complexity: O(n²) in the worst case.
- Use Case: Simple but inefficient for large datasets.

Selection Sort:
- How it works: Selects the smallest element from the unsorted portion 
and swaps it with the first unsorted element. Repeats until the list is sorted.
- Time Complexity: O(n²) in the worst case.
- Use Case: Simple but inefficient for large datasets.

Insertion Sort:
- How it works: Builds the final sorted array one element at a time by 
inserting each element into its correct position in the already sorted 
part of the array.
- Time Complexity: O(n²) in the worst case.
- Use Case: Efficient for small or nearly sorted datasets.

Searching Algorithms
--------------------
Linear Search:
- How it works: Checks each element in a list sequentially until the target 
element is found or the end of the list is reached.
- Time Complexity: O(n) in the worst case.
- Use Case: Works on unsorted lists but inefficient for large datasets.

Binary Search:
- How it works: Locates a target value in a sorted array by repeatedly dividing 
the search interval in half and comparing the target value to the middle element.
- Time Complexity: O(log n) in the worst case.
- Use Case: Efficient for large, sorted datasets.

Recursion Implementation Examples
---------------------------------
"""

# ==========================================
# Recursion Examples
# ==========================================

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    Time Complexity: O(n)
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case


def binary_search(arr, target, low, high):
    """
    Perform binary search on a sorted array using recursion.
    Time Complexity: O(log n)
    """
    if low > high:  # Base case: target not found
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:  # Base case: target found
        return mid
    elif arr[mid] < target:  # Recursive case: search right half
        return binary_search(arr, target, mid + 1, high)
    else:  # Recursive case: search left half
        return binary_search(arr, target, low, mid - 1)


# ==========================================
# Iteration Examples
# ==========================================

def factorial_iterative(n):
    """
    Calculate the factorial of a number using iteration.
    Time Complexity: O(n)
    """
    result = 1
    for i in range(1, n + 1):  # Count-controlled iteration
        result *= i
    return result

# Checking each element in a list until the target element is found or the
# the end of the list is reached. No sorting is required.

def linear_search(arr, target):
    """
    Perform linear search on a list using iteration.
    Time Complexity: O(n)
    """
    for i in range(len(arr)):  # Condition-controlled iteration
        if arr[i] == target:
            return i
    return -1  # Sentinel value (not found)


# ==========================================
# Sorting Algorithms
# ==========================================

def bubble_sort(arr):
    """
    Sort an array using Bubble Sort.
    Time Complexity: O(n²)
    """
    n = len(arr)
    for i in range(n):  # Outer loop
        for j in range(0, n - i - 1):  # Inner loop
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
    return arr


def selection_sort(arr):
    """
    Sort an array using Selection Sort.
    Time Complexity: O(n²)
    """
    n = len(arr)
    for i in range(n):  # Outer loop
        min_idx = i
        for j in range(i + 1, n):  # Inner loop
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap elements
    return arr


def insertion_sort(arr):
    """
    Sort an array using Insertion Sort.
    Time Complexity: O(n²)
    """
    for i in range(1, len(arr)):  # Outer loop
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  # Inner loop
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ==========================================
# Searching Algorithms
# ==========================================


def binary_search_iterative(arr, target):
    """
    Perform binary search on a sorted array using iteration.
    Time Complexity: O(log n)
    """
    low = 0
    high = len(arr) - 1
    while low <= high:  # Condition-controlled iteration
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Sentinel value (not found)


# ==========================================
# Stack Overflow Example
# ==========================================

def infinite_recursion():
    """
    Example of a function that causes a stack overflow.
    WARNING: Do not run this function; it will crash the program.
    """
    return infinite_recursion()  # No base case, leads to stack overflow


# ==========================================
# Main Program
# ==========================================

if __name__ == "__main__":
    # Test factorial
    print("Factorial of 5 (Recursive):", factorial(5))
    print("Factorial of 5 (Iterative):", factorial_iterative(5))

    # Test binary search
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(f"Binary Search (Recursive) for {target}:", binary_search(sorted_arr, target, 0, len(sorted_arr) - 1))
    print(f"Binary Search (Iterative) for {target}:", binary_search_iterative(sorted_arr, target))

    # Test sorting algorithms
    unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort:", bubble_sort(unsorted_arr.copy()))
    print("Selection Sort:", selection_sort(unsorted_arr.copy()))
    print("Insertion Sort:", insertion_sort(unsorted_arr.copy()))

    # Test linear search
    print(f"Linear Search for {target}:", linear_search(sorted_arr, target))

    # Uncomment the line below to see stack overflow in action (WARNING: Will crash the program)
    # infinite_recursion()

"""
Sorting & Searching
Written by Gower Campbell

Data Structures & Algorithms
Define order of complexity to determine the complexity order of
searching for data using different algorithms (manipulated).

Data Structures:
- Queues: FIFO (First In, First Out)
  - Added to the back.
  - The first item added to our list will be the first item to leave.

- Stacks: LIFO (Last In, First Out)
  - Only exits when the item before it has been removed from the stack.

Algorithms:
- A set of instructions that can solve a problem.
- Provides a systematic way to solve a problem and automate tasks.

Input:
- Algorithms that take data as input.

Deterministic:
- Algorithms that will always produce the same output for a given input.
- There is no randomness or uncertainty.

Finite:
- Have a set number of steps or instructions.
- Cannot run forever and should produce an output or terminate.

Plays a big role in various fields that need computer science, mathematics,
and engineering. These are the building blocks for computer programming and
are used to perform tasks like searching and sorting.

Complexity Order:
- Describes how complex an algorithm is.
- Describes the relative representation of complexity that requires an algorithm
  to perform and scale, which is the upper bound of the growth rate of a function.
- Both Time Complexity & Space Complexity.
- We use Big O notation to express the complexity of an algorithm.

O(1) Constant Time Complexity:
- Remains constant regardless of input size.
- Example: Accessing a list element with its index or performing a basic arithmetic calculation.

O(log n) Logarithmic Time Complexity: (Good)
- Execution time grows logarithmically with input size.
- Very efficient.
- Example: Binary Search.

O(n) Linear Time Complexity: (Average)
- Execution time grows linearly with input size.
- Example: Iterating over each element in a list.

O(n²) Quadratic Time Complexity: (Bad)
- Execution time grows quadratically with input size.
- Example: Nested iteration over input data (e.g., Bubble Sort).

O(2ⁿ) Exponential Time Complexity: (Highly Inefficient)
- Execution time grows exponentially with input size.
- Example: Brute force algorithms that solve problems by going through every possible option.

Algorithm Complexity:
- Dominant term of n (Input size).
- When an input becomes very large, the other terms become negligible.
- Consider the number of operations your function performs with regards to input size.
- Identify the factor that influences the growth rate the most and express it using Big O notation.

We can compare algorithms and determine which ones are better than others.
We estimate runtime for an algorithm, helping us determine if it will be useful
for the task at hand. It also helps us identify areas in our algorithms that have
the highest time complexity, allowing us to optimize and improve them.

For lists, we can use a sort method to organize a database.
"""

# Example: Sorting a list of words from a file
with open('readfile.txt', 'r') as file:
    words = file.read().splitlines()  # Reads each line as an item in a list
pass
words.sort()  # Sorts the list alphabetically
pass
# If you want to print the sorted words
for word in words:
    print(word)
pass
# sort() method to use a step-by-step approach.

"""
Bubble Sort:
- Bubble Sort is a simple sorting algorithm that repeatedly steps through a list,
  compares adjacent elements, and swaps them if they are in the wrong order.
- This process repeats until the list is sorted.
"""

def bubble_sort(array):
    """
    Sorts an array using the Bubble Sort algorithm.

    Parameters:
    array (list): The array to be sorted.

    Returns:
    list: The sorted array.
    """
    length = len(array)
    # Outer loop: Continue until no swaps are needed

    # Keep looping until no swaps are made
    swapped = True  # Assume we need to sort
    while swapped:
        swapped = False  # Reset swapped flag for each pass

#  Inner loop: Compare adjacent element

        # Go through the list up to the second-last element
        for i in range(length - 1):
            # If two adjacent elements are out of order, swap them
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Swap elements
                swapped = True  # Mark that a swap happened

    return array  # Return the sorted array
"""
Bubble Sort Visualization:
[5, 3, 8, 4, 2]  # Initial array
[3, 5, 8, 4, 2]  # Swap 5 and 3
[3, 5, 4, 8, 2]  # Swap 8 and 4
[3, 5, 4, 2, 8]  # Swap 8 and 2
[3, 4, 5, 2, 8]  # Swap 5 and 4
[3, 4, 2, 5, 8]  # Swap 5 and 2
[3, 2, 4, 5, 8]  # Swap 4 and 2
[2, 3, 4, 5, 8]  # Swap 3 and 2
"""

"""
Insertion Sort:
- Insertion Sort is a simple sorting algorithm that builds the final sorted array
  one item at a time.
- It works by iterating through the array, comparing each element to the elements
  before it, and inserting it into its correct position in the sorted portion of the array.

Time Complexity:
- Best Case: O(n) - When the array is already sorted.
- Average Case: O(n²) - When the array is randomly sorted.
- Worst Case: O(n²) - When the array is sorted in reverse order.
"""

def insertion_sort(array):
    """
    Sorts an array using the Insertion Sort algorithm.

    Parameters:
    array (list): The array to be sorted.

    Returns:
    list: The sorted array.
    """
    length = len(array)

    # Start from the second element (index 1)
    for i in range(1, length):
        current_value = array[i]
        j = i - 1

        # Move elements of array[0..i-1] that are greater than current_value
        # to one position ahead of their current position
        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1

        # Insert the current_value into the correct position
        array[j + 1] = current_value

    return array


"""
Selection Sort:
- Selection Sort works by repeatedly finding the smallest element in the unsorted
  portion of the array and swapping it with the first unsorted element.
- This process continues until the entire array is sorted.

Time Complexity:
- Best Case: O(n²)
- Average Case: O(n²)
- Worst Case: O(n²)
"""

def selection_sort(array):
    """
    Sorts an array using the Selection Sort algorithm.

    Parameters:
    array (list): The array to be sorted.

    Returns:
    list: The sorted array.
    """
    length = len(array)

    # Traverse through all array elements
    for i in range(length - 1):
        # Assume the current index is the minimum
        min_index = i

        # Find the index of the smallest element in the unsorted portion
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array


"""
SEARCHING ALGORITHMS

There are two main searching algorithms:
1. Linear Search
2. Binary Search

- Linear Search is the simplest and closest to how humans naturally search for something.
- Binary Search is faster but requires the list to be sorted beforehand.
"""

"""
Linear Search:
- Start from the first element and compare each element with the target value.
- If the target value is found, return its index.
- If the end of the list is reached without finding the target, return -1.

Time Complexity: O(n) - In the worst case, we may need to check every element.
"""

def linear_search(array, target_value):
    """
    Performs a linear search on the given array.

    Parameters:
    array (list): The list of elements to search through.
    target_value: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index, value in enumerate(array):
        if value == target_value:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found


"""
Binary Search:
- Requires the list to be sorted.
- Start by comparing the target value with the middle element of the list.
- If the target is equal to the middle element, return its index.
- If the target is smaller, repeat the search in the left half of the list.
- If the target is larger, repeat the search in the right half of the list.
- Repeat the process until the target is found or the list can no longer be divided.

Time Complexity: O(log n) - The search space is halved with each comparison.
"""

def binary_search(array, target):
    """
    Performs a binary search on the given sorted array.

    Parameters:
    array (list): The sorted list of elements to search through.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if array[mid] == target:
            return mid  # Return the index if the target is found
        elif array[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Return -1 if the target is not found


# Example usage:
if __name__ == "__main__":
    # Example array for Linear Search
    linear_array = [3, 5, 2, 8, 10, 7]
    linear_target = 8
    print("Linear Search:")
    print("Array:", linear_array)
    print("Target:", linear_target)
    linear_result = linear_search(linear_array, linear_target)
    print("Result (Index):", linear_result)

    # Example array for Binary Search
    binary_array = [2, 5, 7, 8, 10, 12, 15]
    binary_target = 10
    print("\nBinary Search:")
    print("Array:", binary_array)
    print("Target:", binary_target)
    binary_result = binary_search(binary_array, binary_target)
    print("Result (Index):", binary_result)

"""
Output:
Linear Search:
Array: [3, 5, 2, 8, 10, 7]
Target: 8
Result (Index): 3

Binary Search:
Array: [2, 5, 7, 8, 10, 12, 15]
Target: 10
Result (Index): 4
"""

"""
Summary:
- Sorting Algorithms: Bubble Sort, Insertion Sort, and Selection Sort are 
simple but have O(n²) time complexity.
- Searching Algorithms: Linear Search is O(n), while Binary Search 
is O(log n) but requires a sorted array.
- Complexity Order: Understanding Big O notation helps compare algorithms 
and optimize performance.
"""

"""
Glossary:
- Big O Notation: A mathematical notation that describes the upper 
bound of an algorithm's complexity.
- Time Complexity: The amount of time an algorithm takes to 
complete as a function of the input size.
- Space Complexity: The amount of memory an algorithm 
ses as a function of the input size.
"""


