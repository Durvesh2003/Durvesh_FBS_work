"""
* * * * * 
*       *
*       *
*       *
*       *
* * * * *
"""
n = int(input("Enter the number : "))

for i in range(1,n+2):
    for j in range(1,n+1):
        if(i ==1 or j == 1 or i == n+1 or j == n):
            print("*", end = " ")
        else :
            print( " ", end = " ")
    print()
