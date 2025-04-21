"""
Selection Sort Algorithm
=======================
This module implements Selection Sort, a simple in-place sorting algorithm that repeatedly
selects the smallest (or largest) element from the unsorted portion and places it at the
beginning. It is not stable and inefficient for large datasets due to its O(n²) time complexity.

- Best Case: O(n²) (no optimization for sorted lists)
- Average/Worst Case: O(n²)
- Space Complexity: O(1)
- Stability: No (swaps may disrupt relative order of equal elements)

The implementation supports custom comparators via 'key' and 'reverse' parameters, similar
to Python's sorted() function, for flexible sorting.
"""

def selection_sort(arr, key=None, reverse=False):
    """
    Sorts the input list in ascending or descending order using Selection Sort.

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

    n = len(arr)
    
    # Traverse through all elements
    for i in range(n):
        # Find the minimum (or maximum if reverse=True) element in unsorted portion
        min_index = i
        for j in range(i + 1, n):
            try:
                # Use key function if provided, otherwise compare directly
                val_j = key(arr[j]) if key else arr[j]
                val_min = key(arr[min_index]) if key else arr[min_index]
                
                # Compare based on reverse flag
                if reverse:
                    if val_j > val_min:
                        min_index = j
                else:
                    if val_j < val_min:
                        min_index = j
            except TypeError as e:
                raise TypeError(f"Elements are not comparable: {e}")
        
        # Swap the found minimum/maximum element with the first element of unsorted portion
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Selection Sort behavior
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
            sorted_list = selection_sort(test, key=key_func, reverse=rev)
            print(f"Input: {original} -> Sorted: {sorted_list} (key={key_func}, reverse={rev})")
        except TypeError as e:
            print(f"Error for input {original}: {e}")
