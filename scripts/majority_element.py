from collections import Counter


def majority_element(nums):
    '''
    Takes a list of number, return a number that's
    occurring more than n/2 times
    '''
    counter = Counter(nums)
    majority_elem = {}
    for k, v in counter.items():
        if v >= (len(nums)/2):
            majority_elem[k] = v
    if majority_elem:
        return f'Major element occurrence is :{list(majority_elem.keys())[0]}'
    return 'No element with occurrence equal or more than n/2 found in the given list.'


# Testing:--> Uncomment below
# if __name__ == '__main__':
#     nums1 = [1, 2, 2, 3, 4, 4, 4, 5, 4, 4, 4, 4]
#     nums2 = [1, 2, 2, 3, 4, 4, 4, 5]
#     print(majority_element(nums1))
#     print(majority_element(nums2))