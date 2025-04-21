"""
Merge Sort Algorithm
===================
This module implements Merge Sort, a stable and efficient sorting algorithm that uses a
divide-and-conquer strategy. It recursively splits the array into halves, sorts them, and
merges the sorted halves. Merge Sort is reliable with consistent O(n log n) time complexity
but requires O(n) extra space.

- Best/Average/Worst Case: O(n log n)
- Space Complexity: O(n) for temporary arrays
- Stability: Yes (preserves relative order of equal elements)

The implementation supports custom comparators via 'key' and 'reverse' parameters, similar
to Python's sorted() function, for flexible sorting.
"""

def merge_sort(arr, key=None, reverse=False):
    """
    Sorts the input list in ascending or descending order using Merge Sort.

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

    def merge(left, right):
        """Merges two sorted arrays into a single sorted array."""
        result = []
        i = j = 0

        try:
            while i < len(left) and j < len(right):
                left_val = key(left[i]) if key else left[i]
                right_val = key(right[j]) if key else right[j]

                # Compare based on reverse flag
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

            # Append remaining elements
            result.extend(left[i:])
            result.extend(right[j:])
        except TypeError as e:
            raise TypeError(f"Elements are not comparable: {e}")

        return result

    def merge_sort_helper(arr):
        """Recursively divides and sorts the array."""
        if len(arr) <= 1:
            return arr

        # Split array into two halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        left = merge_sort_helper(left)
        right = merge_sort_helper(right)

        # Merge the sorted halves
        return merge(left, right)

    try:
        # Sort the array and update in-place
        sorted_arr = merge_sort_helper(arr)
        arr[:] = sorted_arr  # Update original array in-place
    except TypeError as e:
        raise TypeError(f"Sorting failed: {e}")

    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Merge Sort behavior
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
            sorted_list = merge_sort(test, key=key_func, reverse=rev)
            print(f"Input: {original} -> Sorted: {sorted_list} (key={key_func}, reverse={rev})")
        except TypeError as e:
            print(f"Error for input {original}: {e}")
