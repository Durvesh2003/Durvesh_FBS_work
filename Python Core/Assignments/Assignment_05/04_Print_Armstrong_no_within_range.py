# 4. WAP to print Armstrong number within a given range
num = int(input("Enter the number : "))
x = len(str(num))
sum = 0
for i in range (1,num+1):
    r1 = i % 10
    sum += r1 ** x
    i // 10
if (i == num):
    print(f"Number are : {i}")