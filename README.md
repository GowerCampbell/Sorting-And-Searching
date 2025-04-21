# 🧠 Sorting and Searching Learning Module

Welcome to the **Sorting and Searching Learning Module** — a hands-on guide to mastering two foundational concepts in computer science. Curated by *Gower Campbell*, this repository walks you through key algorithms, real-world applications, and complexity insights — all using clean, modular Python.

Whether you're new to coding or revisiting the basics, this module aims to make sorting and searching intuitive, practical, and engaging.

---

## 📚 Table of Contents

1. [📌 Introduction](#introduction)
2. [🔀 Sorting Algorithms](#sorting-algorithms)
3. [🔍 Searching Algorithms](#searching-algorithms)
4. [🌍 Real-World Applications](#real-world-applications)
5. [📊 Complexity Analysis](#complexity-analysis)
6. [🧱 Data Structures](#data-structures)
7. [🧠 Reflections](#reflections)
8. [📦 How to Use This Repository](#how-to-use-this-repository)
9. [📖 Bibliography](#bibliography)

---

## 📌 Introduction

Sorting and searching power everything from database queries to recommendation engines. At their core:

- **Sorting**: Organizes data in a specific sequence (ascending, descending, or custom).
- **Searching**: Retrieves specific data from a dataset, structured or unstructured.

**Examples:**
- Sort emails by date ➜ view latest messages first.
- Search your music library ➜ find a track in seconds.

This module explores:

✔️ Popular algorithms  
✔️ Real-world use cases (e.g., cafés, libraries, music apps)  
✔️ Time-space trade-offs  
✔️ Clean Python implementations (MVC pattern)

---

## 🔀 Sorting Algorithms

Sorting transforms unordered data into a predictable structure. Here's what you'll explore:

| Algorithm         | Worst Time   | Space    | Summary                                                                 | Code |
|------------------|--------------|----------|-------------------------------------------------------------------------|------|
| **Bubble Sort**     | O(n²)       | O(1)     | Swaps adjacent elements iteratively. Simple but inefficient.            | [bubble_sort.py](sorting_algorithms/bubble_sort.py) |
| **Insertion Sort**  | O(n²)       | O(1)     | Inserts elements into correct position. Great for small/nearly sorted.  | [insertion_sort.py](sorting_algorithms/insertion_sort.py) |
| **Selection Sort**  | O(n²)       | O(1)     | Finds the smallest and places it in order. Simple, not optimal.         | [selection_sort.py](sorting_algorithms/selection_sort.py) |
| **Quick Sort**      | O(n²)       | O(log n) | Divide-and-conquer using a pivot. Fast and widely used.                 | [quicksort.py](sorting_algorithms/quicksort.py) |
| **Merge Sort**      | O(n log n)  | O(n)     | Recursively splits, sorts, and merges. Reliable and stable.             | [merge_sort.py](sorting_algorithms/merge_sort.py) |
| **Timsort**         | O(n log n)  | O(n)     | Python’s hybrid built-in sort. Fast, adaptive, and production-ready.    | [timsort.py](sorting_algorithms/timsort.py) |

### 🧠 Key Concepts

- **Stable Sort**: Maintains relative order (e.g., Merge Sort ✔️, Quick Sort ❌)  
- **In-Place**: Minimal memory usage  
- **Divide & Conquer**: Solves via recursive problem partitioning

---

## 🔍 Searching Algorithms

Searching finds **target values** in datasets. Depending on sorting, different techniques apply.

| Algorithm         | Time       | Requirement   | Summary                                                             | Code |
|------------------|------------|---------------|---------------------------------------------------------------------|------|
| **Linear Search**   | O(n)     | None          | Scans sequentially. Simple but slow for large data.                 | [linear_search.py](searching_algorithms/linear_search.py) |
| **Binary Search**   | O(log n) | Sorted Data   | Halves search space each step. Fast and efficient.                  | [binary_search.py](searching_algorithms/binary_search.py) |

📂 **Also see:** [Recursive Binary Search](searching_algorithms/binary_search_recursive.py)

### 🔎 Concepts to Know

- **Sorted data is key** for binary search.  
- **Recursive vs Iterative**: Recursive = cleaner, Iterative = stack-safe.

---

## 🌍 Real-World Applications

### ☕ [Coffee Order System](examples/coffeeordersystem.py)
- Sort orders by timestamp or total.
- Search by customer name or ID.
- Built using MVC pattern.

### 📚 [Library System](examples/libary_system.py)
- Sort books by title, author, or availability.
- Search by ISBN or keyword.
- Uses `Book`, `Member`, and `LibraryController` classes.

### 🎵 [Album Manager](examples/album_system.py)
- Custom sorting via `key` functions.
- Search albums by name or artist.
- OOP design using `__lt__`, `__eq__`, etc.

---

## 📊 Complexity Analysis

Big O notation describes **how an algorithm’s performance scales** with input size — crucial for assessing efficiency and scalability.

### 🔍 Common Time Complexities

| Big O        | Name              | Description                                | Example                       |
|--------------|-------------------|--------------------------------------------|-------------------------------|
| O(1)         | Constant Time     | Same time regardless of input              | `arr[0]`                      |
| O(log n)     | Logarithmic       | Reduces problem size each step             | Binary Search                 |
| O(n)         | Linear            | Grows linearly with input                  | Linear Search                 |
| O(n log n)   | Linearithmic      | Slightly faster than quadratic             | Merge Sort, QuickSort (avg)   |
| O(n²)        | Quadratic         | Slows drastically with large data          | Bubble, Selection Sort        |

### 📈 Performance Table

| Algorithm         | Best       | Average     | Worst       |
|------------------|------------|-------------|-------------|
| **Bubble Sort**     | O(n)      | O(n²)       | O(n²)       |
| **Insertion Sort**  | O(n)      | O(n²)       | O(n²)       |
| **Selection Sort**  | O(n²)     | O(n²)       | O(n²)       |
| **QuickSort**       | O(n log n)| O(n log n)  | O(n²)       |
| **Merge Sort**      | O(n log n)| O(n log n)  | O(n log n)  |
| **TimSort**         | O(n)      | O(n log n)  | O(n log n)  |
| **Linear Search**   | O(1)      | O(n)        | O(n)        |
| **Binary Search**   | O(1)      | O(log n)    | O(log n)    |

> 💡 **Explore sorting visually**:  
> 🎨 [sortvisualizer.com](https://sortvisualizer.com)

---

## 🧱 Data Structures

Efficient algorithms need the right structures. Here are the basics you'll work with:

### 📋 Lists
Dynamic arrays. Fast indexing and iteration.  
🔗 [list_operations.py](data_structures/list_operations.py)

### 📦 Stacks
**LIFO**: Last-In, First-Out. Used in undo features, expression parsing.  
🔗 [stack.py](data_structures/stack.py)

### 🚶 Queues
**FIFO**: First-In, First-Out. Used in simulations, print jobs, task queues.  
🔗 [queue.py](data_structures/queue.py)

---

## 🧠 Reflections

In [reflections.md](docs/reflection.md), explore hands-on lessons and best practices:

- ✔️ Use Insertion Sort for small/narrowly sorted data  
- 🚀 Merge Sort or Timsort = reliable for large, stable sorting  
- ⚠️ Binary Search? Only when data is sorted  
- 🔍 Think real-world: sorting contacts, searching playlists, etc.

---

## 📖 Bibliography

- [GeeksforGeeks: Sorting Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#Sorting)  
- [GeeksforGeeks: Searching Algorithms](https://www.geeksforgeeks.org/searching-algorithms/)  
- [Python Docs: Data Structures (Lists)](https://docs.python.org/3/tutorial/datastructures.html)  
- [Python Docs: Sorting Techniques](https://docs.python.org/3/howto/sorting.html)  
- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
- [UCT Visual Tools](https://www.cs.uct.ac.za/Research/DNA/Visualizations/)  
- [Dalal (2004) - Search Algorithms](https://www.researchgate.net/publication/221186184_Searching_algorithms_in_inverted_files)



