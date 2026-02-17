# WAP to accept year from user and check it it is leap year or not
year = int(input("Enter the Year : "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} is Leap Year")
        else:
            print(f"{year} is Not a Leap")
    else:
        print(f"{year} is Leap Year")
else :
    print(f"{year} is not Leap Year")