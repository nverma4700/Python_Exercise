'''
String are not mutable. We can't assign a vlaue to a index of a string. 
Task: Read a given string, change the character at a given index and then print the modified string. 
Sample Input:
abracadabra
5 k   

Sample output: 
abrackdabra
'''

def mutate_string(string, pos, char):
    new_s = string[:pos] + char + string[(pos + 1):]
    return new_s


if __name__ == '__main__':
    string = input()
    pos, char = input().split()
    s_new = mutate_string(string, int(pos), char)
    print(s_new)
    