'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically 
and print each name on a new line.

Sample Input: 
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''


if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
    sorted_list = sorted(student_list, key=lambda x: x[1])
    second_lowest_score_list = []
    lowest_score = sorted_list[0][1]
    for i in range(len(sorted_list)-1):
        if sorted_list[i][1] != sorted_list[i+1][1]:
            lowest_score = sorted_list[i][1]
            second_lowest_score = sorted_list[i+1][1]
            break
        else:
            continue
    for i in sorted_list: 
        if i[1] == second_lowest_score:
            second_lowest_score_list.append(i)
    sorted_second_lowest_score_list = sorted(second_lowest_score_list, key=lambda x:x[0])
    
    for i in sorted_second_lowest_score_list:
        print(i[0])