# 5. WAP to print Fibonacci series upto n.

n = int(input("Enter the number : "))

a = -1
b = 1 

print(f"fibonacci series of {n} is :",end = ' ')

# Using For

for i in range (1,n+1):
    c = a + b
    print(c,end = ' ' )
    a = b
    b = c


# Using While 
'''
i = 1
while(i<=n):
    c = a + b
    print(c,end = ' ' )
    a = b
    b = c
    i+=1
'''