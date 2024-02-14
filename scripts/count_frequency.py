def count_freq(nums):
    '''
    Count a occurrence of all the numbers in the list. 
    Returns number and frequency as a dictionary key-value pair.
    '''
    freq = {}
    for num in nums: 
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

# Testing: --> uncomment below
# nums = [1,2,3,4,1,1,1,2,3,3,3,4,4]
# frequency = count_freq(nums)
# for k,v in frequency.items():
#         print(f'{k} occurs {v} times.')

