# 3. Write a program to find sum of following series using functions :

# a. 1+ 2 + 3 + 4+..... + n

# def SumOfSeries(n):
#     sum = 0
#     for i in range(n):
#         sum += i
#     return sum

# n = int(input("Enter the number :"))

# res = SumOfSeries(n)

# print(res)

# b. 1!+ 2! + 3! + 4!+..... + n!

def SumOfSeriesOfFact(n):
    sum = 0
    for i in range(1,n+1):
        fact = 1
        for j in range (1,i+1):
            fact *= j
        sum += fact 
    return sum

n = int(input("Enter the number :"))

res = SumOfSeriesOfFact(n)

print(res)

# c. 1^1 + 2^2 + 3^3+ ...... n^n

def SumOfSeriesOfmul(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**i
    return sum

n = int(input("Enter the number :"))

res = SumOfSeriesOfmul(n)

print(res)