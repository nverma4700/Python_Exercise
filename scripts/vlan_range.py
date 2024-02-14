from itertools import groupby


def vlan_range(input_list):
    '''
    From a list of number creates a VLAN range. 
    Consecutive numbers of lenght 3 and greate should be seperated by '-'
    2 consecutive number should be seperated by ','
    All non consecutive number shoud be seprated by ','
    '''
    vlan_range_list = []
    '''
    groupby is used to group the elements based on the key
    Key = key=lambda e: e[0]-e[1] --> grouping the elements together based on the 
    differnce between enumerate counter and the index element. Example:
    [1,2,4,7,8] --> group together as (1,2) -1, (4) -2 and, (7,8) -4.
    '''
    for group, member in groupby(enumerate(input_list), key=lambda e: e[0]-e[1]):
        member_list = list(member) # Group is the difference, member are group member
        # Members list as (index, value) Example: [(4, 7), (5, 8), (6, 9)]
        start, end = member_list[0][1], member_list[-1][1] # returns the start and end of the group members index value.
        
        if start == end:
            vlan_range_list.append(str(start))
        else:
            if len(member_list) == 2:
                vlan_range_list.append(f'{start}, {end}')
            else:
                vlan_range_list.append(f'{start}-{end}')
        
    vlan_range = ', '.join(vlan_range_list)
    return vlan_range


# Testing: --> uncomment below
input_list = [1, 3, 4, 5, 7, 8, 9, 11, 15, 16]
print(vlan_range(input_list))
    
                
        
        
        