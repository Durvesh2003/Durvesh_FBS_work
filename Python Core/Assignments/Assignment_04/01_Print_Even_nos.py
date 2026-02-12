# 1. WAP to print all even numbers until n.
'''
n = int(input("Enter the number : "))
print("Even Numbers are :", end= ' ')
for i in range (1,n+1):
    if(i%2 == 0):
        print(i,end= ' ')
'''

num = int(input("Enter the number : "))
i = 1
while(i <= num):
    if (i%2 == 0):
        print(i,end= ' ')
    i += 1