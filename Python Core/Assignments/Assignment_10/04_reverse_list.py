# 4. Write a program to reverse the list.

def rev_list(list):
    start = 0
    end = len(list)-1

    while start < end:
        list[start],list[end] = list[end],list[start]

        start += 1
        end -=1
    
    return list

list = [67,20,90,80,76,88,40]
print(rev_list(list))



# list = [67,20,90,80,76,88,40]
# rev = []
# for i in list :
#         rev += [i]

# print(rev)
