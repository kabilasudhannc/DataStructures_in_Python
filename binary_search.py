def binary_search(searching_list, target):
    first = 0
    last = len(searching_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if searching_list[midpoint] < target:
            first = midpoint + 1
        elif searching_list[midpoint] > target:
            last = midpoint - 1
        elif searching_list[midpoint] == target:
            return midpoint

    return None


def verify(index):
    if index is not None:
        print("Target was found in the index:", index)
    else:
        print("Target was not found in the list")


numbers = [num for num in range(1, 11)]
print(numbers)
result = binary_search(numbers, 4)
verify(result)
