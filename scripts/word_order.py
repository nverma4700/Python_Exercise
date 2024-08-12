'''
You are given n words. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word.
Sample Input: 
4
bcdef
abcdefg
bcde
bcdef

Sample Output: 
3
2 1 1
'''

def word_dictionary(word_list):
    '''
    Return words in list as key and their occurance as values
    '''
    word_dic = {}
    for i in word_list:
        if i in word_dic:
            word_dic[i] += 1
        else:
            word_dic[i] = 1
    return word_dic
    
if __name__ == '__main__':
    n = int(input())
    word_list = []
    for _ in range(n):
        word_list.append(input())
    word_dic = word_dictionary(word_list)
    unique_word = len(word_dic)
    occurance = ' '.join([str(v) for v in word_dic.values()])
    print(unique_word)
    print(occurance)