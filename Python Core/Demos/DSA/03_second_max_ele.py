li = [45,32,89,56,21,90,42,77,90]

max = li[0]

smax = 0

for i in range(len(li)):
    if li[i] > max:
        smax = max
        max = li[i]
    elif(li[i]> smax) and li[i] != max:
        smax = li[i]
print(f'max:{max} , smax :{smax}')