def count_dup_with_index(input_list, x):
    '''
    For a input list, returns the occurrence of a given element
    with the index value
    '''
    index = []
    count = 0
    for elem in enumerate(input_list):
        if elem[1] == x:
            index.append(str(elem[0]))
            count += 1
    index = ','.join(index)
    return f"Element '{x}' repeated {count} times at index {index}."


# Testing --> uncomment below:
input_list = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
print(count_dup_with_index(input_list, x=2))