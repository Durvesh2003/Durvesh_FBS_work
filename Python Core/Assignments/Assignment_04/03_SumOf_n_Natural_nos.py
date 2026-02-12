# 3. WAP to print sum of series upto n.

#Using For loop

num = int(input("Enter the number : "))

sum= 0

for i in range(1,num+1):
    sum += i

print(f"Sum of series of n number is : {sum}")


# Using While Loop

n = int(input("Enter the number : "))
Sum = 0
i = 1
while(i<=n):
    Sum += i
    i+=1
print(f"Sum is : {Sum}")