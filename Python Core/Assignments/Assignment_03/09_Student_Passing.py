# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

Maths = int(input("Enter marks of Maths : "))
Chemistry = int(input("enter the marks of Chemistry : "))
physics = int(input("Enter the marks of Physics : "))
Cp = int(input("Enter the marks of c programming : "))
Mechanics = int(input ("Enter the marks of Mechanics : "))

Total_marks = Maths + Chemistry + physics + Cp + Mechanics

percentage = Total_marks/5

if ( percentage <= 100 and percentage >= 60 ):

    print("Student had pass with First Class")

elif ( percentage < 60 and percentage >= 50):

    print("student had pass with Second Class")

elif (percentage < 50 and percentage >= 40):

    print("student had pass with Third Class")

else :

    print('fail')

