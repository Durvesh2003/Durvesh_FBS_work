def linearSearch(li,search_ele):
    for i in range(0,len(li)):
        if(search_ele == li[i]):
            return i
    else :
        return -1

li = [45,32,89,56,21,90,42,77]
search_ele = int(input("Enter the Element : "))

res = linearSearch(li,search_ele)

if res != -1:
    print(f'{search_ele} is present at index {res}')
else :
    print(f'{search_ele} is not present ')