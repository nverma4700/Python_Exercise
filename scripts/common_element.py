def common_element(lst1, lst2):
    '''
    Returns common elements and elements from both list
    '''
    common_element = []
    for elem in lst1:
        if elem in lst2:
            common_element.append(elem)
    
    common_element_1 = list(set(lst1) & set(lst2)) # intersections
    elements_from_both_list = list(set(lst1) | set(lst2)) # union
    
    return common_element, common_element_1, elements_from_both_list

# Testing: --> uncomment below
lst1 = [1,2,4,5,6,7,8]
lst2 = [1,9,6,4,8]
print(common_element(lst1,lst2))