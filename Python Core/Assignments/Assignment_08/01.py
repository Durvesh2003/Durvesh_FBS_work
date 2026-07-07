# 1. Write a program to calculate area of rectangle

def area(l,b):
    area = l*b
    return area

l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle :"))

res = area(l,b)
print(f"Area of rectangle is {res}")