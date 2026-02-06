# 7. Write a program to check if user has entered correct userid and password.
User = "Durvesh1001" 
Pass = "Duru@2003"

UserId = input("Enter you UserId :")
Password = input("Enter password :")

if(UserId == User and Password == Pass):
    print("Login Successful.....")
else :
    print("Invalid Credentials.......")