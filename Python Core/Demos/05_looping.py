#  Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("enter the number : "))     # 456

temp = num
rev = 0

while (temp > 0):

    digit = temp % 10

    rev = rev * 10 + digit

    temp = temp // 10


if (rev == num):
    print ("Number is Palindrome")
else : 
    print ("NUmber is not Palindrome")


    