def palindrome(string):
    '''
    Check and return if the string is palidromw or not
    '''
    x = string
    y = string[::-1]
    if x == y:
        return f'String: {string} is a palindrome'
    else:
        return f'String: {string} is not a palindrome'


#Testing:
# if __name__ == "__main__":
#     str1 = "hello"
#     str2 = "madam"
#     print(palindrome(string=str1))
#     print(palindrome(string=str2))