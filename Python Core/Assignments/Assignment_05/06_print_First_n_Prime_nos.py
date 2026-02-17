# # 6. Write a program to print first n prime numbers.

# 1. Input n
# 2. count = 0
# 3. num = 2
# 4. While count < n:
#        Assume num is prime
#        Check divisibility from 2 to num-1
#        If divisible → Not prime
#        If prime:
#             Print num
#             count += 1
#        num += 1
# 5. End

n = int(input("Enter the number how much u want first n prime nos : "))

count = 0
num= 2

while (count < n):
    for i in range (2, num ):
        if (num % i == 0):
            break
    else :
        print(num, end = " ")
        count += 1
    num += 1