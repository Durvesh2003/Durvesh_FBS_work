# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.
# Using Sides
side1 = int(input("Enter the one side of the traingele: "))
side2 = int(input("Enter the second side of the traingle : "))
side3 = int(input("Enter the Third side of the traintgle : "))
if (side1 > 0 and side2 > 0 and side3 > 0):
    if (side1+side2 > side3  and side1+side2 > 3 and side2+side3 > side1):
        print(" traingle is valid")
    else :
        print("Traingle is not valid")
else:
    print("Traingle is in valid")


# Using Angles 
angle1 = int(input("Enter the one angle of the traingele: "))
angle2= int(input("Enter the second angle of the traingle : "))
angle3= int(input("Enter the Third angle of the traintgle : "))

if (angle1 > 0 and angle2 > 0 and angle3 > 0 ):
    if(angle1 + angle2 + angle3 == 180):
        print("Traingle is valid")
    else:
        print("Not valid")
else: 
    print("not valid because value should be greater than zero")
