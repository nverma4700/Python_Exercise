'''
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed 
characters as space-separated strings on a single line

Sample Input:
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak
'''

test_case = int(input())
if 1<=test_case<=10:
    my_list = list()
    for _ in range(test_case):
        index = input().strip()
        even = ''.join([index[i] for i in range(len(index)) if i % 2 == 0])
        odd = ''.join([index[i] for i in range(len(index)) if i % 2 != 0])
        print(f'{even} {odd}')
