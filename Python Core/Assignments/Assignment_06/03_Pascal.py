"""
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

"""
n = int(input("Enter the number : "))

for i in range(1,n):
    for j in range(1,n+1-i):
        print("*",end = " ")
    print()