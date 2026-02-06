# 4. Write a program to input all sides of a triangle and check whether triangle is valid or
# not.

side1 = int(input("Enter the one side of the traingele: "))
side2 = int(input("Enter the second side of the traingle : "))
side3 = int(input("Enter the Third side of the traintgle : "))
if (side1 > 0 and side2 > 0 and side3 > 0):
    if(side1 == side2 and side2 == side3 and side1 == side3):
        print("Traingle is Equilateral Traingle ")
    else:
        print("Traingle is not an Valid Equilateral traingle")
else: 
    print("Invalid since value can be zero for Equilateral traingle")

# Using Angle

angle1 = int(input("Enter the one angle of the traingele: "))
angle2= int(input("Enter the second angle of the traingle : "))
angle3= int(input("Enter the Third angle of the traintgle : "))
if (angle1 == 60 and angle2 == 60 and angle3 == 60 ):
    print("Its an Equilateral Traingle")
else:
    print("Not an equilateral traingle and give correct inputs")
        

