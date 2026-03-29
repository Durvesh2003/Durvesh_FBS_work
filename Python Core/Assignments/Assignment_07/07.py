"""
            1
         1  2  1
      1  2  3  2  1
   1  2  3  4  3  2  1
1  2  3  4  5  4  3  2  1

"""
n = int(input("Enter the number : "))
num = 1
for i in range(1,n+1):

    for j in range(1,n+1-i):
        print(" ",end = " ")
    
    for k in range(1,i+1):
        print(k,end=" ")
    
    for k in range(i,1,-1):
        print(k-1,end= " ")
        
    print()