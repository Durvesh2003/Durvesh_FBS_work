# 1. Write a program to find sum of all elements of list

def Sum_of_List(list):

    sum = 0

    for i in list:
        sum += i
    return sum

list = [1,2,3,4,5,6,7]

total_sum = Sum_of_List(list)

print(total_sum)