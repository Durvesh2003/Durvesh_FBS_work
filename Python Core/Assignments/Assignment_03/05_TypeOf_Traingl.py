# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
side1 = int(input("Enter the one side of the traingele: "))
side2 = int(input("Enter the second side of the traingle : "))
side3 = int(input("Enter the Third side of the traintgle : "))

if (side1 > 0 and side2 > 0 and side3 > 0):

    if (side1+side2 > side3  and side1+side2 > 3 and side2+side3 > side1):
        
        if(side1 == side2 and side2 == side3 and side1 == side3):
            print("Traingle is Equilateral Traingle ")
        
        elif (side1 == side2 or side2 == side3 or side1 == side3 ):
            print("Traingle is Isoceles Traingle")
        
        else:
            print("traingle is Scalene Traingle")

    else:
        print("Not a Traingle")
        
else:
    print("Invalid values for checking Traingle")