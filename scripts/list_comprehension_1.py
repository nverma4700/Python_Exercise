'''
You are given three integers x,y,z. Print a list of all possible 
combinations of x,y,z where the sum of x,y,z is not equal to n.
'''
if __name__ == '__main__':
    x = int(input('Enter value for x: '))
    y = int(input('Enter value for y: '))
    z = int(input('Enter value for z: '))
    n = int(input('Enter value for n: '))
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n)]
    print(result)
