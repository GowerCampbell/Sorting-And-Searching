"""
Bubble Sort Algorithm
====================
This module implements Bubble Sort, a stable and in-place sorting algorithm that repeatedly
compares adjacent elements and swaps them if they are in the wrong order. It is simple but
inefficient for large datasets due to its O(n²) time complexity. The implementation includes
an optimization to exit early if no swaps are needed.

- Best Case: O(n) when the list is already sorted (due to swapped flag)
- Average/Worst Case: O(n²)
- Space Complexity: O(1)
- Stability: Yes (preserves relative order of equal elements)

The implementation supports custom comparators via 'key' and 'reverse' parameters, similar
to Python's sorted() function, for flexible sorting.
"""

def bubble_sort(arr, key=None, reverse=False):
    """
    Sorts the input list in ascending or descending order using Bubble Sort.

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
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize for already sorted lists
        swapped = False
        
        # Last i elements are already in place after each pass
        for j in range(0, n - i - 1):
            try:
                # Use key function if provided, otherwise compare directly
                val_j = key(arr[j]) if key else arr[j]
                val_j_next = key(arr[j + 1]) if key else arr[j + 1]
                
                # Compare based on reverse flag
                if reverse:
                    if val_j < val_j_next:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                else:
                    if val_j > val_j_next:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
            except TypeError as e:
                raise TypeError(f"Elements are not comparable: {e}")
        
        # If no swapping occurred, the array is already sorted
        if not swapped:
            break
    
    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Bubble Sort behavior
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
            sorted_list = bubble_sort(test, key=key_func, reverse=rev)
            print(f"Input: {original} -> Sorted: {sorted_list} (key={key_func}, reverse={rev})")
        except TypeError as e:
            print(f"Error for input {original}: {e}")
