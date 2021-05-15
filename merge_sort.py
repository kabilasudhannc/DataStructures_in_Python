def merge_sort(sorting_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublist created in previous step
    Combine: Merge the sorted sublist created in previous step

    Takes O(n log n) time
    """
    if len(sorting_list) <= 1:
        return sorting_list

    left_half, right_half = split(sorting_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(sorting_list):
    """
     Divide the unsorted list at midpoint into sublist
     Returns two sublist - left and right
     Takes overall O(log n) time
    """
    mid = len(sorting_list) // 2
    left = sorting_list[: mid]
    right = sorting_list[mid:]
    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    Takes overall O(n) time
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify(sorted_list):
    n = len(sorted_list)

    if n == 0 or n == 1:
        return True

    return sorted_list[0] < sorted_list[1] and verify(sorted_list[1:])


a_list = [23, 61, 1, 2, 63, 7, 3, 9, 54, 66]
result = merge_sort(a_list)
print(verify(result))
