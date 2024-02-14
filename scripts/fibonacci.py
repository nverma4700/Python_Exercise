def fibonacci(n):
    fab_list = [0,1]
    for i in range(1, n):
        fab_list.append(fab_list[i]+fab_list[i-1])
        
    return fab_list


# Testing: --> uncomment below
# print(fibonacci(10))