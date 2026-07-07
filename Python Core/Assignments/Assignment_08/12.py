def New_list(lst):
    list2 = []

    for i in lst:
        if i not in list2:
            list2.append(i)
    return list2



lst = [1,2,3,4,5,6.7]
obj=New_list(lst)
print(obj)