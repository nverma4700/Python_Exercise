def palindrome(string):
    x = string
    y = string[::-1]
    if x == y:
        return f'String: {string} is a palindrome'
    else:
        return f'String: {string} is not a palindrome'