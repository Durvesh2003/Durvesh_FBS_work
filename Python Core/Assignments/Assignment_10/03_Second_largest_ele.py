# 3. Write a program to find the second largest element in the list.

def Second_largest(list):
    max_ele = float('-inf')
    second_largest_ele = float('-inf')

    for ele in list:
        if ele > max_ele:
            second_largest_ele = max_ele
            max_ele = ele
        elif ele > second_largest_ele and ele != max_ele:
            second_largest_ele = ele
    return second_largest_ele

list = [23,67,20,90,80,76,88,40]
Second_largest_value = Second_largest(list)

print(f"Second Largest Value is b : {Second_largest_value}")