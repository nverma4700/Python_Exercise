#Find the Runner-Up Score. 
#You are given n scores. Store them in a list and find the score of the runner-up.

# Sample input = 2 3 6 6 5
# Sampls input = 6 6 6 6 6 6 6 6 6 5


if __name__ == '__main__':
    score = input('Enter the score: ')
    arr = list(map(int, score.split()))
    sorted_arr = sorted(arr, reverse=True)
    if len(arr) > 2:
        for i in range(len(arr) -1):
            if sorted_arr[i] != sorted_arr[i+1]:
                runner_up = sorted_arr[i+1]
                break
        if runner_up:
            print(runner_up)
        else:
            print('Runner up not found')
    else:
        print('Length of score list is not sufficient to find the runner-up')


        