"""
        1
      1   2 
    1       3 
  1           4
1   2   3   4   5
"""
n = int(input("Enter the number : "))
num = 2
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ", end = " " )
    for k in range (1,2* i):
        if(k == 1):
            print("1",end=" ")
        elif(k == 2*i-1):
            print(i,end = " ")
        elif(k%2 != 0 and i == n):
            print(num,end=" ")
            num += 1
        else:
            print(" ", end = " ")
    print()