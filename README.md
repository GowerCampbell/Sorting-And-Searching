# Sorting and Searching 

Welcome to my **Sorting and Searching Learning Module** — a hands-on guide to mastering two foundational concepts in computer science. Curated by Gower Campbell, this repository offers a comprehensive walkthrough of key algorithms, real-world applications, and complexity insights — all in clean, modular Python.

Whether you're a coding newcomer or revisiting the basics, this module aims to make sorting and searching intuitive, applicable, and engaging.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Sorting Algorithms](#sorting-algorithms)
3. [Searching Algorithms](#searching-algorithms)
4. [Real-World Applications](#real-world-applications)
5. [Complexity Analysis](#complexity-analysis)
6. [Reflections](#reflections)
7. [How to Use This Repository](#how-to-use-this-repository)

---

## Introduction

Sorting and searching are essential techniques that power everything from database queries to recommendation engines. At their core:

- **Sorting** organizes data in a specific sequence — ascending, descending, or custom.
- **Searching** retrieves target data from a collection, whether structured or unstructured.

For instance:
- Sorting emails by date helps you view the latest messages first.
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
| **Bubble Sort**     | O(n²)           | O(1)            | Iteratively compares and swaps adjacent elements. Easy to grasp, but inefficient for large datasets. | [bubble_sort.py](sorting_algorithms/bubble_sort.py) |
| **Insertion Sort**  | O(n²)           | O(1)            | Inserts elements into their correct position. Great for nearly sorted or small datasets. | [insertion_sort.py](sorting_algorithms/insertion_sort.py) |
| **Selection Sort**  | O(n²)           | O(1)            | Selects the smallest remaining element and places it at the correct position. Simple but not optimal. | [selection_sort.py](sorting_algorithms/selection_sort.py) |
| **Quick Sort**      | O(n²)           | O(log n)        | Uses a pivot to partition data and recursively sort subarrays. Fast in practice; core of many libraries. | [quick_sort.py](sorting_algorithms/quick_sort.py) |
| **Merge Sort**      | O(n log n)      | O(n)            | Divide-and-conquer algorithm that splits, sorts, and merges. Reliable and stable. | [merge_sort.py](sorting_algorithms/merge_sort.py) |
| **Timsort**         | O(n log n)      | O(n)            | Hybrid of Merge and Insertion Sort; Python’s built-in `sort()` is based on this. Adaptive and production-ready. | [timsort.py](sorting_algorithms/timsort.py) |

## 🔃 Sorting Algorithms
Sorting algorithms reorder elements based on specific rules. This module includes:

1. Bubble Sort
Compares adjacent elements and swaps if they’re out of order. Best for small or nearly sorted datasets.
Time: O(n) best, O(n²) average/worst
Space: O(1)
📂 Implementation

2. Insertion Sort
Builds a sorted list by inserting elements into their correct position.
Time: O(n) best, O(n²) average/worst
Space: O(1)
📂 Implementation

3. Selection Sort
Selects the smallest (or largest) element and places it at the front.
Time: O(n²) all cases
Space: O(1)
📂 Implementation

4. QuickSort
Uses a pivot to partition and recursively sort. Fast in practice.
Time: O(n log n) best/avg, O(n²) worst
Space: O(log n)
📂 Implementation

5. Merge Sort
Divide-and-conquer strategy that splits and merges sorted halves. Stable and predictable.
Time: O(n log n) all cases
Space: O(n)
📂 Implementation

6. TimSort
Hybrid of Merge Sort and Insertion Sort. Built for real-world data.
Time: O(n) best, O(n log n) average/worst
Space: O(n)
📂 Implementation


### Key Sorting Concepts

- **Stability**: Does the algorithm maintain the relative order of equal elements? (e.g., Merge Sort: ✔️, Quick Sort: ❌)
- **In-Place**: Does it sort within the original structure using minimal extra memory?
- **Divide and Conquer**: Efficient strategy used by Merge and Quick Sort to reduce problem size.

---

## Searching Algorithms

Searching is about **locating specific data within a dataset**. Depending on whether the data is sorted, different strategies are more effective.

| Algorithm       | Time Complexity | Requirement    | Overview | Code |
|----------------|------------------|----------------|----------|------|
| **Linear Search**   | O(n)          | None           | Scans each element in sequence. Straightforward but inefficient for large datasets. | [linear_search.py](searching_algorithms/linear_search.py) |
| **Binary Search**   | O(log n)      | Sorted Data    | Repeatedly splits the dataset in half to narrow down the search. Fast and efficient. | [binary_search.py](searching_algorithms/binary_search.py) |

### Key Searching Concepts

- **Sorted Data Requirement**: Binary Search only works when data is sorted. Sorting first can significantly improve search speed in large datasets.
- **Recursive vs Iterative**: Binary Search is implemented both recursively (clean, elegant) and iteratively (efficient, stack-safe).

---

## Real-World Applications

See how sorting and searching play out in everyday systems:

1. **[Coffee Order System](real_world_examples/coffee_order_system.py)**  
   - Sort orders by total price or timestamp.
   - Search by customer name or order ID.
   - Built using MVC (Model-View-Controller) for clarity and scalability.

2. **[Library System](real_world_examples/library_system.py)**  
   - Sort books by title, author, or availability.
   - Search for a book by ISBN or keyword.
   - Incorporates classes like `Book`, `Member`, and a central `LibraryController`.

3. **[Album Management Tool](real_world_examples/album_management.py)**  
   - Sorts albums using Python’s `key` parameter with custom comparators.
   - Searches by album name or artist.
   - Object-Oriented approach using magic methods like `__lt__` and `__eq__`.

---

## Complexity Analysis

To choose the right algorithm, you must understand its performance in terms of **Big O** notation. Review the [complexity guide](docs/complexity.md) for visual charts and examples:

- **O(1)**: Constant time (e.g., direct index access)
- **O(log n)**: Logarithmic (e.g., Binary Search)
- **O(n)**: Linear (e.g., Linear Search)
- **O(n²)**: Quadratic (e.g., Bubble Sort)
- **O(n log n)**: Efficient sorting (e.g., Merge Sort, Quick Sort average case)

---


## Reflections

In [reflections.md](docs/reflections.md), you’ll find personal insights and best-practice tips:
- Use Insertion Sort for tiny, nearly sorted collections.
- Prefer Merge Sort or Timsort for stability and speed on larger datasets.
- Choose Binary Search only when your data is already sorted.
- Think of sorting and searching like real-life activities: organizing your email inbox, finding a name in your contact list, or browsing a playlist.

---

## 📚 Bibliography

- [GeeksforGeeks: Sorting Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#Sorting)  
- [GeeksforGeeks: Searching Algorithms](https://www.geeksforgeeks.org/searching-algorithms/)

- [Python Docs: Data Structures (Lists)](https://docs.python.org/3/tutorial/datastructures.html)  
- [Python Docs: Sorting Techniques](https://docs.python.org/3/howto/sorting.html)  
- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

- [University of Cape Town (2014): Visual Algorithm Tools](https://www.cs.uct.ac.za/Research/DNA/Visualizations/)

- [Dalal (2004): Search Algorithm Examples – ResearchGate](https://www.researchgate.net/publication/221186184_Searching_algorithms_in_inverted_files)

