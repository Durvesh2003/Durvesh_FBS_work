def bubble_sort(li):
    size = len(li)
    for i in range(1,size):
        #print(i)
        for j in range(0,size-i):
            #print(j)
            if (li[j] > li[j + 1]):
                li[j] , li[j+1] = li[j+1],li[j]
        
        #print()

li = [60,50,40,30,20,10]
print(f"Before Swapping li : {li}")
bubble_sort(li)
print(f"After swapping li : {li}")