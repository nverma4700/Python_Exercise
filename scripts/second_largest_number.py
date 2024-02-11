def second_largest_number(list):
    largest_number = 1
    second_largest = 1
    for num in list:
        if num > largest_number:
            second_largest = largest_number
            largest_number = num
        elif num > second_largest and num !=largest_number:
            second_largest = num
    return second_largest, largest_number

if __name__ == '__main__':
    list = [1,19,223,4,56,7,8,9]
    print(second_largest_number(list=list))