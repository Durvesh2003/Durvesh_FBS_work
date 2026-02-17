# 5. Write a program to print prime numbers between 1 to 100.
'''
num = int(input("Enter the number : "))

for i in range(2,num):
    is_prime = True
    

    for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        
    if is_prime:
        print(i, end=" ")
 '''

num = int(input("Enter the number : "))

for i in range(2, num):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
   