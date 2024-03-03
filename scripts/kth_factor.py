def kthfactor(n: int, k: int) -> int:
    '''
    Consider a list of all factors of n sorted in ascending order, 
    return the kth factor in this list or return -1 if n has less than k factors.
    Example: 
    Input: n = 12, k = 3
    Output: 3
    Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
    '''
    factor = []
    for num in range(1,n+1):
        if n % num == 0:
            factor.append(num) # return a list of all the factors of n
    if k <= len(factor):
        return factor[k-1] # return an index value. 3rd position index is (3-1)
    else:
        return -1
    
#Testing: 
print(kthfactor(16,4))