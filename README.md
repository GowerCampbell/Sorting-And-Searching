
# Sorting and Searching Learning Module

Welcome to the **Sorting and Searching Learning Module** — a hands-on guide to mastering two foundational concepts in computer science. Curated by Gower Campbell, this repository offers a comprehensive walkthrough of key algorithms, real-world applications, and complexity insights — all in clean, modular Python.

Whether you're a coding newcomer or revisiting the basics, this module aims to make sorting and searching intuitive, applicable, and engaging.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Sorting Algorithms](#sorting-algorithms)
3. [Searching Algorithms](#searching-algorithms)
4. [Real-World Applications](#real-world-applications)
5. [Complexity Analysis](#complexity-analysis)
6. [Data Structures](#data-structures)
7. [Reflections](#reflections)
8. [How to Use This Repository](#how-to-use-this-repository)
9. [Bibliography](#bibliography)

---

## Introduction

Sorting and searching are essential techniques that power everything from database queries to recommendation engines. At their core:

- **Sorting** organizes data in a specific sequence — ascending, descending, or custom.
- **Searching** retrieves target data from a collection, whether structured or unstructured.

For instance:
- Sorting emails by8080by date helps you view the latest messages first.
- Searching a song in your music library lets you find that track in seconds.

This module explores:
- Popular sorting/searching algorithms
- Practical use cases (e.g., cafés, libraries, music apps)
- Performance trade-offs
- Python implementations, following clean coding and MVC principles

---

## Sorting Algorithms

Sorting transforms disordered data into a predictable structure. The module includes both basic and advanced algorithms, each with annotated code, complexity analysis, and links for deep dives.

| Algorithm       | Worst-Case Time | Space Complexity | Overview | Code |
|----------------|------------------|------------------|----------|------|
| **Bubble Sort**     | O(n²)           | O(1)            | Iteratively compares and swaps adjacent elements. Easy to grasp, but inefficient for large datasets. | [bubble_sort.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/sorting_algorithms/bubble_sort.py) |
| **Insertion Sort**  | O(n²)           | O(1)            | Inserts elements into their correct position. Great for nearly sorted or small datasets. | [insertion_sort.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/sorting_algorithms/insertion_sort.py) |
| **Selection Sort**  | O(n²)           | O(1)            | Selects the smallest remaining element and places it at the correct position. Simple but not optimal. | [selection_sort.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/sorting_algorithms/selection_sort.py) |
| **Quick Sort**      | O(n²)           | O(log n)        | Uses a pivot to partition data and recursively sort subarrays. Fast in practice; core of many libraries. | [quick_sort.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/sorting_algorithms/quick_sort.py) |
| **Merge Sort**      | O(n log n)      | O(n)            | Divide-and-conquer algorithm that splits, sorts, and merges. Reliable and stable. | [merge_sort.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/sorting_algorithms/merge_sort.py) |
| **Timsort**         | O(n log n)      | O(n)            | Hybrid of Merge and Insertion Sort; Python’s built-in sort() is based on this. Adaptive and production-ready. | [timsort.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/sorting_algorithms/timsort.py) |

### Key Sorting Concepts

- **Stability**: Does the algorithm maintain the relative order of equal elements? (e.g., Merge Sort: ✔️, Quick Sort: ❌)
- **In-Place**: Does it sort within the original structure using minimal extra memory?
- **Divide and Conquer**: Efficient strategy used by Merge and Quick Sort to reduce problem size.

---

## Searching Algorithms

Searching is about **locating specific data within a dataset**. Depending on whether the data is sorted, different strategies are more effective.

| Algorithm       | Time Complexity | Requirement    | Overview | Code |
|----------------|------------------|----------------|----------|------|
| **Linear Search**   | O(n)          | None           | Scans each element in sequence. Straightforward but inefficient for large datasets. | [linear_search.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/searching_algorithms/linear_search.py) |
| **Binary Search**   | O(log n)      | Sorted Data    | Repeatedly splits the dataset in half to narrow down the search. Fast and efficient. | [binary_search.py](https://github.com/gowercampbell/sorting-searching-module/blob/main/searching_algorithms/binary_search.py) |

### Key Searching Concepts

- **Sorted Data Requirement**: Binary Search only works when data is sorted. Sorting first can significantly improve search speed in large datasets.
- **Recursive vs Iterative**: Binary Search is implemented both recursively (clean, elegant) and iteratively (efficient, stack-safe).

---

## Real-World Applications

See how sorting and searching play out in everyday systems:

1. **[Coffee Order System](https://github.com/gowercampbell/sorting-searching-module/blob/main/real_world_examples/coffee_order_system.py)**  
   - Sort orders by total price or timestamp.
   - Search by customer name or order ID.
   - Built using MVC (Model-View-Controller) for clarity and scalability.

2. **[Library System](https://github.com/gowercampbell/sorting-searching-module/blob/main/real_world_examples/library_system.py)**  
   - Sort books by title, author, or availability.
   - Search for a book by ISBN or keyword.
   - Incorporates classes like Book, Member, and a central LibraryController.

3. **[Album Management Tool](https://github.com/gowercampbell/sorting-searching-module/blob/main/real_world_examples/album_management.py)**  
   - Sorts albums using Python’s key parameter with custom comparators.
   - Searches by album name or artist.
   - Object-Oriented approach using magic methods like `__lt__` and `__eq__`.

---

## Complexity Analysis

Big O notation describes how an algorithm’s performance scales with the size of its input. It focuses on the **worst-case scenario** to evaluate efficiency and scalability.

### Common Complexities

- **O(1)** – Constant time (e.g., accessing a list index)
- **O(log n)** – Logarithmic time (e.g., Binary Search)
- **O(n)** – Linear time (e.g., Linear Search)
- **O(n log n)** – Linearithmic time (e.g., Merge Sort, QuickSort average)
- **O(n²)** – Quadratic time (e.g., Bubble Sort, Selection Sort)

### Complexity Comparison Table

| Algorithm         | Best Case     | Average Case   | Worst Case     |
|------------------|---------------|----------------|----------------|
| **Bubble Sort**   | O(n)          | O(n²)          | O(n²)          |
| **Insertion Sort**| O(n)          | O(n²)          | O(n²)          |
| **Selection Sort**| O(n²)         | O(n²)          | O(n²)          |
| **QuickSort**     | O(n log n)    | O(n log n)     | O(n²)          |
| **Merge Sort**    | O(n log n)    | O(n log n)     | O(n log n)     |
| **TimSort**       | O(n)          | O(n log n)     | O(n log n)     |
| **Linear Search** | O(1)          | O(n)           | O(n)           |
| **Binary Search** | O(1)          | O(log n)       | O(log n)       |

---

## Data Structures

Efficient algorithms rely on the right data structures. This module introduces foundational structures used in sorting, searching, and problem-solving.

### Lists
Dynamic arrays that allow indexing, slicing, and iteration. Python’s go-to structure for general-purpose storage.

📂 [Implementation](https://github.com/gowercampbell/sorting-searching-module/blob/main/data_structures/list_operations.py)

### Stacks
**LIFO** (Last In, First Out) structure. Ideal for undo features, recursive parsing, and expression evaluation.

📂 [Implementation](https://github.com/gowercampbell/sorting-searching-module/blob/main/data_structures/stack.py)

### Queues
**FIFO** (First In, First Out) structure. Commonly used in task scheduling, simulations, and print/job queues.

📂 [Implementation](https://github.com/gowercampbell/sorting-searching-module/blob/main/data_structures/queue.py)

---

## Reflections

In [reflections.md](https://github.com/gowercampbell/sorting-searching-module/blob/main/docs/reflections.md), you’ll find personal insights and best-practice tips:
- Use Insertion Sort for tiny, nearly sorted collections.
- Prefer Merge Sort or Timsort for stability and speed on larger datasets.
- Choose Binary Search only when your data is already sorted.
- Think of sorting and searching like real-life activities: organizing your email inbox, finding a name in your contact list, or browsing a playlist.

---

## How to Use This Repository

1. **Clone the Repository**: `git clone https://github.com/gowercampbell/sorting-searching-module.git`
2. **Navigate to Folders**: Explore `sorting_algorithms/`, `searching_algorithms/`, `real_world_examples/`, and `data_structures/` for code.
3. **Run Scripts**: Use `python sorting_algorithms/bubble_sort.py` (or similar) to test implementations.
4. **Read Reflections**: Check [docs/reflections.md](https://github.com/gowercampbell/sorting-searching-module/blob/main/docs/reflections.md) for insights.
5. **Experiment**: Modify code to test edge cases or add features (e.g., custom sorting keys).

---

## Bibliography

- [GeeksforGeeks: Sorting Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#Sorting)
- [GeeksforGeeks: Searching Algorithms](https://www.geeksforgeeks.org/searching-algorithms/)
- [Python Docs: Data Structures (Lists)](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Docs: Sorting Techniques](https://docs.python.org/3/howto/sorting.html)
- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [University of Cape Town (2014): Visual Algorithm Tools](https://www.cs.uct.ac.za/Research/DNA/Visualizations/)
- [Dalal (2004): Search Algorithm Examples – ResearchGate](https://www.researchgate.net/publication/221186184_Searching_algorithms_in_inverted_files)


