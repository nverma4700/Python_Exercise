def sort_dict_by_value(dic):
    '''
    Python function that will create and return a dictionary from another dictionary, but sorted by value. 
    You can assume the values are all comparable and have a natural sort order
    '''
    d = {k:v 
         for k,v in sorted(dic.items(), key = lambda x: x[1])
         }
    return d

## Testing: 
# composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
# print(sort_dict_by_value(dic=composers))

def dict_common_element(d1, d2):
    '''
    function that creates a dictionary that contains only the keys common to both dictionaries, 
    with values being a tuple containg the values from `d1` and `d2`. (Order of keys is not important).
    '''
    dic = {}
    common_key = set(d1) & set(d2)
    for key in common_key:
        dic[key] = (d1[key], d2[key])
        
    # OR
    
    # dic = {k: (d1[k], d2[k]) for k in common_key}
    # return dic

## Testing: 
# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
# print(dict_common_element(d1, d2))

def merge_dic(*dicts):
    '''
    You have text data spread across multiple servers.
    Each server is able to analyze this data and return a dictionary that contains words and their frequency.

    Your job is to combine this data to create a single dictionary that contains all the words and their 
    combined frequencies from all these data sources. Bonus points if you can make your dictionary sorted by frequency (highest to lowest).

    For example, you may have three servers that each return these dictionaries:
    '''
    new_dict = {}
    for d in dicts:
        for k,v in d.items():
            if k in new_dict:
                new_dict[k] += v
            else:
                new_dict[k] = v
    sorted_dic = {k:v for k, v in sorted(new_dict.items(), key= lambda x:x[1], reverse=True)}
    return sorted_dic

## Testing: 
# d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
# d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
# d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
# print(data_merge(d1, d2, d3))


def identity(node1, node2, node3):
    '''
    Function to find the unique key in all the dictionary and print out the 
    tuple of their vlaue. If key is not present in certain dictionary, return 
    0 as the value
    '''
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    unique_keys = set(union - intersection)

    result = {k: (node1.get(k,0), node2.get(k,0), node3.get(k,0)) for k in unique_keys}
    return result

## Testing: 
# n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
# n2 = {'employees': 250, 'users': 23, 'user': 230}
# n3 = {'employees': 150, 'users': 4, 'login': 1000}
# print(identity(n1, n2, n3))

