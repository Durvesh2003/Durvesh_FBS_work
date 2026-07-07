n = int(input("Entre the number: "))


"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
# for i in range (1,n):
#     for j in range(2,i+1):
#         print(' ',end= ' ')
#     for j in range(1,n-i+1):
#         print('*',end=' ')
#     print()

"""
*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * *
"""
for i in range (1,n+1):
    for j in range(1,i+1):
        print('*',end= ' ')
    for j in range(i+1,n*2-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        if(i != n or j != 1):      # or #  if j!=5 :
            print('*',end= ' ')
    print()


# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print( j , end= " ")
    print()

"""
A B C D E 
A B C D 
A B C 
A B 
A 
"""

for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64 + j) , end= " ")
    print()


"""
* * * * *
*       *
*       *
*       *
* * * * *
"""
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or j ==1 or i == 5 or j == 5:
            print("*",end=" ")
        else:
            print(" ",end= " ")
    print()


'''
* * * * * 
* *   * * 
*   *   * 
* *   * * 
* * * * * 
'''
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or j ==1 or i == 5 or j == 5 or i == j or i+j == 6:
            print("*",end=" ")
        else:
            print(" ",end= " ")
    print()

'''
* * * * * 
*     * 
*   * 
* * 
* 
'''
for i in range(1,n+1):
    for j in range(1,n+2-i):
        if (i==1 or j==1 or i+j==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
5 4 3 2 1 
4     1 
3   1 
2 1 
1 
"""
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        if i == 1 or j ==1 or i+j == 6:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

#  1 + 1 2 + 1 2 3 + 1 2 3 4 
'''
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    if i != 4:
        print("+",end=" ")
'''


'''
* * * * * 
$ $ $ $ $ 
* * * * * 
$ $ $ $ $ 
* * * * * 
'''
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i%2 == 0):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()


'''
* $ * $ * 
$ * $ * $ 
* $ * $ * 
$ * $ * $ 
* $ * $ * 
'''
for i in range(1,n+1):
    for j in range(1,n+1):
        if((i+j)%2 == 0):
            print("*",end=" ")
        else:
            print("$",end=" ")
    print()

"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,n+2-i):
        print("*",end=" ")
    print()
    
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''    
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()

'''
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,n+2-i):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
    

'''
* * * * * 
  * * * * 
    * * * 
      * * 
        *  
      * * 
    * * * 
  * * * * 
* * * * * 
'''
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(1,n+2-i):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(1,i+2):
        print("*",end=" ")
    print()

'''
*               * 
* *           * * 
* * *       * * * 
* * * *   * * * * 
* * * * * * * * * 
'''
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(1,2*(n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j != n :             # or #   if (i != n or j!= 1):
            print("*",end=" ")
    print()


# Pascals Traingle
'''
        1   
      1   1   
    1   2   1   
  1   3   3   1   
1   4   6   4   1 
'''

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    
    c=1
    for j in range(1,i+1):
        print(c,end="   ")
        c = c * (i-j) // j
    
    print()