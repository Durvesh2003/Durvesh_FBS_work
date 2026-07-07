li = [45,32,89,56,21,90,42,77,90]


# if len(li) == 0 :
#     print(f"max is 0")
# elif len(li) != 0:


max = li[0]
smax = 0

for i in range(len(li)):
    if li[i] > max:
        smax = max
        max = li[i]
    elif(li[i]> smax) and li[i] != max:    # This is used for negative value and duplicate value in list
        smax = li[i]
print(f'max:{max} , smax :{smax}')