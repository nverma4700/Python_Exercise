def rotate_array(nums,k):
    '''
    Given an integer array nums, rotate the array to the
    right by k steps, where k is non-negative.
    '''
    count = 0
    while count <= k:
        nums.insert(0, nums[-1])
        nums.pop(-1)
        count += 1
    return nums


#Testing: --> Uncomment below
# n1 = [1,2,3,4,5,6,7]
# k1 = 3
# n2 = [-1,-100,3,99]
# k2 = 2
# print(rotate_array(nums=n1, k=k1))
# print(rotate_array(nums=n2, k=k2))