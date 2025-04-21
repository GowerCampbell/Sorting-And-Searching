"""
Insertion Sort Algorithm
=======================
This module implements Insertion Sort, a stable and in-place sorting algorithm that builds
a sorted list by inserting each element into its correct position. It is efficient for small
or nearly sorted datasets but inefficient for large datasets due to its O(n²) time complexity.

- Best Case: O(n) when the list is already sorted
- Average/Worst Case: O(n²)
- Space Complexity: O(1)
- Stability: Yes (preserves relative order of equal elements)

The implementation supports custom comparators via 'key' and 'reverse' parameters, similar
to Python's sorted() function, for flexible sorting.
"""

def insertion_sort(arr, key=None, reverse=False):
    """
    Sorts the input list in ascending or descending order using Insertion Sort.

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

    # Traverse through elements starting from the second element
    for i in range(1, len(arr)):
        # The element to be inserted
        key_element = arr[i]
        key_value = key(key_element) if key else key_element
        
        # Find the correct position in the sorted portion
        j = i - 1
        
        # Shift elements that are greater (or smaller if reverse=True) than key
        try:
            while j >= 0:
                current_value = key(arr[j]) if key else arr[j]
                if reverse:
                    if current_value < key_value:
                        break
                else:
                    if current_value > key_value:
                        break
                arr[j + 1] = arr[j]  # Shift element to the right
                j -= 1
        except TypeError as e:
            raise TypeError(f"Elements are not comparable: {e}")
        
        # Place the key in its correct position
        arr[j + 1] = key_element
    
    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Insertion Sort behavior
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
            sorted_list = insertion_sort(test, key=key_func, reverse=rev)
            print(f"Input: {original} -> Sorted: {sorted_list} (key={key_func}, reverse={rev})")
        except TypeError as e:
            print(f"Error for input {original}: {e}")
        sorted_list = insertion_sort(test)
        print(f"Input: {original} -> Sorted: {sorted_list}")
