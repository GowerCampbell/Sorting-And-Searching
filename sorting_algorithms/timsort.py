"""
Timsort Algorithm (Simplified)
=============================
This module implements a simplified version of Timsort, a hybrid sorting algorithm derived
from Merge Sort and Insertion Sort. It is designed for real-world data, leveraging natural
runs and using Insertion Sort for small segments and Merge Sort for merging. Timsort is
stable and adaptive, powering Python's built-in sort() and sorted() functions.

- Best Case: O(n) for nearly sorted data
- Average/Worst Case: O(n log n)
- Space Complexity: O(n) for merging
- Stability: Yes (preserves relative order of equal elements)

This implementation simplifies Timsort by using a fixed run size and basic merging, omitting
advanced optimizations like galloping or dynamic run sizing for clarity. It supports custom
comparators via 'key' and 'reverse' parameters, similar to Python's sorted() function.
"""

def timsort(arr, key=None, reverse=False):
    """
    Sorts the input list in ascending or descending order using a simplified Timsort.

    Args:
        arr (list): The list to be sorted (modified in-place).
        key (callable, optional): A function to extract a comparison key from each element.
                                 Defaults to None (direct comparison).
        reverse (bool, optional): If True, sort in descending order. Defaults to False.

    Returns:
        list: The sorted list (same as input for convenience).

    Raises:
        TypeError: If elements are not comparable or key function is invalid.
    """
    if not arr:
        return arr  # Early return for empty lists

    # Validate input types
    if key is not None and not callable(key):
        raise TypeError("key must be a callable function")

    MIN_RUN = 32  # Minimum run size for Insertion Sort (typical range: 32–64)

    def insertion_sort(start, end):
        """Sorts a small segment of the array using Insertion Sort."""
        for i in range(start + 1, end + 1):
            key_element = arr[i]
            key_value = key(key_element) if key else key_element
            j = i - 1

            try:
                while j >= start:
                    current_value = key(arr[j]) if key else arr[j]
                    if reverse:
                        if current_value < key_value:
                            break
                    else:
                        if current_value > key_value:
                            break
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key_element
            except TypeError as e:
                raise TypeError(f"Elements are not comparable: {e}")

    def merge(left, right):
        """Merges two sorted arrays into a single sorted array."""
        result = []
        i = j = 0

        try:
            while i < len(left) and j < len(right):
                left_val = key(left[i]) if key else left[i]
                right_val = key(right[j]) if key else right[j]

                if reverse:
                    if left_val >= right_val:
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1
                else:
                    if left_val <= right_val:
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1

            result.extend(left[i:])
            result.extend(right[j:])
        except TypeError as e:
            raise TypeError(f"Elements are not comparable: {e}")

        return result

    try:
        # Step 1: Divide array into runs and sort with Insertion Sort
        n = len(arr)
        for start in range(0, n, MIN_RUN):
            end = min(start + MIN_RUN - 1, n - 1)
            insertion_sort(start, end)

        # Step 2: Merge runs using Merge Sort
        size = MIN_RUN
        while size < n:
            for left in range(0, n, size * 2):
                mid = min(left + size - 1, n - 1)
                right = min(left + 2 * size - 1, n - 1)
                if mid < right:
                    # Extract left and right runs
                    left_run = arr[left:mid + 1]
                    right_run = arr[mid + 1:right + 1]
                    # Merge runs and update array
                    merged = merge(left_run, right_run)
                    arr[left:left + len(merged)] = merged
            size *= 2

    except TypeError as e:
        raise TypeError(f"Sorting failed: {e}")

    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Timsort behavior
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], None, False),  # Random list, default sorting
        ([1, 2, 3, 4, 5], None, False),               # Already sorted
        ([5, 4, 3, 2, 1], None, True),                # Reverse sorted, descending
        ([], None, False),                             # Empty list
        ([1], None, False),                            # Single element
        ([{"val": 3}, {"val": 1}, {"val": 2}], lambda x: x["val"], False),  # Custom key
        ([1, 2, 3, 10, 9, 8, 7], None, False),        # Partially sorted
    ]

    # Run and display results for each test case
    for test, key_func, rev in test_cases:
        original = test.copy()  # Preserve original for display
        try:
            sorted_list = timsort(test, key=key_func, reverse=rev)
            print(f"Input: {original} -> Sorted: {sorted_list} (key={key_func}, reverse={rev})")
        except TypeError as e:
            print(f"Error for input {original}: {e}")
