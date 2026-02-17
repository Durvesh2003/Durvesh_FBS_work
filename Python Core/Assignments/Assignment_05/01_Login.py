# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

Correct_UserId = "Admin123"
Correct_pass = "Durvesh1234"

for i in range(1,4):

    userId = input("Enter The Username : ")
    password = input("Enter Password : ")

    if (userId == Correct_UserId and password == Correct_pass):
        print("Login Successfull")
        break
    
else :
    print("Wrong Credentials")
    print("Login Failed !!! ")