def find_rotations(str1, str2):
    '''
    Count the number of rotations it takes left or right 
    to make str1 same as str2 if they are same kind.
    '''
    # Count left rotations:
    l = 0
    # Count right rotations:
    r = 0
    l_str = str1
    r_str = str1
    
    # Checking for left rotations:
    while True: 
        l_str = l_str[-1] + l_str[0:-1]
        if l_str == str2:
            l += 1
            break
        else:
            l += 1
            if l > len(str2):
                break
    
    # Checking for right rotations:
    while True:
        r_str = r_str[1:] + r_str[0]
        if r_str == str2:
            r += 1
            break
        else:
            r += 1
            if r > len(str2):
                break
            
    if l > r:
        rotations = 'right'
    else:
        rotations = 'left'
        
    if l < len(str2) or r < len(str2):
        return f'Took {min(l,r)} {rotations} rotations'
    else:
        return "given strings are not of same kind"
        

# Testing: --> uncomment below:          
# print(find_rotations('ksgee', 'geeks'))