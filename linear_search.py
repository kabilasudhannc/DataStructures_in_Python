def linear_search(searching_list, target):
    """
    :param searching_list: takes the searching list form the user
    :param target: takes the target element from the user
    :return: Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(searching_list)):
        if searching_list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print('Target was found in index: ', index)
    else:
        print('Target was not found in the list')


numbers = [i for i in range(1, 11)]
result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 10)
verify(result)
