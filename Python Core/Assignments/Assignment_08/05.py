# 5. Sum of all prime numbers between 1 to n

def SumOfSeriesOfFact(n):
    sum = 0
    for i in range(2,n+1):
        
        for j in range (2,i):
            if i % j == 0:
                 break
        else:
            sum += i
        
            
    return sum

n = int(input("Enter the number :"))

res = SumOfSeriesOfFact(n)

print(res)