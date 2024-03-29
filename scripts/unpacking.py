def sum_of_list(*args):
    '''
    Take list as a argument, unpack list using "*" iterate 
    through all the element of list and return the sum.
    '''
    sum = 0
    for i in args:
        sum += i
    
    return sum

my_list = [1,2,3,4,5]
print(sum_of_list(*my_list))


def dic_unpacking(**kwargs):
    '''
    unpack the dictionary and return the values
    
    '''
    for k, v in kwargs.items():
        print(f'Name is {k}, age is {v} years.')

my_dic = {'John' : 25, 'Sandy': 35}
print(dic_unpacking(**my_dic))