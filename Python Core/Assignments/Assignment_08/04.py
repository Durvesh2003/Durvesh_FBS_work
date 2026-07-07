# 4. Sum of all odd numbers between 1 to n

def SumOfSeriesOf_Odd_num(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 != 0:
            sum += i
    return sum

n = int(input("Enter the number :"))

res = SumOfSeriesOf_Odd_num(n)

print(res)