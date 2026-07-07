# 10. Write a program to check if entered year is a leap year or not.

def Leap_year(n):
    if(n%4 == 0 and n%100 != 0) or (n% 400 == 0):
            return "Leap Year"
    return "Not Leap year"


n = int(input("Enter the year"))
res = Leap_year(n)
print(res)