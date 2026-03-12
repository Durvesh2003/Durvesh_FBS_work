"""    *
      * *
     *   *
    *     *
   *       *
  *         *
  *         *
   *       *
    *     *
     *   *
      * *
       *
"""

n = int(input("Enter the number : "))

for i in range (1,n+1):

    for j in range(1,n+1-i):
        print(" ",end = " ")

    for k in range(1,2*i):

        if(k==1 or k == 2*i-1):
            print("*",end = " ")
        else:
            print(" ",end = " ")
        
    print()



for i in range(n+1, 1, -1):

    for j in range(1, n+2-i):
        print(" ", end=" ")
    

    for k in range(1,2*i-2):
        if(k == 1 or k == 2*i-3):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    
    print()


