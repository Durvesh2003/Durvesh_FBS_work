# 2. Write a program to calculate area of circle

def area(r):
    area = 3.14 * (r**2)
    return area

r = int(input("Enter the radius of circle:"))


res = area(r)
print(f"Area of circle is {res}")