'''
Convert all lowercase letters to uppercase letters and vice versa.

Example: 
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''
def swap_case(s):
    new_s = ''
    for i in s:
        if i == i.lower():
            i = i.upper()
            new_s += i
        else:
            i = i.lower()
            new_s += i
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)