# merge_sort.py

# Learning Objective:
# - Understand the merge sort algorithm.
# - Modify the algorithm to sort strings by their length in descending order.
# - Gain experience working with lists, loops, and recursive logic in Python.

# Written By Gower Campbell


def merge_sort(items):
    """
    Sorts a list of strings by their length in descending order using merge sort.

    Parameters:
        items (list): The list of strings to be sorted.

    Returns:
        list: The sorted list.
    """
    items_length = len(items)  # Get the length of the input list
    temporary_storage = [None] * items_length  # Create temporary storage for merging
    size_of_subsections = 1  # Initialise the size of subsections to 1

    # Iterate until the size of subsections is less than the length of the list
    while size_of_subsections < items_length:
        # Iterate over the list in steps of size_of_subsections * 2
        for i in range(0, items_length, size_of_subsections * 2):
            # Determine the start and end of the two subsections to merge
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, items_length)
            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, items_length)

            # Initialise pointers for both sections and the temporary storage
            left_index = first_section_start
            right_index = second_section_start
            temp_index = 0

            # Merge the subsections based on string length in descending order
            while left_index < first_section_end or right_index < second_section_end:
                if left_index < first_section_end and right_index < second_section_end:
                    # Compare the lengths of strings in both subsections
                    if len(items[left_index]) > len(items[right_index]):
                        temporary_storage[temp_index] = items[left_index]  # Add the longer string to temporary storage
                        left_index += 1
                    else:
                        temporary_storage[temp_index] = items[right_index]  # Add the other string if it's longer or equal
                        right_index += 1
                    temp_index += 1
                elif left_index < first_section_end:
                    # Add remaining elements from the left section
                    temporary_storage[temp_index] = items[left_index]
                    left_index += 1
                    temp_index += 1
                else:
                    # Add remaining elements from the right section
                    temporary_storage[temp_index] = items[right_index]
                    right_index += 1
                    temp_index += 1

            # Copy the sorted elements back to the original list
            for j in range(temp_index):
                items[first_section_start + j] = temporary_storage[j]

        # Double the size of subsections for the next iteration
        size_of_subsections *= 2

    return items

# Lists
list1 = ["apple", "banana", "kiwi", "orange", "strawberry", "blueberry", "raspberry", "grape", "melon", "pineapple"]
list2 = ["dog", "cat", "elephant", "giraffe", "lion", "tiger", "zebra", "monkey", "kangaroo", "penguin"]
list3 = ["car", "bicycle", "motorcycle", "bus", "truck", "van", "scooter", "train", "airplane", "helicopter"]

# Sort the lists
sorted_list1 = merge_sort(list1)
sorted_list2 = merge_sort(list2)
sorted_list3 = merge_sort(list3)

# Print the sorted lists
print("\n<-----Merge Sort----->")
print("\nSorted List 1:", sorted_list1)
print("\nSorted List 2:", sorted_list2)
print("\nSorted List 3:", sorted_list3)
print("")

# <------Reflections----->

# This task helped me understand how the merge sort algorithm can work to sort 
# strings and number based on custom criteria; [if len(items[left_index]) > 
# len(items[right_index]):] From there i was able to sort ensuring the merge
# function correctly handled the different subsections while maintaining 
# the desired order:
#
# temporary_storage[temp_index] = items[left_index]
#     left_index += 1
# else:
#     temporary_storage[temp_index] = items[right_index]
#     right_index += 1
# temp_index += 1 
# 
# Overall, this was really interesting and I want to make sure I know my
# way around search and sort for future tasks like this.


# <-----Bibliography------>
"""
- GeeksforGeeks: Merge Sort
https://www.geeksforgeeks.org/merge-sort/
- Python Documentation: Lists and Loops:
https://docs.python.org/3/tutorial/introduction.html#lists
"""
