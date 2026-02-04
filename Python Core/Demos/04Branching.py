# Syntax
# if(condition):
#     block of Code

# if
'''
num = int(input("Enter a number : "))
if(num%2 == 0):
    print(f'{num} is an Even Number')       # no output if num is odd
'''
    
# if_else
'''
numm = int(input("Enter a number : "))
if(numm%2 == 0):
    print(f'{numm} is an Even Number')       
else:
    print(f"{numm} is odd number")
'''
    
# WAP to check number is positive or negative
'''
n1 = int(input(" Enter a number : "))
if (n1 > 0):
    print(f"{n1} is a +ve number")
else :
    print(f"{n1} is a -ve number")
'''

# nested if_else
'''
gender = input("Enter the Gender (F/M) :")
age = int(input("Enter the Age :"))

# if (gender == 'F'):\
if gender in ['f','F','Female','female']:
    if (age > 17):
        print("Eligible for marraige")
    else :
        print("complete study")
else :
    if (age > 20):
        print("Eligible for marriage")
    else :
        print("complete study")
'''

# Check person is eligible to vote or not
'''
Age = int(input("Enter the Age :"))
if (Age > 0):
    if (Age > 17 and Age < 111 ):
        print("person is Eligible to vote")
    # elif (Age > 110):
    #     print("Invalid Age")
    else :
        print("Not Eligible to vote")
else :
    print ("Invalid Age")
'''

# if_else Ladder

num1 = int(input("Enter the Number : "))
if (num1 < 0):
    print(f"Number is negative")
elif (num1 == 0):
    print("Number is neutral")
else :
    print("Number is Positive")