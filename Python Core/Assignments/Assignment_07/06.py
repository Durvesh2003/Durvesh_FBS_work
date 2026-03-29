"""
1 2 3 4 5
2     5
3   5
4 5
5

"""

n = int(input("Enter the number : "))

for i in range(1,n+1):
    for j in range(1,n+2-i):
        if (i == 1):
            print(j,end=" ")
        elif(j == 1):
            print(i,end= " ")
        elif(j==n+1-i):
            print(n,end=  " ")
        else:
            print(" ",end=" ")
    print()