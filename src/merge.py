def merge(left, right):
    """
    Merges two sorted arrays (left and right) into a single sorted array.

    Args:
        left (list): A sorted list of elements.
        right (list): A sorted list of elements.

    Returns:
        list: A sorted list containing all elements from left and right.
    """
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        array (list): The input list to be sorted.

    Returns:
        list: A sorted list containing all elements from the input array.
    """
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

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
    sorted_array = merge_sort(user_array)
    print("Sorted Array:", sorted_array)