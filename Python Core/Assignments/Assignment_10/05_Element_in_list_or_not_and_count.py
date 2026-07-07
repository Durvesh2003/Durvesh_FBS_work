# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def Ele_in_list(list,num):
    count = 0
    for i in list:
        if i == num:
            count += 1

    if num in list:
        print(f"Element {num} appears {count} times")
    else:
        print(f"element {num} does not appears")
  
    

num = int(input("Enter the number : "))
list = [20,40,20,30,50,10,15,25,45,20]
Ele_in_list(list,num)

