# 10. Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = input("Enter the Gender (F/M) :")
age = int(input("Enter the Age :"))
if(age > 0 ):
    # if (gender == 'F'):
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
else :
    print("Invalid")
