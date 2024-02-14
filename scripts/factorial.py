def factorial(num):
    '''
    Returns a factorial of a given number
    '''
    fac = 1
    if num < 0:
        return 'Factorial of negative number can be computed. Kindly input positive number'
    elif num == 0 or num == 1:
        return 1
    else:
        for number in range(2, num+1):
            fac = number * factorial(number-1)
        return fac

# Testing --> uncomment below
print(factorial(num=5))