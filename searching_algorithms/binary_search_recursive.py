"""
Recursive Binary Search Algorithm
================================
This module implements Binary Search using a recursive approach. It efficiently finds a
target in a sorted list by repeatedly dividing the search space in half. The recursive
implementation is clean and elegant but uses O(log n) stack space due to the call stack.

- Time Complexity: O(log n) (best: O(1), average/worst: O(log n))
- Space Complexity: O(log n) due to recursive call stack
- Requirement: Sorted data

The implementation supports a 'key' parameter for attribute-based searches and a 'return_mode'
parameter to control whether the leftmost, rightmost, or all occurrences are returned. A
'verbose' flag enables step-by-step output for educational purposes.

Example:
    # Search for a book by ISBN
    books = [{"isbn": "123", "title": "Book A"}, {"isbn": "456", "title": "Book B"}]
    index = binary_search_recursive(books, "456", key=lambda x: x["isbn"])
    # Result: 1

    # Find all occurrences of a value
    numbers = [1, 2, 2, 2, 3]
    indices = binary_search_recursive(numbers, 2, return_mode="all")
    # Result: [1, 2, 3]
"""

def binary_search_recursive(arr, target, key=None, return_mode="leftmost", verbose=False):
    """
    Searches for the target in a sorted list using recursive Binary Search.

    Args:
        arr (list): The sorted list to search through.
        target: The value to search for.
        key (callable, optional): A function to extract a comparison key from each element.
                                 Defaults to None (direct comparison).
        return_mode (str, optional): Specifies the return behavior:
                                    - "leftmost": Return the first occurrence (default).
                                    - "rightmost": Return the last occurrence.
                                    - "all": Return a list of all matching indices.
        verbose (bool, optional): If True, prints each recursive step for debugging/education.
                                 Defaults to False.

    Returns:
        int or list: Depending on return_mode:
                     - int: Index of the leftmost or rightmost occurrence, or -1 if not found.
                     - list: List of all matching indices (for return_mode="all").

    Raises:
        TypeError: If elements are not comparable with the target or key function is invalid.
        ValueError: If the list is not sorted or return_mode is invalid.
    """
    if not arr:
        return -1 if return_mode != "all" else []  # Early return for empty lists

    # Validate input types
    if key is not None and not callable(key):
        raise TypeError("key must be a callable function")
    if return_mode not in ("leftmost", "rightmost", "all"):
        raise ValueError("return_mode must be 'leftmost', 'rightmost', or 'all'")

    # Validate sorted order (performed once)
    def is_sorted():
        try:
            for i in range(1, len(arr)):
                val_prev = key(arr[i - 1]) if key else arr[i - 1]
                val_curr = key(arr[i]) if key else arr[i]
                if val_prev > val_curr:
                    return False
            return True
        except TypeError as e:
            raise TypeError(f"Elements are not comparable: {e}")

    if not is_sorted():
        raise ValueError("Input list must be sorted in ascending order")

    def search(left, right):
        """Helper function for recursive Binary Search."""
        if left > right:
            return -1 if return_mode != "all" else []

        mid = (left + right) // 2
        try:
            mid_value = key(arr[mid]) if key else arr[mid]

            if verbose:
                print(f"Step: left={left}, right={right}, mid={mid}, mid_value={mid_value}, target={target}")

            if mid_value == target:
                if return_mode == "all":
                    # Collect all occurrences by searching both sides
                    left_matches = search(left, mid - 1) if mid > left else []
                    right_matches = search(mid + 1, right) if mid < right else []
                    matches = left_matches + [mid] + right_matches
                    return sorted(matches)  # Ensure indices are in order
                elif return_mode == "leftmost":
                    # Find the leftmost occurrence
                    if mid == 0 or (key(arr[mid - 1]) if key else arr[mid - 1]) != target:
                        return mid
                    return search(left, mid - 1)
                else:  # rightmost
                    # Find the rightmost occurrence
                    if mid == len(arr) - 1 or (key(arr[mid + 1]) if key else arr[mid + 1]) != target:
                        return mid
                    return search(mid + 1, right)
            elif mid_value < target:
                return search(mid + 1, right)
            else:
                return search(left, mid - 1)
        except TypeError as e:
            raise TypeError(f"Elements are not comparable with target: {e}")

    try:
        result = search(0, len(arr) - 1)
        # Ensure consistent return type for single index
        if return_mode == "all" and isinstance(result, int):
            return [result] if result != -1 else []
        return result
    except TypeError as e:
        raise TypeError(f"Search failed: {e}")

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Recursive Binary Search behavior
    test_cases = [
        ([11, 12, 22, 25, 34, 64, 90], 25, None, "leftmost", False),  # Target present
        ([1, 2, 3, 4, 5], 6, None, "leftmost", False),                # Target absent
        ([1, 2, 2, 2, 3], 2, None, "all", False),                     # Multiple occurrences
        ([], 1, None, "leftmost", False),                             # Empty list
        ([1], 1, None, "rightmost", False),                           # Single element
        ([{"val": 1}, {"val": 2}, {"val": 3}], 2, lambda x: x["val"], "leftmost", False),  # Custom key
        ([1, 2, 2, 2, 3], 2, None, "rightmost", True),                # Verbose mode
        ([1] * 1000, 1, None, "all", False),                          # Large list with duplicates
    ]

    # Run and display results for each test case
    for arr, target, key_func, mode, verbose in test_cases:
        original = arr.copy()  # Preserve original for display
        try:
            result = binary_search_recursive(arr, target, key=key_func, return_mode=mode, verbose=verbose)
            result_str = f"Found at index {result}" if mode != "all" else f"Found at indices {result}"
            print(f"Input: {original}, Target: {target}, Key: {key_func}, Mode: {mode}, Verbose: {verbose}")
            print(f"Result: {result_str}\n")
        except (TypeError, ValueError) as e:
            print(f"Error for input {original}, target {target}: {e}\n")
