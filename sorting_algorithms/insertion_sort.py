def insertion_sort(arr):
    """
    Sorts the input list in ascending order using the Insertion Sort algorithm.

    Args:
        arr (list): The list to be sorted (modified in-place).

    Returns:
        list: The sorted list (same as input for convenience).
    """
    # Traverse through the elements starting from the second element
    for i in range(1, len(arr)):
        # The element to be inserted
        key = arr[i]
        
        # Find the correct position for the key in the sorted portion of the list
        j = i - 1
        
        # Shift elements of arr[0..i-1] that are greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1
        
        # Place the key in its correct position in the sorted portion
        arr[j + 1] = key
    
    return arr

# Example usage and testing
if __name__ == "__main__":
    # Test cases to demonstrate Insertion Sort behavior
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
        sorted_list = insertion_sort(test)
        print(f"Input: {original} -> Sorted: {sorted_list}")
