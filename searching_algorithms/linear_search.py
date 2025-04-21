"""
Linear Search Algorithm
======================
This module implements Linear Search, a simple searching algorithm that sequentially checks
each element in a list until a match is found or the list is exhausted. It works on both
sorted and unsorted data but is inefficient for large datasets due to its O(n) time complexity.

- Time Complexity: O(n) (best: O(1), average/worst: O(n))
- Space Complexity: O(1)
- Requirement: None (no need for sorted data)

The implementation supports a 'key' parameter to allow searching based on object attributes,
similar to Python's sorting functions, enabling flexible searches in real-world applications.
"""

def linear_search(arr, target, key=None):
    """
    Searches for the target in the input list using Linear Search.

    Args:
        arr (list): The list to search through.
        target: The value to search for.
        key (callable, optional): A function to extract a comparison key from each element.
                                 Defaults to None (direct comparison).

    Returns:
        int: The index of the first occurrence of the target, or -1 if not found.

    Raises:
        TypeError: If elements are not comparable with the target or key function is invalid.
    """
    if not arr:
        return -1  # Early return for empty lists

    # Validate input types
    if key is not None and not callable(key):
        raise TypeError("key must be a callable function")

    # Scan each element in the list
    for i in range(len(arr)):
        try:
            # Use key function if provided, otherwise compare directly
            value = key(arr[i]) if key else arr[i]
            if value == target:
                return i  # Return the first matching index
        except TypeError as e:
            raise TypeError(f"Elements are not comparable with target: {e}")

    return -1  # Target not found

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Linear Search behavior
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], 25, None),           # Random list, target present
        ([1, 2, 3, 4, 5], 6, None),                         # Sorted list, target absent
        ([5, 4, 3, 2, 1], 3, None),                         # Reverse sorted, target present
        ([], 1, None),                                       # Empty list
        ([1], 1, None),                                      # Single element, target present
        ([{"val": 3}, {"val": 1}, {"val": 2}], 1, lambda x: x["val"]),  # Custom key
    ]

    # Run and display results for each test case
    for arr, target, key_func in test_cases:
        original = arr.copy()  # Preserve original for display
        try:
            index = linear_search(arr, target, key=key_func)
            result = f"Found at index {index}" if index != -1 else "Not found"
            print(f"Input: {original}, Target: {target}, Key: {key_func} -> {result}")
        except TypeError as e:
            print(f"Error for input {original}, target {target}: {e}")
