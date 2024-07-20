'''
Task: You are given a string.
Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, d
igits, lowercase and uppercase characters. 

Input Format: 

Outut Format: 
In the first line, print True if
has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False. 

Input: qAz#
Output:
    True
    True
    False
    True
    True
'''

if __name__ == '__main__':
    s = input()
    alphanum = alpha = digit = lower = upper = False
    for i in s:
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.isalnum():
            alphanum = True

    
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)