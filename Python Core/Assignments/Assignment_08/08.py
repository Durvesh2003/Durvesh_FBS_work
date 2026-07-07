# 8. Write a program find reverse of a number

def reverse(n):
    temp = n
    rev = 0 

    while (temp > 0):
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return rev

n = int(input("Enter the number u want to reverse:"))
res = reverse(n)
print(res)