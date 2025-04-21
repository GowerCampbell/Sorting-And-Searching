"""
Binary Search Algorithm
======================
This module implements Binary Search, an efficient searching algorithm that finds a target
in a sorted list by repeatedly dividing the search space in half. It is fast but requires
the input list to be sorted. Both iterative and recursive implementations are provided, with
the iterative version being stack-safe for large datasets.

- Time Complexity: O(log n) (best: O(1), average/worst: O(log n))
- Space Complexity: O(1) for iterative, O(log n) for recursive due to call stack
- Requirement: Sorted data

The implementation supports a 'key' parameter to allow searching based on object attributes,
similar to Python's sorting functions, enabling flexible searches in real-world applications.
"""

def binary_search_iterative(arr, target, key=None):
    """
    Searches for the target in a sorted list using iterative Binary Search.

    Args:
        arr (list): The sorted list to search through.
        target: The value to search for.
        key (callable, optional): A function to extract a comparison key from each element.
                                 Defaults to None (direct comparison).

    Returns:
        int: The index of the first occurrence of the target, or -1 if not found.

    Raises:
        TypeError: If elements are not comparable with the target or key function is invalid.
        ValueError: If the list is not sorted (basic validation).
    """
    if not arr:
        return -1  # Early return for empty lists

    # Validate input types
    if key is not None and not callable(key):
        raise TypeError("key must be a callable function")

    # Basic validation: Check if list is sorted (for key-based comparison)
    try:
        for i in range(1, len(arr)):
            val_prev = key(arr[i - 1]) if key else arr[i - 1]
            val_curr = key(arr[i]) if key else arr[i]
            if val_prev > val_curr:
                raise ValueError("Input list must be sorted in ascending order")
    except TypeError as e:
        raise TypeError(f"Elements are not comparable: {e}")

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        try:
            # Use key function if provided, otherwise compare directly
            mid_value = key(arr[mid]) if key else arr[mid]

            if mid_value == target:
                # Ensure first occurrence by checking leftward
                while mid > 0:
                    prev_value = key(arr[mid - 1]) if key else arr[mid - 1]
                    if prev_value != target:
                        break
                    mid -= 1
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        except TypeError as e:
            raise TypeError(f"Elements are not comparable with target: {e}")

    return -1  # Target not found

def binary_search_recursive(arr, target, key=None):
    """
    Searches for the target in a sorted list using recursive Binary Search.

    Args:
        arr (list): The sorted list to search through.
        target: The value to search for.
        key (callable, optional): A function to extract a comparison key from each element.
                                 Defaults to None (direct comparison).

    Returns:
        int: The index of the first occurrence of the target, or -1 if not found.

    Raises:
        TypeError: If elements are not comparable with the target or key function is invalid.
        ValueError: If the list is not sorted (basic validation).
    """
    if not arr:
        return -1  # Early return for empty lists

    # Validate input types
    if key is not None and not callable(key):
        raise TypeError("key must be a callable function")

    # Basic validation: Check if list is sorted (for key-based comparison)
    try:
        for i in range(1, len(arr)):
            val_prev = key(arr[i - 1]) if key else arr[i - 1]
            val_curr = key(arr[i]) if key else arr[i]
            if val_prev > val_curr:
                raise ValueError("Input list must be sorted in ascending order")
    except TypeError as e:
        raise TypeError(f"Elements are not comparable: {e}")

    def search(left, right):
        """Helper function for recursive Binary Search."""
        if left > right:
            return -1

        mid = (left + right) // 2
        try:
            mid_value = key(arr[mid]) if key else arr[mid]

            if mid_value == target:
                # Ensure first occurrence by checking leftward
                while mid > 0:
                    prev_value = key(arr[mid - 1]) if key else arr[mid - 1]
                    if prev_value != target:
                        break
                    mid -= 1
                return mid
            elif mid_value < target:
                return search(mid + 1, right)
            else:
                return search(left, mid - 1)
        except TypeError as e:
            raise TypeError(f"Elements are not comparable with target: {e}")

    return search(0, len(arr) - 1)

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Binary Search behavior
    test_cases = [
        ([11, 12, 22, 25, 34, 64, 90], 25, None),           # Sorted list, target present
        ([1, 2, 3, 4, 5], 6, None),                         # Sorted list, target absent
        ([1, 2, 2, 2, 3], 2, None),                         # Multiple occurrences
        ([], 1, None),                                       # Empty list
        ([1], 1, None),                                      # Single element, target present
        ([{"val": 1}, {"val": 2}, {"val": 3}], 2, lambda x: x["val"]),  # Custom key
    ]

    # Run and display results for each test case
    for arr, target, key_func in test_cases:
        original = arr.copy()  # Preserve original for display
        try:
            # Test iterative version
            index_iter = binary_search_iterative(arr, target, key=key_func)
            result_iter = f"Found at index {index_iter}" if index_iter != -1 else "Not found"
            # Test recursive version
            index_rec = binary_search_recursive(arr, target, key=key_func)
            result_rec = f"Found at index {index_rec}" if index_rec != -1 else "Not found"
            print(f"Input: {original}, Target: {target}, Key: {key_func}")
            print(f"Iterative: {result_iter}, Recursive: {result_rec}")
        except (TypeError, ValueError) as e:
            print(f"Error for input {original}, target {target}: {e}")
