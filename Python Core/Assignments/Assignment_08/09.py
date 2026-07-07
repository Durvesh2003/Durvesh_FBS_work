# 9. Write a program to check if entered number is a palindrome or
# not.

def palindrome(n):
    temp = n
    rev = 0 

    while (temp > 0):
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return rev

n = int(input("Enter the number u want to reverse:"))
res = palindrome(n)

if res == n:
    print("It is palindrome")
else:
    print("Not Palindrome")
