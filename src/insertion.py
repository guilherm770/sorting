def insertion_sort(array):
    """
    Sorts the input array using the insertion sort algorithm.

    Insertion sort is a simple sorting algorithm that works by building
    a sorted portion of the array, and repeatedly inserting unsorted
    elements into the correct position within that sorted portion.

    Args:
        array (list): The list of comparable elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """

    # Iterate through the array, starting from the second element (index 1)
    for i in range(1, len(array)):

        # Get the current element to be compared
        key_item = array[i]

        # Initialize a variable to track the position to insert the key item
        j = i - 1

        # Move elements of the sorted portion to the right to make space for the key item
        # while the current element is smaller than the key item
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        # Insert the key item into its correct position in the sorted portion
        array[j + 1] = key_item

    # Return the sorted array
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
    sorted_array = insertion_sort(user_array)
    print("Sorted Array:", sorted_array)