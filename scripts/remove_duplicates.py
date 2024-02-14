def remove_duplicates(numbers):
    '''
    Removes occurrence of elements from the list and return
    a list of unique elements.
    '''
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


# Testing: --> uncomment below
# nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# print(remove_duplicates(nums))