def palindrome(string):
    '''
    Check and return if the string is palidromw or not
    '''
    x = string
    # Below will return an inverse of a string.
    # Ex: x = 'hello', y will be 'olleh'
    y = string[::-1] # similar to [-1::-1] --> Will start from the last index with a hop of -ve 1
    if x == y:
        return f'String: {string} is a palindrome'
    else:
        return f'String: {string} is not a palindrome'


#Testing: --> Uncomment below
# if __name__ == "__main__":
#     str1 = "hello"
#     str2 = "madam"
#     print(palindrome(string=str1))
#     print(palindrome(string=str2))