def check_string_binary(str):
    '''
    Check wheather a given string is binary and return True or False
    '''
    binary = '01'
    count = 0
    for i in str: 
        if i not in binary:
            count += 1
            break
    if count:
        return False
    else:
        return True
    

# Testing: --> uncomment below:
# str1 = 'GeekforGeeks!'
# str2 = "1111111"
# str3 = "001021010001010"
# str4 = "000000000"
# print(check_string_binary(str1))
# print(check_string_binary(str2))
# print(check_string_binary(str3))
# print(check_string_binary(str4))