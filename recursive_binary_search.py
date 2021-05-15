def recrusive_binary_search(searching_list, target):
    if len(searching_list) == 0:
        return False
    else:
        mid = len(searching_list) // 2
        if searching_list[mid] == target:
            return True
        else:
            if searching_list[mid] > target:
                return recrusive_binary_search(searching_list[:mid], target)
            elif searching_list[mid] < target:
                return recrusive_binary_search(searching_list[mid + 1:], target)


def verify(result):
    print('Target Found:', result)


numbers = [num for num in range(1, 11)]
result = recrusive_binary_search(numbers, 11)
verify(result)
