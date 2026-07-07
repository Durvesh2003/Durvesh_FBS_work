# 2. Write a program to find maximum and minimum element in a list.

def max_min(list):
    max_ele = list[0]
    min_ele = list[0]

    for i in list:
        if i > max_ele:
            max_ele = i  

        if i < min_ele:
            min_ele = i          
    return max_ele , min_ele   

    
                   
list = [23,67,20,90,80,76,88,40]
max_val , min_val = max_min(list)
print(f"max = {max_val}\nmin = {min_val}")

