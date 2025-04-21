
def bubble_sort(arr):
    """
    Sorts the input list in ascending order using the Bubble Sort algorithm.

    Args:
        arr (list): The list to be sorted (modified in-place).

    Returns:
        list: The sorted list (same as input for convenience).
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize for already sorted lists
        swapped = False
        
        # Last i elements are already in place after each pass
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, the array is already sorted
        if not swapped:
            break
    
    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Bubble Sort behavior
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],  # Random list
        [1, 2, 3, 4, 5],              # Already sorted
        [5, 4, 3, 2, 1],              # Reverse sorted
        [],                            # Empty list
        [1],                           # Single element
    ]
    
    # Run and display results for each test case
    for test in test_cases:
        original = test.copy()  # Preserve original for display
        sorted_list = bubble_sort(test)
        print(f"Input: {original} -> Sorted: {sorted_list}")
