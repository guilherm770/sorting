def bubble_sort(array):
    """
    Sorts an input list in ascending order using the Bubble Sort algorithm.

    Parameters:
        array (list): The list to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    n = len(array)

    # Iterate over the list n times
    for i in range(n):
        is_sorted = True  # A flag to check if the list is already sorted

        # Compare adjacent elements and swap them if necessary
        # After each iteration, the largest unsorted element will 'bubble up' to its correct position
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # Swap the elements
                is_sorted = False  # If a swap occurs, the list is not sorted yet

        # If the inner loop didn't perform any swaps, the list is already sorted
        # We can break out of the loop early to save unnecessary iterations
        if is_sorted:
            break

    return array

def get_input_array():
    """
    Asks the user to input a list of space-separated integers.

    Returns:
        list: The user input list of integers.
    """
    input_str = input("Enter a list of space-separated integers: ")
    input_list = [int(num) for num in input_str.split()]
    return input_list

if __name__ == "__main__":
    user_array = get_input_array()
    sorted_array = bubble_sort(user_array)
    print("Sorted Array:", sorted_array)