"""
QuickSort Algorithm
==================
This module implements QuickSort, an efficient, in-place sorting algorithm that uses a
divide-and-conquer strategy. It selects a pivot, partitions the array around it, and
recursively sorts the subarrays. QuickSort is fast in practice but not stable, with a rare
O(n²) worst-case time complexity.

- Best/Average Case: O(n log n)
- Worst Case: O(n²) (e.g., already sorted list with poor pivot choice)
- Space Complexity: O(log n) due to recursive call stack
- Stability: No (pivoting may disrupt relative order of equal elements)

The implementation supports custom comparators via 'key' and 'reverse' parameters, similar
to Python's sorted() function, and uses the last element as the pivot for simplicity.
"""

def quick_sort(arr, key=None, reverse=False):
    """
    Sorts the input list in ascending or descending order using QuickSort.

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

    def partition(low, high):
        """Partitions the array around a pivot (last element) and returns the pivot index."""
        pivot = arr[high]
        pivot_value = key(pivot) if key else pivot
        i = low - 1  # Index of smaller element

        for j in range(low, high):
            try:
                current_value = key(arr[j]) if key else arr[j]
                # Compare based on reverse flag
                if reverse:
                    if current_value > pivot_value:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                else:
                    if current_value <= pivot_value:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
            except TypeError as e:
                raise TypeError(f"Elements are not comparable: {e}")

        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(low, high):
        """Recursively sorts the array by partitioning and sorting subarrays."""
        if low < high:
            # Find pivot index
            pi = partition(low, high)
            # Recursively sort elements before and after pivot
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)

    # Start QuickSort
    try:
        quick_sort_helper(0, len(arr) - 1)
    except TypeError as e:
        raise TypeError(f"Sorting failed: {e}")

    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate QuickSort behavior
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], None, False),  # Random list, default sorting
        ([1, 2, 3, 4, 5], None, False),               # Already sorted
        ([5, 4, 3, 2, 1], None, True),                # Reverse sorted, descending
        ([], None, False),                             # Empty list
        ([1], None, False),                            # Single element
        ([{"val": 3}, {"val": 1}, {"val": 2}], lambda x: x["val"], False),  # Custom key
    ]

    # Run and display results for each test case
    for test, key_func, rev in test_cases:
        original = test.copy()  # Preserve original for display
        try:
            sorted_list = quick_sort(test, key=key_func, reverse=rev)
            print(f"Input: {original} -> Sorted: {sorted_list} (key={key_func}, reverse={rev})")
        except TypeError as e:
            print(f"Error for input {original}: {e}")
