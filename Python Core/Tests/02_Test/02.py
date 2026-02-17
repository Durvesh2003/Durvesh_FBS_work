
num = int(input("Enter the number : "))

r1 = num % 10
num = num// 10
r2 = num % 10
num = num// 10
r3 = num % 10
num = num// 10

if(r1 == (r2*2) and r1 == (r3/2)):
    print("Yes,You have done it")
else:
    print("Please try again")

