# 7. Write a program to solve the following series :



# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


# a. 1! + 2! + 3! + 4! + .....n!
'''
n = int(input("Enter for first n numbers : "))

count = 0
num = 1
sum = 0

while (count < n):
    fact = 1
    for i in range (1,num+ 1):
        
        fact = fact * i
    sum += fact
    print(f"Factorial_sum after each adding of sum is {sum}")    
    count += 1
    num += 1
print(f"Final answer of sum of n factorials is : {sum}")

'''

# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
'''
n = int(input("Enter for first n numbers : "))

sum = 0
    
for i in range (1,n + 1):
        sum += n**i
        print(f"after each adding of sum is {sum}")    
    
print(f"Final answer  : {sum}")
'''


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

# Output should be for series of first n i.e 5 
                                    #    0/p = 1 2 4 8 16

n = int(input("Enter number of terms : "))

sum = 0
term = 1

for i in range(n):
    sum += term
    term *= 2   # multiply by common ratio (2)

print("Sum of geometric series is :", sum)

    
