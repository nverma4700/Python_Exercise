def check_armstrong_number(num):
    '''
    Check if the number is armstrong or not
    '''
    sum = 0
    for i in str(num):
        sum += int(i) ** 3
    if num == sum:
        return True
    else: 
        return False
    
print(check_armstrong_number(153))