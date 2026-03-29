"""
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
"""
n = int(input("Enter the number : " ))

for i in range(1,n+1):
    
    for j in range(1,n+1-i):
        print("*",end = " ")
    
    for k in range(i,2*i):
        print(k,end= " ")

    for k in range(2*i-2, i-1, -1):
        print(k,end=" ")
    
    print()