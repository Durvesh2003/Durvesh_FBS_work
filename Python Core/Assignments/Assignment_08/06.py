# 6. Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacci(n):
    a = 0
    b = 1

    if n<= 0:
        print("Please Enter positive Integer ")
    elif n == 1:
        print(a)
    else :
        print ("Fibonacci series is")
        print(a,b,end = " ")
        for i in range(2,n):
            c = a + b
            print (c,end = " ")
            a = b
            b = c
        
n = int(input("Enter the number:"))

fibonacci(n)

